import os
import pandas as pd
import getpass
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import ast

# Definição de cores
VERDE = "\033[32m"
AZUL = "\033[34m"
RESET = "\033[0m"

class SistemaCRUD:
    def __init__(self, arquivo='banco_de_dados.ods'):
        self.arquivo = arquivo
        # Verifica se o arquivo existe, se não, cria um novo
        if not os.path.exists(self.arquivo):
            self.usuarios = pd.DataFrame(columns=['Usuário', 'Senha', 'Chave', 'Nível'])
            self.salvar_dados()
        else:
            self.carregar_dados()
    
    def carregar_dados(self):
        """Carrega os dados do arquivo ODS."""
        try:
            self.usuarios = pd.read_excel(self.arquivo, engine='odf')
            # Se o DataFrame estiver vazio, cria as colunas
            if self.usuarios.empty:
                self.usuarios = pd.DataFrame(columns=['Usuário', 'Senha', 'Chave', 'Nível'])
        except Exception as e:
            print(f"Erro ao carregar dados: {e}")
            # Cria um novo DataFrame se ocorrer um erro
            self.usuarios = pd.DataFrame(columns=['Usuário', 'Senha', 'Chave', 'Nível'])
    
    def salvar_dados(self):
        """Salva os dados no arquivo ODS."""
        try:
            self.usuarios.to_excel(self.arquivo, engine='odf', index=False)
            print("Dados salvos com sucesso!")
        except Exception as e:
            print(f"Erro ao salvar dados: {e}")
    
    def criptografar_senha(self, mensagem):
        """Criptografa uma senha usando AES."""
        # Gerar uma chave aleatória de 32 bytes para AES-256
        chave = os.urandom(32)
        
        # Gerar um vetor de inicialização (IV) aleatório (16 bytes para AES)
        iv = os.urandom(16)

        # Preencher a mensagem para garantir que seu tamanho seja múltiplo do tamanho do bloco
        padder = padding.PKCS7(algorithms.AES.block_size).padder()
        mensagem_padded = padder.update(mensagem.encode()) + padder.finalize()

        # Criação do objeto de cifra AES com a chave e IV
        cipher = Cipher(algorithms.AES(chave), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()

        # Criptografar a mensagem
        mensagem_criptografada = encryptor.update(mensagem_padded) + encryptor.finalize()

        # Retorna o IV concatenado com a mensagem criptografada e a chave
        return iv + mensagem_criptografada, chave
    
    def descriptografar_senha(self, mensagem_criptografada, chave):
        """Descriptografa uma senha usando AES."""
        try:
            # Extrair o IV da mensagem criptografada (os primeiros 16 bytes)
            iv = mensagem_criptografada[:16]
            mensagem_criptografada = mensagem_criptografada[16:]

            # Criação do objeto de cifra AES com a chave e IV
            cipher = Cipher(algorithms.AES(chave), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()

            # Descriptografar a mensagem
            mensagem_descriptografada = decryptor.update(mensagem_criptografada) + decryptor.finalize()

            # Remover o preenchimento (padding)
            unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
            mensagem_original = unpadder.update(mensagem_descriptografada) + unpadder.finalize()

            # Retorna a mensagem original
            return mensagem_original.decode()
        except Exception as e:
            print(f"Erro ao descriptografar: {e}")
            return None
    
    def verifica_linha(self):
        """Verifica a próxima linha disponível no DataFrame."""
        if self.usuarios.empty:
            return 0
        return len(self.usuarios)
    
    def criar_usuario(self, user, passw, nivel):
        """Cria um novo usuário com senha criptografada."""
        # Verifica se o usuário já existe
        if not self.usuarios.empty and (self.usuarios['Usuário'] == user).any():
            print("Usuário já existe!")
            return False
        
        # Criptografa a senha
        senha_criptografada, chave = self.criptografar_senha(passw)
        
        # Converte para formato armazenável
        senha_bytes = list(senha_criptografada)
        chave_bytes = list(chave)
        
        # Define o nível de acesso
        if nivel == 1:
            nivel = 'Admin'
        elif nivel == 2:
            nivel = 'Funcionario'
        elif nivel == 3:
            nivel = 'Guest'
        else:
            print('Digite um valor válido para o nível de acesso')
            return False
        
        # Adiciona o novo usuário como uma nova linha
        nova_linha = pd.DataFrame({
            'Usuário': [user],
            'Senha': [str(senha_bytes)],
            'Chave': [str(chave_bytes)],
            'Nível': [nivel]
        })
        
        self.usuarios = pd.concat([self.usuarios, nova_linha], ignore_index=True)
        
        # Salva as alterações
        self.salvar_dados()
        print(f"Usuário '{user}' criado com sucesso!")
        return True
    
    def autenticar(self, user, passw):
        """Verifica se o usuário e senha estão corretos."""
        # Verifica se o DataFrame está vazio
        if self.usuarios.empty:
            return False, None
            
        # Verifica se o usuário existe
        if not (self.usuarios['Usuário'] == user).any():
            return False, None
        
        try:
            # Obtém a senha criptografada e a chave
            senha = self.usuarios.loc[self.usuarios['Usuário'] == user, 'Senha'].iloc[0]
            chave = self.usuarios.loc[self.usuarios['Usuário'] == user, 'Chave'].iloc[0]
            nivel = self.usuarios.loc[self.usuarios['Usuário'] == user, 'Nível'].iloc[0]
            
            # Converte de string para bytes
            senha_bytes = bytes(ast.literal_eval(senha))
            chave_bytes = bytes(ast.literal_eval(chave))
            
            # Descriptografa a senha e compara
            senha_descriptografada = self.descriptografar_senha(senha_bytes, chave_bytes)
            
            if senha_descriptografada == passw:
                return True, nivel
        except Exception as e:
            print(f"Erro na autenticação: {e}")
        
        return False, None
    
    def atualizar_usuario(self, user, nv_user=None, nv_senha=None, nv_nivel=None):
        """Atualiza os dados de um usuário existente."""
        # Verifica se o DataFrame está vazio
        if self.usuarios.empty:
            print("Não há usuários cadastrados!")
            return False
            
        # Verifica se o usuário existe
        if not (self.usuarios['Usuário'] == user).any():
            print("Usuário não encontrado!")
            return False
        
        try:
            # Obtém o índice do usuário
            idx = self.usuarios[self.usuarios['Usuário'] == user].index[0]
            
            # Atualiza o nome de usuário
            if nv_user and nv_user != user:
                if (self.usuarios['Usuário'] == nv_user).any():
                    print(f"O usuário '{nv_user}' já existe!")
                    return False
                self.usuarios.loc[idx, 'Usuário'] = nv_user
                user = nv_user  # Atualiza a variável para continuar referenciando o usuário
            
            # Atualiza a senha
            if nv_senha:
                senha_criptografada, chave = self.criptografar_senha(nv_senha)
                
                # Converte para formato armazenável
                senha_bytes = list(senha_criptografada)
                chave_bytes = list(chave)
                
                self.usuarios.loc[idx, 'Senha'] = str(senha_bytes)
                self.usuarios.loc[idx, 'Chave'] = str(chave_bytes)
            
            # Atualiza o nível
            if nv_nivel:
                if nv_nivel == 1:
                    nivel = 'Admin'
                elif nv_nivel == 2:
                    nivel = 'Funcionario'
                elif nv_nivel == 3:
                    nivel = 'Guest'
                else:
                    print('Digite um valor válido para o nível de acesso')
                    return False
                
                self.usuarios.loc[idx, 'Nível'] = nivel
            
            # Salva as alterações
            self.salvar_dados()
            limpa_tela()
            print(f"Usuário '{user}' atualizado com sucesso!")
            return True
        except Exception as e:
            print(f"Erro ao atualizar usuário: {e}")
            return False
    
    def deletar_usuario(self, user):
        """Remove um usuário do sistema."""
        # Verifica se o DataFrame está vazio
        if self.usuarios.empty:
            print("Não há usuários cadastrados!")
            return False
            
        # Verifica se o usuário existe
        if not (self.usuarios['Usuário'] == user).any():
            print("Usuário não encontrado!")
            return False
        
        try:
            # Remove o usuário
            self.usuarios = self.usuarios[self.usuarios['Usuário'] != user].reset_index(drop=True)
            
            # Salva as alterações
            self.salvar_dados()
            limpa_tela()
            print(f"Usuário '{user}' removido com sucesso!")
            return True
        except Exception as e:
            print(f"Erro ao deletar usuário: {e}")
            return False
    
    def listar_usuarios(self):
        """Lista todos os usuários cadastrados."""
        if self.usuarios.empty:
            print("Não há usuários cadastrados.")
            return
        
        print("\nUsuários cadastrados:")
        for idx, row in self.usuarios.iterrows():
            print(f"{idx+1}. {row['Usuário']} - Nível: {row['Nível']}")


def limpa_tela():
    """Limpa a tela do terminal."""
    so = os.name
    if so == 'posix':
        os.system('clear')
    elif so == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def menu_interno(sistema, usuario):
    """Menu interno após login."""
    while True:
        print(f"\n{VERDE}Bem-vindo, {usuario}!{RESET}")
        print(f"{VERDE}Selecione uma das opções abaixo{RESET}")
        print(f"{AZUL}1.{RESET} Listar usuários")
        print(f"{AZUL}2.{RESET} Atualizar um cadastro")
        print(f"{AZUL}3.{RESET} Deletar um cadastro")
        print(f"{AZUL}4.{RESET} Fazer logoff")
        
        try:
            opcao = int(input("\nOpção: "))
            
            if opcao == 1:
                sistema.listar_usuarios()
                
            elif opcao == 2:
                user = input("\nDigite o usuário que deseja alterar: ")
                nv_user = input("Digite um novo usuário (deixe em branco para manter o mesmo): ")
                nv_user = nv_user if nv_user else None
                
                alt_senha = input("Deseja alterar a senha? (s/n): ")
                nv_senha = None
                if alt_senha.lower() == 's':
                    nv_senha = getpass.getpass("Digite a nova senha: ")
                
                alt_nivel = input("Deseja alterar o nível? (s/n): ")
                nv_nivel = None
                if alt_nivel.lower() == 's':
                    try:
                        nv_nivel = int(input("Digite o novo nível (1-Admin, 2-Funcionario, 3-Guest): "))
                    except ValueError:
                        print("Nível inválido!")
                        continue
                
                sistema.atualizar_usuario(user, nv_user, nv_senha, nv_nivel)
                
            elif opcao == 3:
                user = input("\nDigite o usuário que deseja deletar: ")
                confirm = input(f"Tem certeza que deseja deletar o usuário '{user}'? (s/n): ")
                if confirm.lower() == 's':
                    sistema.deletar_usuario(user)
                
            elif opcao == 4:
                print("Fazendo logoff...")
                break
                
            else:
                print("Opção inválida!")
                
        except ValueError:
            print("Por favor, digite um número válido.")


def menu_principal():
    """Menu principal do sistema."""
    sistema = SistemaCRUD()
    
    while True:
        print('\n////', end='')
        print(f"{VERDE}SISTEMA CRUD{RESET}", end='')
        print('////')
        print(f"{AZUL}1.{RESET} Fazer Login")
        print(f"{AZUL}2.{RESET} Cadastro")
        print(f"{AZUL}3.{RESET} Sair do sistema")
        
        try:
            opcao = int(input("\nOpção: "))
            
            if opcao == 1:
                user = input("Usuário: ")
                passw = getpass.getpass("Senha: ")
                
                autenticado, nivel = sistema.autenticar(user, passw)
                if autenticado:
                    limpa_tela()
                    print(f'Seja bem-vindo {user}!')
                    menu_interno(sistema, user)
                else:
                    print('Usuário ou senha incorretos')
                    input("Pressione Enter para continuar...")
                    
            elif opcao == 2:
                user = input("Novo usuário: ")
                passw = getpass.getpass("Senha: ")
                try:
                    nivel = int(input("Nível de acesso (1-Administrador, 2-Funcionário, 3-Visitante): "))
                    sistema.criar_usuario(user, passw, nivel)
                except ValueError:
                    print("Nível inválido!")
                input("Pressione Enter para continuar...")
                
            elif opcao == 3:
                print("Saindo do sistema...")
                break
                
            else:
                print("Opção inválida!")
                input("Pressione Enter para continuar...")
                
        except ValueError:
            print("Por favor, digite um número válido.")
            input("Pressione Enter para continuar...")


menu_principal()
