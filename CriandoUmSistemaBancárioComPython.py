def exibir_menu():
    print("""
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
""")


def depositar(saldo, extrato, depositos):
    valor = float(input("Informe o valor do deposito: R$ "))
    if valor > 0:
        saldo += valor
        depositos.append(valor)
        extrato.append(f"Deposito: R$ {valor:.2f}")
        print("✅ Deposito realizado com sucesso.")
    else:
        print("❌ Operacao falhou! Valor invalido.")
    return saldo, extrato, depositos


def sacar(saldo, extrato, saques, limite_saques, limite_valor_saque):
    if len(saques) >= limite_saques:
        print("❌ Limite diario de saques excedido.")
        return saldo, extrato, saques

    valor = float(input("Informe o valor do saque: R$ "))

    if valor <= 0:
        print("❌ Operacao falhou! Valor invalido.")
    elif valor > limite_valor_saque:
        print(f"❌ Saque nao permitido acima de R$ {limite_valor_saque:.2f}.")
    elif valor > saldo:
        print("❌ Saldo insuficiente.")
    else:
        saldo -= valor
        saques.append(valor)
        extrato.append(f"Saque: R$ {valor:.2f}")
        print("✅ Saque realizado com sucesso.")
    
    return saldo, extrato, saques


def exibir_extrato(extrato, saldo):
    print("\n🧾 === EXTRATO BANCARIO ===")
    if not extrato:
        print("Sem movimentacoes registradas.")
    else:
        for item in extrato:
            print(item)
    print(f"\n💰 Saldo atual: R$ {saldo:.2f}")
    print("============================\n")


# 🔄 Loop principal do sistema
saldo = 0.0
depositos = []
saques = []
extrato = []
LIMITE_SAQUES_DIARIO = 3
VALOR_MAXIMO_SAQUE = 500.00

while True:
    exibir_menu()
    opcao = input("Escolha uma opcao: ").lower()

    if opcao == "d":
        saldo, extrato, depositos = depositar(saldo, extrato, depositos)

    elif opcao == "s":
        saldo, extrato, saques = sacar(
            saldo, extrato, saques,
            LIMITE_SAQUES_DIARIO,
            VALOR_MAXIMO_SAQUE
        )

    elif opcao == "e":
        exibir_extrato(extrato, saldo)

    elif opcao == "q":
        print("👋 Encerrando sessao. Obrigado por usar o Banco DIO Jefferson Edition!")
        break

    else:
        print("⚠️ Opcao invalida. Tente novamente.")
