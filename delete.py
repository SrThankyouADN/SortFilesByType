import os
import shutil
import time


def deletar_arquivos(extensoes, nome_pasta):
    """
    Deleta arquivos com as especificadas extensões em uma pasta e suas subpastas.

    Args:
        extensoes (str): Lista de extensões de arquivo separadas por vírgulas para deletar.
        nome_pasta (str): Nome da pasta para pesquisa por arquivos a serem deletados.

    Returns:
        None

    Esta função recebe uma lista de extensões de arquivo e o nome de uma pasta como entrada. Ela pesquisa recursivamente por arquivos na
    especificada pasta e suas subpastas. Se um arquivo corresponder a uma extensão especificada, ele é deletado. O número de arquivos deletados é impresso no final.

    Exemplo:
        >>> deletar_arquivos('txt,py', 'minha_pasta')
        Processando...
        5 arquivos foram deletados.
        Processo concluído!
    """
    extensoes = [ext.strip() for ext in extensoes.split(",")]
    num_deletados = 0
    total_arquivos = 0

    def deletar_arquivos_recursivamente(caminho_pasta):
        nonlocal num_deletados
        nonlocal total_arquivos
        for root, dirs, files in os.walk(caminho_pasta):
            for arquivo in files:
                nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
                ext_arquivo = ext_arquivo.replace(".", "")
                total_arquivos += 1
                if ext_arquivo in extensoes:
                    caminho_arquivo = os.path.join(root, arquivo)
                    os.remove(caminho_arquivo)
                    num_deletados += 1

    print("Processando...")
    deletar_arquivos_recursivamente("Pasta desconhecida")
    print(f"\n{num_deletados} arquivos foram deletados.")
    print("Processo concluído!")


# Solicitar ao usuário as extensões dos arquivos e nome da pasta
extensoes = input("Insira as extensões dos arquivos separadas por vírgulas: ")
nome_pasta = input("Insira o nome da pasta (pressione enter para manter o nome padrão): ")
if not nome_pasta:
    nome_pasta = extensoes.split(",")[0]

deletar_arquivos(extensoes, nome_pasta)
