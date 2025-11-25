from ia import responder

print(" DehAI iniciada! Digite 'sair' para encerrar.\n")

while True:
    user_input = input("Você: ")
    
    if user_input.lower() == "sair":
        print("DehAI: Até mais, debora!")
        break

    resposta = responder(user_input)
    print(f"DehAI: {resposta}\n")
