"2) Traduzir cada sequência de nucleotídeos para sua sequência de proteína correspondente."
from bio.ler_fasta import ler_fasta
from bio.sequencia import Sequencia
from bio.constantes import DNA_PARA_AMINOACIDO, DNA_STOP_CODONS


caminho_do_arquivo = "./arquivos/Flaviviridae-genomes.fasta"
organismos_do_fasta = ler_fasta(caminho_do_arquivo)
for organismo in organismos_do_fasta:
    for sequencia in organismo.sequencias:
        proteinas = sequencia.transcrever(caminho_do_arquivo).traduzir(caminho_do_arquivo)
        print(f"ID: {organismo.id}, Nome: {organismo.nome}, Proteínas: {proteinas}")

