import csv

def adicionar_cliente():
    nome = input("Digite o nome do cliente: ")
    email = input("Digite o email do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    
    with open('clientes.csv', mode='a', newline='') as arquivo:
        escritor = csv.writer(arquivo)  # Cria um objeto escritor para escrever no arquivo CSV
        escritor.writerow([nome, email, telefone])  # Escreve uma nova linha com os dados do cliente
    
    print("Cliente adicionado com sucesso!")  # Exibe uma mensagem confirmando a adição do cliente

def visualizar_clientes():
    with open('clientes.csv', mode='r') as arquivo:
        leitor = csv.reader(arquivo)  # Cria um objeto leitor para ler o arquivo CSV
        for linha in leitor:  # Itera sobre cada linha no arquivo
            print(linha)  # Imprime a linha, que contém os dados de um cliente

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
    nome = input("Digite o nome do cliente que deseja buscar: ")  # Solicita o nome do cliente a ser buscado
    with open('clientes.csv', mode='r') as arquivo:
        leitor = csv.reader(arquivo)  # Cria um objeto leitor para ler o arquivo CSV
        for linha in leitor:  # Itera sobre cada linha no arquivo
            if linha[0] == nome:  # Se o nome na primeira posição da linha for igual ao nome buscado
                print("Cliente encontrado:")
                print(linha)  # Imprime os dados do cliente encontrado
                return  # Sai da função pois o cliente foi encontrado
        print("Cliente não encontrado.")  # Se o loop terminar sem encontrar o cliente, exibe essa mensagem

def main():
    while True:
        print("\nMenu:")
        print("1. Adicionar novo cliente")
        print("2. Visualizar todos os clientes")
        print("3. Buscar cliente pelo nome")
        print("4. Encerrar o programa")
        
        opcao = input("Escolha uma opção: ")  # Solicita ao usuário que escolha uma opção do menu
        
        if opcao == '1':
            adicionar_cliente()  # Chama a função para adicionar um novo cliente
        elif opcao == '2':
            visualizar_clientes()  # Chama a função para visualizar todos os clientes
        elif opcao == '3':
            buscar_cliente()  # Chama a função para buscar um cliente pelo nome
        elif opcao == '4':
            print("Encerrando o programa...")  # Exibe uma mensagem de encerramento
            break  # Sai do loop, encerrando o programa
        else:
            print("Opção inválida. Tente novamente.")  # Se o usuário inserir uma opção inválida, exibe essa mensagem

if __name__ == "__main__":
    main()  # Chama a função principal para iniciar o programa