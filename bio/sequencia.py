class Sequencia:

    def __init__(self, sequencia):
        self.sequencia = sequencia

    def __repr__(self):
        return f'Sequencia("{self.sequencia}")'

    def __iter__(self):
        return self.sequencia

    def __str__(self):
        return self.sequencia

    def __len__(self):
        return len(self.sequencia)

    def __eq__(self, outra_sequencia):
        return str(self) == str(outra_sequencia)

    def __getitem__(self, index):
        return self.sequencia.__getitem__(index)
    
    def calcular_tamanho(self):
        return len(self.sequencia)
    
    def calcular_gc(self):
        gc_count = self.sequencia.count('G') + self.sequencia.count('C')
        return (gc_count / len(self.sequencia)) * 100 if len(self.sequencia) > 0 else 0
    
    def sequencia_complementar(self):
        complementos = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
        return ''.join(complementos[nucleo] for nucleo in self.sequencia)

