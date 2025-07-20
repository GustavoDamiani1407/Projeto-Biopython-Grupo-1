from bio.ler_fasta import ler_fasta
from bio.sequencia import Sequencia
from bio.organismo_fasta import OrganismoFasta

caminho_do_arquivo = "./arquivos/Flaviviridae-genomes.fasta"
organismos_do_fasta = ler_fasta(caminho_do_arquivo)
gc = organismos_do_fasta.calcular_gc()
print("Os organismos desse arquivo fasta são:")
for organismo in organismos_do_fasta:
    print(f"ID: {organismo.id}, Nome: {organismo.nome}, Porcentagem de GC:: {gc}%")
