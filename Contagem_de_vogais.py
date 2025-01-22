
texto = input("Digite um texto ou frase: ")
texto = texto.lower()  
vogais = ["a", "e", "i", "o", "u"]
total_vogais = 0  

for vogal in vogais:
    quantidade = texto.count(vogal)  
    total_vogais += quantidade
    print(f"A vogal '{vogal}' aparece {quantidade} vezes.")

print(f"Total de vogais no texto: {total_vogais}")
    