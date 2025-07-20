from bio.ler_fasta import ler_fasta
from bio.constantes import DNA_PARA_AMINOACIDO, DNA_STOP_CODONS

def solução_2(caminho_arquivo):
    organismos_do_fasta = ler_fasta(caminho_arquivo)
    resultados = []

    for organismo in organismos_do_fasta:
        proteinas_do_organismo = []
        # Correção: 'sequencia' e não 'sequencias'
        proteinas = organismo.sequencia.transcrever().traduzir()
        proteinas_do_organismo.append(proteinas)
        
        resultados.append({
            'id': organismo.id,
            'nome': organismo.nome,
            'proteinas': proteinas_do_organismo
        })

    return resultados
