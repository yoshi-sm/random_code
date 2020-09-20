arquivo = input("Digite o nome do arquivo de saida (ex: grafeno.xyz), caso o arquivo ja exista ele sera substituido: ")

repeticao_x = int(input("Digite a quantidade de repeticoes em colunas (ex: 10): "))
repeticao_y = int(input("Digite a quantidade de repeticoes em linhas (ex: 2): "))
qtd_atomos = 2 * repeticao_x * repeticao_y

distancia_x = 4.26
distancia_y = 2.46

with open(arquivo, "w") as f:
	pass

with open(arquivo, "a") as f:
	f.write(f"{qtd_atomos} \n\n")
	for j in range(repeticao_y):
		for i in range(int(repeticao_x/2)):
			f.write(f"C {i * distancia_x + 0.0} {j * distancia_y + 0.0} 0.0\n")
			f.write(f"C {i * distancia_x + 0.71} {j * distancia_y + 1.23} 0.0\n")
			f.write(f"C {i * distancia_x + 2.13} {j * distancia_y + 1.23} 0.0\n")
			f.write(f"C {i * distancia_x + 2.84} {j * distancia_y + 0.0} 0.0\n")
		
		if repeticao_x % 2 == 1:
			f.write(f"C {int(repeticao_x / 2) * distancia_x + 0.0} {j * distancia_y + 0.0} 0.0\n")
			f.write(f"C {int(repeticao_x / 2) * distancia_x + 0.71} {j * distancia_y + 1.23} 0.0\n")

print(f"Arquivo {arquivo} criado!")
