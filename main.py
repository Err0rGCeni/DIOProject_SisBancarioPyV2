def menu():
    prompt = '''
    ===== SELECIONE =====
    [ d]\tDepositar
    [ s]\tSacar
    [ e]\tExtrato
    [nu]\tNovo Usuário
    [nc]\tNova Conta
    [ q]\tSair

    '''
    return input(prompt)

# * -> Keyword only
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    ex_saldo = valor > saldo
    ex_limit = valor > limite
    ex_saques = numero_saques >= limite_saques

    if ex_saldo:
        print("Falha: Saldo insuficiente!")
    
    elif ex_limit:
        print("Falha: Saque excede o limite!")
    
    elif ex_saques:
        print("Falha: Número de saques excedido!")
    
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    
    else:
        print("Falha: Valor inválido!")
    
    return saldo, extrato



    if numero_saques < limite_saques:
        if valor <= limite and valor <= saldo:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Valor de saque excede o limite ou saldo insuficiente!")
    else:
        print("Limite de saques diários atingido!")
    return saldo, extrato

# Positional only <- /
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Valor de depósito inválido!")
    return saldo, extrato

# Positional & Keyword
def exibir_extrato(saldo, /, *, extrato):
    if extrato:
        print("Movimentações:\n" + extrato + f"Saldo atual: R$ {saldo:.2f}")
    else:
        print("Não foram realizadas movimentações.")

def filtrar_usuario(cpf, usuarios):
    print(usuarios)
    for usuario in usuarios:
        print(usuario)
        if usuario["cpf"] == cpf:
            return usuario
    return False

def cadastrar_usuario(usuarios):
    cpf = int(input("Informe o CPF (somente números): "))
    usuario = filtrar_usuario(cpf, usuarios)
    
    if usuario:
        print("Falha: CPF já utilizado.")
        return
    
    nome = input("Informe o Nome: ")
    data_nascimento = input("Informe a Data de Nascimento: ")
    endereco = input("Informe o endereço: ")
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    
    return usuario

def cadastrar_conta(agencia, numero_conta, usuarios):
    cpf = int(input("Informe o CPF do títular: "))
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Falha: Usuário não encontrado!")

def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []
    numero_conta = 1

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor de depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)
        
        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":            
            cadastrar_usuario(usuarios)
        
        elif opcao == "nc":
            conta = cadastrar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                numero_conta += 1
                contas.append(conta)
            
        elif opcao == "q":
            break

main()
