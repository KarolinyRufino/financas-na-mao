# ---------------------------------------
# Finanças na mão - TELA INICIAL SIMULADA

# Dados simulados
saldo = 1250
receitas = 3200
gastos = 1950
categoria_maior_gasto = "Delivery"
historico = []

# =============== FUNÇÕES =============== 
def mostrar_historico():
    print("\n========= ÚLTIMAS TRANSAÇÕES =========\n")

    if len(historico) == 0:
        print("Nenhuma transação registrada recentemente.")
        return
    
    ultimas = historico[-3:]

    for transacao in reversed(ultimas):
        print(transacao)


    print("\n----------- RESUMO INTELIGENTE -----------")

    if gastos > receitas:
        print("⚠️ Atenção: seus gastos ultrapassaram sua renda.")
    else:
        print("✅ Sua situação financeira está controlada.")

    print(
        f"\nCategoria com maior gasto: "
        f"{categoria_maior_gasto}"
    )

    print(
        f"\n💡​ Sugestão:"
        "\nTente reduzir gastos com delivery nesta semana."
    )
    print("\n-------------------------------------")

def menu():
    while True:
        print("\n======== FINANÇAS NA MÃO ========")
        print(f"Saldo Atual: R$ {saldo}")
        print(f"Receitas do mês: R$ {receitas}")
        print(f"Gastos do mês: R$ {gastos}")

        print("\n============ MENU ============")
        print("1 - Ver historico")
        print("2 - Adicionar entrada")
        print("3 - Adicionar saída")
        print("4 - Assistente IA")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            mostrar_historico()

        elif opcao == "2":
            adicionar_entrada()

        elif opcao == "3":
            adicionar_saida()

        elif opcao == "4":
            assistente_ia()

        elif opcao == "0":
            print("\nSaindo do sistema...")
            break

        else:
            print("\n❌ Opção inválida.")
 
# ========= FUNÇÕES FINANCEIRAS =========
def adicionar_entrada():
    global saldo
    global receitas

    valor = float(
        input("\nDigite o valor da entrada: R$ ")
    )

    saldo += valor
    receitas += valor

    historico.append(
        f"Entrada: +R$ {valor:.2f}"
    )

    print("\n✅ Entrada adicionada com sucesso.")

def adicionar_saida():
    global saldo
    global gastos

    valor = float(
        input("\nDigite o valor da saída: R$ ")
    )

    saldo -= valor
    gastos += valor

    historico.append(
        f"Saída: -R$ {valor:.2f}"
    )

    print("\n✅ Saída adicionada com sucesso.")

# ---------------------------------------
# Assistente IA - TELA SIMULADA

# Dados simulados
gastos_mes_passado = 1700

def assistente_ia():
    # RESUMO IA
    if gastos > receitas:
        print(
            "Você está gastando mais do que recebe."
        )

    elif gastos >= receitas * 0.8:
        print(
            "Seus gastos estão altos este mês."
        )

    else:
        print(
            "Você está mantendo um bom controle financeiro."
        )

    # FIM RESUMO

    while True:
        print("\n====== ASSISTENTE IA ======")

        print("1 - Onde estou gastando mais?")
        print("2 - Comparar meses")
        print("3 - Ver padrões financeiros")
        print("4 - Como economizar?")
        print("5 - Organização financeira")
        print("6 - Sugestões de vendas")
        print("0 - Voltar")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            print("\nSeu maior gasto está em:")
            print(categoria_maior_gasto)

            print("\nUma boa ideia é acompanhar essa categoria mais de perto.")

        elif opcao == "2":
            diferenca = gastos - gastos_mes_passado

            if diferenca > 0:
                print(f"\nVocê gastou R$ {diferenca:.2f} a mais que no mês passado.")

            elif diferenca < 0:
                print(f"\nVocê gastou R$ {abs(diferenca):.2f} a menos que no mês passado.")
            
            else:
                print("\nSeus gastos permaneceram iguais.")
        
        elif opcao == "3":
            print("\nPadrão encontrado:")

            print("Você costuma registrar mais gastos aos finais de semana.")

            print("Vale acompanhar esses dias com mais atenção.")

        elif opcao == "4":
            print("\nSugestão de economia:")

            print("Tente definir um limite semanal para sua categoria com maior gasto.")

        elif opcao == "5":
            print("\nDica de organização:")

            print("Anote seus gastos diariamente.")

            print("Pequenos registros ajudam a evitar surpresas no fim do mês.")

        elif opcao == "6":
            print("\nOportunidades encontrada:")

            print("O Dia das Crianças está próximo.")
            print("Considere criar promoções ou pacotes especiais para essa data.")

        elif opcao == "0":
            break

        else:
            print("\nOpção inválida.")


# ---------------------------------------
# =========== INICIAR SISTEMA ===========
menu()