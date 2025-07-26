from problemas.problema_1 import solução_1
from problemas.problema_2 import solução_2
from problemas.problema_3 import solução_3

# Caminho do arquivo FASTA
caminho_do_arquivo = "arquivos/Flaviviridae-genomes.fasta"

def exibir_menu():
    print("\nSelecione uma opção:")
    print("1 - Resolver Problema 1 (GC content por organismo)")
    print("2 - Resolver Problema 2 (Tradução para proteínas)")
    print("3 - Resolver Problema 3 (Relatório de mutação na posição 1000)")
    print("4 - Resolver Problema 3 (Relatório de mutação na posição 1000) - versão completa")
    print("5 - Sair")

def resolver_problema_1():
    resultados_gc = solução_1(caminho_do_arquivo)
    print("\n[Problema 1] GC content por organismo:")
    for res in resultados_gc:
        print(f"ID: {res['id']}, Nome: {res['nome']}, GC: {res['gc']:.2f}%")

def resolver_problema_2():
    resultados_proteinas = solução_2(caminho_do_arquivo)
    print("\n[Problema 2] Tradução para proteínas:")
    for res in resultados_proteinas:
        print(f"ID: {res['id']}, Nome: {res['nome']}")
        for i, prot in enumerate(res['proteinas'], 1):
            print(f"  Proteína {i}: {prot}")

def resolver_problema_3():
    resultado_mutacao = solução_3(caminho_do_arquivo)
    print("\n[Problema 3] Relatório de mutação na posição 1000:")
    print(f"Total com mutação (posição 1000 == 'G'): {len(resultado_mutacao['com_mutacao'])}")
    print(f"Total sem mutação (posição 1000 == 'A'): {len(resultado_mutacao['sem_mutacao'])}")

def resolver_problema_3_alternativo():
    resultado_mutacao = solução_3(caminho_do_arquivo)
    print("\n[Problema 3] Relatório de mutação na posição 1000:")
    com_mutacao = resultado_mutacao['com_mutacao']
    sem_mutacao = resultado_mutacao['sem_mutacao']

    with open("organismos_com_mutacao.tsv", "w", encoding="utf-8") as f_mut:
        f_mut.write("ID\tNome\n")
        for org in com_mutacao:
            f_mut.write(f"{org.id}\t{org.nome}\n")

    with open("organismos_sem_mutacao.tsv", "w", encoding="utf-8") as f_sem:
        f_sem.write("ID\tNome\n")
        for org in sem_mutacao:
            f_sem.write(f"{org.id}\t{org.nome}\n")

    print(f"Total com mutação: {len(com_mutacao)}")
    if com_mutacao:
        print("Organismos com mutação, basta verificar o arquivo 'organismos_com_mutacao.tsv':")


    print(f"Total sem mutação: {len(sem_mutacao)}")
    if sem_mutacao:
        print("Organismos sem mutação: basta verificar o arquivo 'organismos_sem_mutacao.tsv':")


    print("\nArquivos 'organismos_com_mutacao.tsv' e 'organismos_sem_mutacao.tsv' gerados com sucesso.")

if __name__ == "__main__":
    while True:
        exibir_menu()
        escolha = input("Digite a opção desejada: ").strip()

        if escolha == "1":
            resolver_problema_1()
        elif escolha == "2":
            resolver_problema_2()
        elif escolha == "3":
            resolver_problema_3()
        elif escolha == "4":
            resolver_problema_3_alternativo()
        elif escolha == "5":
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Por favor, digite uma opção entre 1 e 5.")

