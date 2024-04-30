import os
import shutil


def deletar_pastas_vazias(caminho_pasta):
    """Deleta pastas vazias"""
    for root, dirs, files in os.walk(caminho_pasta, topdown=False):
        for dir in dirs:
            caminho_pasta_dir = os.path.join(root, dir)
            if not os.listdir(caminho_pasta_dir):
                print(f"Deletando pasta: {caminho_pasta_dir}")
                shutil.rmtree(caminho_pasta_dir)


caminho_pasta = "."
print("Verificando por pastas vazias...")
deletar_pastas_vazias(caminho_pasta)
