from bio.ler_fasta import ler_fasta
<<<<<<< HEAD

caminho_do_arquivo = "./arquivos/Flaviviridae-genomes.fasta"

orgnismos_do_fasta = ler_fasta(caminho_do_arquivo)

print("Os organismos desse arquivo fasta são: " )
for organismo in orgnismos_do_fasta:
    print(f"ID: {organismo.id}, Nome: {organismo.nome}, Sequência: {organismo.sequencia[:30]}...")
=======
caminho_do_arquivo = "./arquivos/Flaviviridae-genomes.fasta"
organismos = ler_fasta(caminho_do_arquivo)
print(organismos)

for organismo in organismos:
    print(f"ID: {organismo.id}")
    print(f"Nome: {organismo.nome}")
    print(f"Sequência: {organismo.sequencia[:50]}...")  

