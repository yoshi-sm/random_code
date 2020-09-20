arquivo = input("Digite o nome do arquivo de saida (ex: grafeno.xyz), caso o arquivo ja exista ele sera substituido: ")
repeticao = int(input("Digite a quantidade de repeticoes hexagonais (ex: 3): "))
qtd_atomos = repeticao * 6 * repeticao
inicial_y = 0.71 + ((repeticao - 1) * 2.13)
inicial_x = -1.23 - ((repeticao - 1) * 1.23)
espaco_x = 2.46
inicial_y2 = -inicial_y

with open(arquivo, "w") as f:
	pass

with open(arquivo, "a") as f:
	f.write(f"{qtd_atomos}\n\n")
	for j in range(repeticao):

		for i in range(repeticao + j):
			f.write(f"C {inicial_x + i * espaco_x - (j * 1.23)} {inicial_y - (j * 2.13)} 0.0\n")
			f.write(f"C {inicial_x + 1.23 + i * espaco_x - (j * 1.23)} {inicial_y + 0.71 - (j * 2.13)} 0.0\n")
		f.write(f"C {inicial_x + (i + 1) * espaco_x - (j * 1.23)} {inicial_y - (j * 2.13)} 0.0\n")
		for i in range(repeticao + j):
			f.write(f"C {inicial_x + i * espaco_x - (j * 1.23)} {inicial_y2 + (j * 2.13)} 0.0\n")
			f.write(f"C {inicial_x + 1.23 + i * espaco_x - (j * 1.23)} {inicial_y2 - 0.71 + (j * 2.13)} 0.0\n")
		f.write(f"C {inicial_x + (i + 1) * espaco_x - (j * 1.23)} {inicial_y2 + (j * 2.13)} 0.0\n")
