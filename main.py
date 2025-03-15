import random as r

# DECLARAÇÃO DE CONSTANTES GLOBAIS

LIMITE_SAQUES = 3
NUMERO_AGENCIA = "0001"

# FUNÇÃO PRINCIPAL DO PROGRAMA

def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0

    usuarios = []
    contas = []

    while(True):

        opcao = menu().lower()

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo=saldo, limite=limite, extrato=extrato, numero_saques=numero_saques)
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "u":
            usuarios.append(criar_usuario(usuarios))
        elif opcao == "c":
            nova_conta = criar_conta(usuarios)
            if nova_conta != None:
                contas.append(nova_conta)
        elif opcao == "l":
            listar_contas(contas)
        elif opcao == "q":
            break
        else:
            print("Opção inválida, por favor selecione novamente a opção desejada.")

    
    print("Obrigado por usar nosso sistema. Até a próxima.")



# FUNÇÃO DE EXIBIR MENU

def menu():
    saudacao1 = "Olá, seja bem vindo ao Sistema Bancário Quero-Tudo-Que-É-Seu".center(80,"$")
    saudacao2 = "Por favor, escolha uma operação abaixo:".center(80,"$")

    mensagem_menu = f"""
    {saudacao1}
    {saudacao2}
    Menu:
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Cadastrar novo usuário
    [c] Criar nova conta
    [l] Listar contas
    [q] Sair
    ==> """

    return input(mensagem_menu)


# FUNÇÃO DE FAZER DEPOSITO

def depositar(saldo, extrato, /):
    while(True):
        valor_deposito = int(input("Informe o valor que deseja depositar em R$: "))
        if valor_deposito <= 0:
            print("ERRO: Valor de depósito inválido.\nPor favor tente novamente.")

        if valor_deposito > 0:
            break
            
    saldo += valor_deposito
    extrato += f"\nDepósito\tR$ {valor_deposito:.2f}\n"
    print(f"Deposito de R$ {valor_deposito:.2f} realizado com sucesso!")

    return saldo, extrato


# FUNÇÃO DE SACAR DINHEIRO

def sacar(*, saldo, limite, extrato, numero_saques):
    if numero_saques >= LIMITE_SAQUES:
        print("Você já antingiu limite de saques diários.\nPor favor, volte amanhã.")
    else:
        valor_saque = int(input("Informe o valor que deseja sacar em R$: "))
        if valor_saque > 0 and valor_saque <= saldo and valor_saque <= limite:
            saldo -= valor_saque
            numero_saques += 1
            extrato += f"\nSaque\tR$ {valor_saque:.2f}\n"
            print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")
        else:
            if valor_saque > saldo:
                mensagem_erro = "Erro: Saldo insuficiente.\nPor favor tente novamente."
            elif valor_saque > limite:
                mensagem_erro = "Erro: Valor do saque excede limite.\nPor favor, tente novamente."
            else:
                mensagem_erro = "Erro: Valor do saque deve ser positivo.\nPor favor, tente novamente."
            print(mensagem_erro)

    return saldo, extrato, numero_saques


# FUNÇÃO DE EXIBIR O EXTRATO

def exibir_extrato(saldo, /, *, extrato):
    if extrato != "":
        print("Extrato:")
        print(f"\nSaldo:\tR$ {saldo:.2f}")
        print(extrato)
    else:
        print("Não foram realizadas movimentações.")


# FUNÇÃO DE CADASTRAR NOVO CLIENTE

def criar_usuario(usuarios):
    nome = input("Informe o nome do cliente: ")
    data_nascimento = input("Informe a data de nascimento do cliente (dd-mm-aaaa): ")
    
    while(True):
        cpf = input("Informe o cpf do cliente (apenas número): ")
        controle = 0
        for usuario in usuarios:
            if cpf == usuario["cpf"]:
                controle += 1
        if cpf.isnumeric() and controle == 0:
            break
        else:
            if controle != 0:
                print("ERRO: Cpf já existe no banco de dados\nPor favor tente novamente")
            else:
                print("ERRO: Cpf deve ter apenas número\nPor favor tente novamente")
            
    print("Informe o endereço do cliente:")
    logradouro = input("Logradouro: ")
    numero = int(input("Número: "))
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    sigla_estado = input("Sigla do estado: ")
    endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{sigla_estado}"

    cliente = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    print("Novo usuário cadastrado com sucesso!")

    return cliente


# FUNÇÃO DE GERAR NUMERO DE CONTA ALEATÓRIO

def gerar_numero_conta():
    primeiro_digito = "1"
    outros_digitos = "".join([str(r.randint(0,9)) for i in range(9)])

    return primeiro_digito + outros_digitos

# FUNÇÃO DE CRIAR NOVA CONTA

def criar_conta(usuarios):
    cpf = input("Informe o cpf do cliente (apenas número): ")
    controle = 0
    for indice, usuario in enumerate(usuarios):
        if cpf == usuario["cpf"]:
            controle += 1
            indice_encontrado = indice

    if controle != 0:
        print("Criando contra, por favor aguarde...")
        numero_conta = gerar_numero_conta()
        print("Conta criada com sucesso!")
        return {"agencia": NUMERO_AGENCIA, "numero_conta": numero_conta, "usuario": usuarios[indice_encontrado]}
    
    print("Usuário não encontrado! Por favor, tente novamente com um usuário cadastrado")


# FUNÇÃO DE LISTAR CONTAS

def listar_contas(contas):
    listagem_contas = ""
    print("Listagem de contas")
    for conta in contas:
        listagem_contas += f"\nAgência: {conta['agencia']}\nNúmero da Conta: {conta['numero_conta']}\nTitular: {conta['usuario']['nome']}\n"

    print(listagem_contas)


if __name__ == "__main__":
    main()