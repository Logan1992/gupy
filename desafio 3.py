import json

# O arquivo JSON é carregado, preenchi com dados aleatórios;
with open('faturamento.json', 'r') as file:
    dados_faturamento = json.load(file)

faturamento_diario = dados_faturamento["faturamento_diario"]

# Aqui cria-se as variáveis para guardar menor faturamento, maior faturamento, soma, e média
menor_faturamento = None
maior_faturamento = None
soma_faturamento = 0
dias_com_faturamento = 0

# Resolvendo problema de faturamento igual a 0
for faturamento in faturamento_diario:
    if faturamento > 0:
        # Definir o menor e maior faturamento
        if menor_faturamento is None or faturamento < menor_faturamento:
            menor_faturamento = faturamento
        if maior_faturamento is None or faturamento > maior_faturamento:
            maior_faturamento = faturamento
        
        # Somar o faturamento e contar os dias com faturamento
        soma_faturamento += faturamento
        dias_com_faturamento += 1

# Cálculo da média mensal
media_mensal = soma_faturamento / dias_com_faturamento if dias_com_faturamento > 0 else 0

# Calculando o número de dias acima da média
dias_acima_da_media = 0
for faturamento in faturamento_diario:
    if faturamento > media_mensal:
        dias_acima_da_media += 1

# Exibir os resultados
print(f"Menor valor de faturamento: {menor_faturamento}")
print(f"Maior valor de faturamento: {maior_faturamento}")
print(f"Número de dias com faturamento superior à média: {dias_acima_da_media}")
