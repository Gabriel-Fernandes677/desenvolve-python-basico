import emoji as em

print("Emojis disponiveis: ")
print(em.emojize(':red_heart:')," - :red_heart:")
print(em.emojize(':thumbs_up:')," - :thumbs_up:")
print(em.emojize(':thinking_face:')," - :thinking_face:")
print(em.emojize(':partying_face:')," - :partying_face:")

fr = input("Digite uma frase e ela será emojizada:\n")
print(em.emojize(fr))



