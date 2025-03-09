def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while(True):

        opcao = menu().lower()

        if opcao == "d":
            while(True):
                valor_deposito = int(input("Informe o valor que deseja depositar em R$: "))
                if valor_deposito <= 0:
                    print("ERRO: Valor de depósito inválido.\nPor favor tente novamente.")

                if valor_deposito > 0:
                    break
            
            saldo += valor_deposito
            extrato += f"\nDepósito\tR$ {valor_deposito:.2f}\n"
            print(f"Deposito de R$ {valor_deposito:.2f} realizado com sucesso!")
        elif opcao == "s":
            if numero_saques >= LIMITE_SAQUES:
                print("Você já antingiu limite de saques diários.\nPor favor, volte amanhã.")
            else:
                valor_saque = int(input("Informe o valor que deseja sacar em R$: "))
                if valor_saque > 0 and valor_saque <= saldo and valor_saque <= limite:
                    saldo -= valor_saque
                    numero_saques += 1
                    extrato += f"\nSaque\tR$ {valor_saque:.2f}\n"
                    print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")
                    print(f"Número de saques realizados hoje: {numero_saques}")
                else:
                    if valor_saque > saldo:
                        mensagem_erro = "Erro: Saldo insuficiente.\nPor favor tente novamente."
                    elif valor_saque > limite:
                        mensagem_erro = "Erro: Valor do saque excede limite.\nPor favor, tente novamente."
                    else:
                        mensagem_erro = "Erro: Valor do saque deve ser positivo.\nPor favor, tente novamente."
                    print(mensagem_erro)
        elif opcao == "e":
            if extrato != "":
                print("Extrato:")
                print(f"\nSaldo:\tR$ {saldo:.2f}")
                print(extrato)
            else:
                print("Não foram realizadas movimentações.")
            
        elif opcao == "q":
            break
        else:
            print("Opção inválida, por favor selecione novamente a opção desejada.")

    print("Obrigado por usar nosso sistema. Até a próxima.")



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
    [q] Sair
    ==> """

    return input(mensagem_menu)


if __name__ == "__main__":
    main()