import csv

def adicionar_cliente():
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    
    with open('clientes.csv', mode='a', newline='') as arquivo:
        escritor = csv.writer(arquivo)
        escritor.writerow([nome, email, telefone])
    
    print("Cliente adicionado com sucesso!")

def visualizar_clientes():
    with open('clientes.csv', mode='r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(linha)

def main():
    while True:
        print("\nMenu:")
        print("1. Adicionar novo cliente")
        print("2. Visualizar todos os clientes")
        print("3. Buscar cliente pelo nome")
        print("4. Encerrar o programa")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_cliente()
        elif opcao == '2':
            visualizar_clientes()
        elif opcao == '3':
            buscar_cliente()
        elif opcao == '4':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")
            
if __name__ == "__main__":
    main()

def buscar_cliente():
    nome = input("Digite o nome do cliente que deseja buscar: ")
    with open('clientes.csv', mode='r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            if linha[0] == nome:
                print("Cliente encontrado:")
                print(linha)
                return
        print("Cliente não encontrado.")

def main():
    while True:
        print("\nMenu:")
        print("1. Adicionar novo cliente")
        print("2. Visualizar todos os clientes")
        print("3. Buscar cliente pelo nome")
        print("4. Encerrar o programa")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            adicionar_cliente()
        elif opcao == '2':
            visualizar_clientes()
        elif opcao == '3':
            buscar_cliente()
        elif opcao == '4':
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
