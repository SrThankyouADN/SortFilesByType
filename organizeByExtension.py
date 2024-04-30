import os
import shutil
import time


def mover_arquivos(caminho_pasta):
    """
    Move todos os arquivos em um diretório e suas sub-diretórios para novos diretórios com base em suas extensões.

    Args:
        caminho_pasta (str): O caminho do diretório a ser processado.

    Retorna:
        None

    Esta função recebe um caminho de diretório como entrada e recursivamente move todos os arquivos no diretório e suas sub-diretórios para novos diretórios com base em suas extensões. Os novos diretórios são criados no mesmo diretório do diretório de entrada. A função imprime o número de arquivos movidos no final.

    Exemplo:
        >>> mover_arquivos('caminho/para/pasta')
        Processando...
        10 arquivos foram movidos.
        Processo concluído!
    """
    arquivos_movidos = 0
    total_arquivos = 0

    def mover_arquivos_recursivamente(caminho_pasta):
        nonlocal arquivos_movidos
        nonlocal total_arquivos
        for raiz, pastas, arquivos in os.walk(caminho_pasta):
            for arquivo in arquivos:
                nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
                extensao_arquivo = extensao_arquivo.replace(".", "").upper()
                total_arquivos += 1
                nova_pasta = os.path.join(os.path.dirname(caminho_pasta), extensao_arquivo)
                os.makedirs(nova_pasta, exist_ok=True)
                origem = os.path.join(raiz, arquivo)
                destino = os.path.join(nova_pasta, arquivo)
                shutil.move(origem, destino)
                arquivos_movidos += 1

    print("Processando...")
    mover_arquivos_recursivamente(caminho_pasta)
    print(f"\n{arquivos_movidos} arquivos foram movidos.")
    print("Processo concluído!")


# Solicitar ao usuário a pasta a ser percorrida
folder_path = input("Insira o caminho da pasta: ")
mover_arquivos(folder_path)
