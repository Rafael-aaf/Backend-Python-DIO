
def depositar(saldo, valor, extrato, /):
        
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Operação falhou! O valor informado é inválido.")
        
        print("\n================ EXTRATO ================")
        print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

        return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

        print("\n================ EXTRATO ================")
        print(extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")


def cadastrar_usuario(nome, data_nascimento, cpf, endereco, lista_usuarios):
        if cpf not in lista_usuarios:
            lista_usuarios[cpf] = {
                "nome": nome,
                "data_nascimento": data_nascimento,
                "endereço": endereco
                }
            print("\nUsuário cadastrado!")
        else:
            print("\nuUsuário já está cadastrado!")
        

def cadastrar_conta(cpf, lista_conta, numero_agencia, lista_usuarios):
        if cpf in lista_usuarios:
            lista_conta.append([cpf, "0001", numero_agencia])
            print("Conta cadastrada com sucesso")
        
        else:
             print("Usuario precisa estar cadastrado")


def main():
    menu = """

    [d] Depositar
    [s] Sacar
    [e] Extrato
    [u] Cadastrar Usuário
    [c] Cadastrar Conta Corrente
    [q] Sair

    => """

    lista_usuarios = {}
    lista_conta = []
    numero_agencia = 1
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3


    while True:

        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)
            

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)
            

        elif opcao == "e":
            exibir_extrato(saldo, extrato)


        elif opcao == "u":
            nome = str(input("Informe o seu nome: "))
            data_nascimento = str(input("Informe sua data de nascimento: "))
            endereco = str(input("Informe o seu endereço: "))
            cpf = str(input("Informe o seu cpf: "))

            cadastrar_usuario(nome, data_nascimento, cpf, endereco, lista_usuarios)


        elif opcao == "c":
            cpf = str(input("Informe o seu cpf: "))

            cadastrar_conta(cpf, lista_conta, numero_agencia, lista_usuarios)


        elif opcao == "q":
            break


        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


if __name__ == "__main__":
    main()