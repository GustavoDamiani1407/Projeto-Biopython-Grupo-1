from bio.ler_fasta import ler_fasta

def solução_3(caminho_arquivo):
    organismos_do_fasta = ler_fasta(caminho_arquivo)
    
    organismos_com_mutacao = []
    organismos_sem_mutacao = []

    for organismo in organismos_do_fasta:
        sequencia = organismo.sequencia
        if len(sequencia) >= 1000:
            if sequencia[999] == 'G':
                organismos_com_mutacao.append(organismo)
            elif sequencia[999] == 'A':
                organismos_sem_mutacao.append(organismo)

    return {
        "com_mutacao": organismos_com_mutacao,
        "sem_mutacao": organismos_sem_mutacao
    }
