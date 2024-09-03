# A String será informada pelo usuário
string_orgn = input("Digite a string que deseja inverter: ")

# Iniciando uma variável para guardar a inversão
string_invr = ""

# Vamos percorrer a string, só que de trás para frente
for i in range(len(string_orgn) - 1, -1, -1):
    string_invr += string_orgn[i]

# Exibir a string invertida
print("String invertida:", string_invr)
