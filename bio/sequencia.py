# Importa as bibliotecas de constantes
from bio.constantes import DNA_PARA_AMINOACIDO
from bio.constantes import DNA_STOP_CODONS

class Sequencia:

    def __init__(self, sequencia):
        self.sequencia = sequencia.upper()  # Padroniza para maiúsculo

    def __repr__(self):
        return f'Sequencia("{self.sequencia}")'

    def __str__(self):
        return self.sequencia

    def __len__(self):
        return len(self.sequencia)

    def __eq__(self, outra_sequencia):
        return str(self) == str(outra_sequencia)

    def __getitem__(self, index):
        return self.sequencia[index]

    def __iter__(self):
        return iter(self.sequencia)

    def calcular_tamanho(self):
        return len(self.sequencia)

    def calcular_gc(self):
        gc_count = self.sequencia.count('G') + self.sequencia.count('C')
        return (gc_count / len(self.sequencia)) * 100 if len(self.sequencia) > 0 else 0

    def calcular_porcentagem_bases(self):
        total = len(self.sequencia)
        if total == 0:
            return {}
        porcentagens = {}
        for base in 'ATCG':
            porcentagens[base] = (self.sequencia.count(base) / total) * 100
        return porcentagens

    def calcular_percentual(self, bases):
        total = len(self.sequencia)
        if total == 0:
            return 0
        count = sum(self.sequencia.count(base.upper()) for base in bases)
        return (count / total) * 100

    def complementar(self):
        complementos = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        nova_seq = ''.join(complementos.get(n, 'N') for n in self.sequencia)
        return Sequencia(nova_seq)

    def complementar_reversa(self):
        return Sequencia(self.complementar().sequencia[::-1])

    def transcrever(self):
        sequencia_rna = self.sequencia.replace('T', 'U')
        return Sequencia(sequencia_rna)

    def traduzir(self, parar=False):
        rna = self.transcrever().sequencia
        proteina = []

        for i in range(0, len(rna) - 2, 3):
            codon = rna[i:i+3]

            # Adapta códons de parada para RNA
            if codon in [stop.replace('T', 'U') for stop in DNA_STOP_CODONS]:
                if parar:
                    break
                else:
                    proteina.append("*")
                    continue

            aminoacido = DNA_PARA_AMINOACIDO.get(codon.replace('U', 'T'))
            if aminoacido:
                proteina.append(aminoacido)
            else:
                proteina.append("X")

        return ''.join(proteina)