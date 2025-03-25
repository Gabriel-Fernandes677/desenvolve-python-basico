urls = [
    "www.google.com",
    "www.facebook.com",
    "www.reddit.com",
    "www.github.com",
]


dominios = []

for url in urls:
   
    if url.startswith("www.") and url.endswith(".com"):
       
        dominio = url[4:-4]
        dominios.append(dominio)


print("Lista de domínios:", dominios)
