import csv

print("=== GERADOR DE ORÇAMENTO - IMOBILIÁRIA R.M ===")

while True:
    print("\nTipos de locação:")
    print("1 - Apartamento (R$700,00 / 1 quarto)")
    print("2 - Casa (R$900,00 / 1 quarto)")
    print("3 - Estúdio (R$1200,00)")

    tipo_imovel = int(input("Escolha o tipo de imóvel (1-3): "))

    if tipo_imovel == 1:
        valor_base = 700
        nome = "Apartamento"
    elif tipo_imovel == 2:
        valor_base = 900
        nome = "Casa"
    elif tipo_imovel == 3:
        valor_base = 1200
        nome = "Estúdio"
    else:
        print("Opção inválida. Tente novamente.")
        continue

    if tipo_imovel in [1, 2]:
        while True:
            quartos = int(input("Quantos quartos deseja (1 ou 2)? "))
            if quartos == 1:
                break
            elif quartos == 2:
                if tipo_imovel == 1:
                    valor_base += 200
                elif tipo_imovel == 2:
                    valor_base += 250
                break
            else:
                print("Digite apenas 1 ou 2.")

    else:
        quartos = 1

    while True:
        garagem = input("Deseja vaga de garagem/estacionamento? (s/n): ").lower()
        if garagem == "s":
            if tipo_imovel == 3:
                while True:
                    vagas = int(input("Quantas vagas de estacionamento? "))
                    if vagas == 1 or vagas == 2:
                        valor_base += 250
                        break
                    elif vagas > 2:
                        valor_base += 250 + (vagas - 2) * 60
                        break
                    else:
                        print("Digite um número válido de vagas.")
            else:
                valor_base += 300
            break
        elif garagem == "n":
            break
        else:
            print("Digite apenas 's' ou 'n'.")

    while True:
        criancas = input("Possui crianças? (s/n): ").lower()
        if criancas == "s":
            break
        elif criancas == "n":
            if tipo_imovel == 1:
                valor_base *= 0.95
            break
        else:
            print("Digite apenas 's' ou 'n'.")

    print("\n--- RESULTADO DO ORÇAMENTO ---")
    print(f"Tipo de imóvel: {nome}")
    print(f"Quartos: {quartos}")
    print(f"Valor total: R${valor_base:.2f}")

    contrato = 2000
    parcelas = int(input("Deseja parcelar o contrato em quantas vezes (1 a 5)? "))

    if parcelas < 1 or parcelas > 5:
        print("Número de parcelas inválido. Considerando pagamento à vista.")
        parcelas = 1

    valor_parcela = contrato / parcelas
    print(f"Contrato de R${contrato:.2f} em {parcelas}x de R${valor_parcela:.2f}")

    with open("orcamento.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Descrição", "Valor (R$)"])
        writer.writerow(["Tipo de imóvel", nome])
        writer.writerow(["Quartos", quartos])
        writer.writerow(["Valor total", f"{valor_base:.2f}"])
        writer.writerow(["Contrato total", f"{contrato:.2f}"])
        writer.writerow(["Parcelas", f"{parcelas}x de {valor_parcela:.2f}"])

    print("Arquivo 'orcamento.csv' gerado com sucesso.")

    repetir = input("\nDeseja gerar outro orçamento? (s/n): ").lower()
    if repetir == "n":
        print("Encerrando o programa. Obrigado por usar o Gerador de Orçamento R.M.")
    break
