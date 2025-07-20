from bio.ler_fasta import ler_fasta
from bio.sequencia import Sequencia
from bio.organismo_fasta import OrganismoFasta

def solução_1(caminho_arquivo):
    organismos_do_fasta = ler_fasta(caminho_arquivo)
    resultados = []
    for organismo in organismos_do_fasta:
        gc = organismo.sequencia.calcular_gc()
        resultados.append({
            'id': organismo.id,
            'nome': organismo.nome,
            'gc': gc
        })
    return resultados
