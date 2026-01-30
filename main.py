from ia import responder

ASSISTENTE_NOME = "Deia" 

print(" Deia iniciada! Digite 'sair' para encerrar.\n")

while True:
    user_input = input("Você: ")
    
    if user_input.lower() == "sair":
        print(f"{ASSISTENTE_NOME}:Até logo! Senhorita Debora, estarei sempre a sua disposição.")
        break

    resposta = responder(user_input)
    print(f"{ASSISTENTE_NOME}:{resposta}\n")