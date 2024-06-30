# Programa para gerenciar cadastro de funcionários

def mostrar_menu():
    # Função para mostrar o menu de opções
    print("\nMenu:")  # Exibe o título do menu
    print("1. Adicionar novo funcionário")  # Opção para adicionar novo funcionário
    print("2. Atualizar informações de funcionário")  # Opção para atualizar informações de um funcionário existente
    print("3. Remover funcionário")  # Opção para remover um funcionário
    print("4. Visualizar detalhes de um funcionário")  # Opção para visualizar detalhes de um funcionário
    print("5. Listar todos os funcionários")  # Opção para listar todos os funcionários
    print("6. Sair")  # Opção para sair do programa

def adicionar_funcionario(funcionários):
    # Função para adicionar um novo funcionário
    id_func = input("Digite o ID do funcionário: ")  # Pede o ID do funcionário
    if id_func in funcionários:
        # Verifica se o ID já existe
        print("ID já existe. Tente novamente.")  # Informa que o ID já existe
        return  # Sai da função
    nome = input("Digite o nome do funcionário: ")  # Pede o nome do funcionário
    cargo = input("Digite o cargo do funcionário: ")  # Pede o cargo do funcionário
    salario = float(input("Digite o salário do funcionário: "))  # Pede o salário do funcionário
    funcionários[id_func] = {"nome": nome, "cargo": cargo, "salário": salario}  # Adiciona o funcionário ao dicionário
    print("Funcionário adicionado com sucesso.")  # Informa que o funcionário foi adicionado

def atualizar_funcionario(funcionários):
    # Função para atualizar as informações de um funcionário
    id_func = input("Digite o ID do funcionário a ser atualizado: ")  # Pede o ID do funcionário
    if id_func not in funcionários:
        # Verifica se o ID não existe
        print("ID não encontrado. Tente novamente.")  # Informa que o ID não foi encontrado
        return  # Sai da função
    nome = input(f"Novo nome ({funcionários[id_func]['nome']}): ")  # Pede o novo nome (mostra o nome atual)
    cargo = input(f"Novo cargo ({funcionários[id_func]['cargo']}): ")  # Pede o novo cargo (mostra o cargo atual)
    salario = input(f"Novo salário ({funcionários[id_func]['salário']}): ")  # Pede o novo salário (mostra o salário atual)
    if nome:
        # Verifica se foi digitado um novo nome
        funcionários[id_func]['nome'] = nome  # Atualiza o nome do funcionário
    if cargo:
        # Verifica se foi digitado um novo cargo
        funcionários[id_func]['cargo'] = cargo  # Atualiza o cargo do funcionário
    if salario:
        # Verifica se foi digitado um novo salário
        funcionários[id_func]['salário'] = float(salario)  # Atualiza o salário do funcionário
    print("Funcionário atualizado com sucesso.")  # Informa que o funcionário foi atualizado

def remover_funcionario(funcionários):
    # Função para remover um funcionário
    id_func = input("Digite o ID do funcionário a ser removido: ")  # Pede o ID do funcionário
    if id_func in funcionários:
        # Verifica se o ID existe
        del funcionários[id_func]  # Remove o funcionário do dicionário
        print("Funcionário removido com sucesso.")  # Informa que o funcionário foi removido
    else:
        print("ID não encontrado. Tente novamente.")  # Informa que o ID não foi encontrado

def visualizar_funcionario(funcionários):
    # Função para visualizar os detalhes de um funcionário
    id_func = input("Digite o ID do funcionário: ")  # Pede o ID do funcionário
    if id_func in funcionários:
        # Verifica se o ID existe
        print(f"ID: {id_func}")  # Mostra o ID do funcionário
        print(f"Nome: {funcionários[id_func]['nome']}")  # Mostra o nome do funcionário
        print(f"Cargo: {funcionários[id_func]['cargo']}")  # Mostra o cargo do funcionário
        print(f"Salário: {funcionários[id_func]['salário']}")  # Mostra o salário do funcionário
    else:
        print("ID não encontrado. Tente novamente.")  # Informa que o ID não foi encontrado

def listar_funcionarios(funcionários):
    # Função para listar todos os funcionários
    if not funcionários:
        # Verifica se não há funcionários cadastrados
        print("Nenhum funcionário cadastrado.")  # Informa que não há funcionários cadastrados
        return  # Sai da função
    print("Lista de todos os funcionários:")  # Exibe o título da lista
    for id_func, info in funcionários.items():
        # Itera sobre o dicionário de funcionários
        print(f"ID: {id_func}, Nome: {info['nome']}, Cargo: {info['cargo']}, Salário: {info['salário']}")  # Mostra os detalhes de cada funcionário

def main():
    # Função principal do programa
    funcionários = {}  # Cria um dicionário vazio para armazenar os funcionários
    while True:
        # Loop principal do programa
        mostrar_menu()  # Mostra o menu de opções
        opcao = input("Escolha uma opção: ")  # Pede para o usuário escolher uma opção
        if opcao == '1':
            # Se a opção for 1, adiciona um novo funcionário
            adicionar_funcionario(funcionários)
        elif opcao == '2':
            # Se a opção for 2, atualiza as informações de um funcionário
            atualizar_funcionario(funcionários)
        elif opcao == '3':
            # Se a opção for 3, remove um funcionário
            remover_funcionario(funcionários)
        elif opcao == '4':
            # Se a opção for 4, visualiza os detalhes de um funcionário
            visualizar_funcionario(funcionários)
        elif opcao == '5':
            # Se a opção for 5, lista todos os funcionários
            listar_funcionarios(funcionários)
        elif opcao == '6':
            # Se a opção for 6, sai do programa
            print("Saindo do programa.")  # Informa que o programa está saindo
            break  # Sai do loop
        else:
            print("Opção inválida. Tente novamente.")  # Informa que a opção é inválida

if __name__ == "__main__":
    # Verifica se o script está sendo executado diretamente
    main()  # Chama a função principal
