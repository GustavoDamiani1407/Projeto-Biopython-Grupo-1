
from problemas.problema_1 import solução_1

caminho_do_arquivo = "arquivos/Flaviviridae-genomes.fasta"

resultados = solução_1(caminho_do_arquivo)

print("Os organismos desse arquivo fasta são:")
for res in resultados:
    print(f"ID: {res['id']}, Nome: {res['nome']}, Porcentagem de GC: {res['gc']:.2f}%")

