"3. Gerar um relatório que indique quais sequências possuem a mutação e quais não possuem."
from bio.ler_fasta import ler_fasta
from bio.sequencia import Sequencia
from bio.organismo_fasta import OrganismoFasta
from bio.constantes import DNA_PARA_AMINOACIDO, DNA_STOP_CODONS

caminho_do_arquivo = "./arquivos/Flaviviridae-genomes.fasta"
organismos_do_fasta = ler_fasta(caminho_do_arquivo)
for organismo in organismos_do_fasta:
    sequencia = organismo.sequencia
    if len(sequencia) >= 1000:
        mutacao_presente = sequencia[999] == 'G' 
        mutacao_ausente = sequencia[999] == "A"
        organismo_com_mutacao = []
        organismo_sem_mutacao = []
        if mutacao_presente:
            organismo_com_mutacao.append(organismo)
        elif mutacao_ausente:
            organismo_sem_mutacao.append(organismo)
        total_com_mutacao = len(organismo_com_mutacao)
        total_sem_mutacao = len(organismo_sem_mutacao)
print(f"Total de organismos com mutação na posição 1000: {total_com_mutacao}")