from bio.ler_fasta import ler_fasta
caminho_do_arquivo = "./arquivos/Flaviviridae-genomes.fasta"
organismos = ler_fasta(caminho_do_arquivo)
print(organismos)

for organismo in organismos:
    print(f"ID: {organismo.id}")
    print(f"Nome: {organismo.nome}")
    print(f"Sequência: {organismo.sequencia[:50]}...")  
