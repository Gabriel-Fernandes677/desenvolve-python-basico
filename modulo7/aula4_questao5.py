livros = [
    ["O Caçador de Pipas", "Khaled Hosseini", 2003, 368],
    ["Torto Arado", "Itamar Vieira Junior", 2019, 264],
    ["1984", "George Orwell", 1949, 328],
    ["Dom Casmurro", "Machado de Assis", 1899, 448],
    ["O Hobbit", "J.R.R. Tolkien", 1937, 310],
    ["A Culpa é das Estrelas", "John Green", 2012, 318],
    ["A Revolução dos Bichos", "George Orwell", 1945, 112],
    ["Cem Anos de Solidão", "Gabriel García Márquez", 1967, 448],
    ["O Senhor dos Anéis: A Sociedade do Anel", "J.R.R. Tolkien", 1954, 423],
    ["O Grande Gatsby", "F. Scott Fitzgerald", 1925, 180]
]

# Abrir o arquivo CSV para escrita
with open("meus_livros.csv", "w", encoding="utf-8") as arquivo:
    # Escrever os títulos das colunas
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")
    
    # Escrever as informações de cada livro
    for livro in livros:
        arquivo.write(f"{livro[0]},{livro[1]},{livro[2]},{livro[3]}\n")

print("Arquivo CSV criado com sucesso!")
