agenda = {
    "Ana":"1234-5678",
    "Pedro":"8765 - 4321",
    "Maria":"1357-2468"
    }
nome = input("Qual o nome: ")
numero = input("Qual o número: ")
agenda[nome] = numero
print(agenda)
while True:
    pergunta = input("Quer cadastras mais algum contato ? (s/n) ").strip().lower()
    if pergunta == "s":
       nome = input("Qual o nome: ").strip()
       numero = input("Qual o número: ").strip()
       agenda[nome] = numero
       print(agenda)
    elif pergunta == "n":
      print("Cadastro efetuado com sucesso!")
      print(agenda)
      break
    else:
       print("Resposta inválida.")
buscar_nome = input("Digite o nome do contato de deseja buscar: ").strip()
telefone = agenda.get(buscar_nome, "Contato não encontrado.")
print(f"Telefone de {buscar_nome}: {telefone}")       