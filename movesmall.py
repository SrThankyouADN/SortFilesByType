
import os
import shutil

# Solicitar ao usuário o tamanho máximo do arquivo em KB a ser movido
tamanho_max = int(input("Digite o tamanho máximo do arquivo em KB a ser movido: "))

# Percorrer todos os arquivos em pasta_origem e suas subpastas
pasta_origem = "imagens"
num_movidos = 0

print("Processando...")
for root, dirs, files in os.walk(pasta_origem):
    for arquivo in files:
        caminho_arquivo = os.path.join(root, arquivo)
        tamanho_arquivo = os.path.getsize(caminho_arquivo) // 1024  # em KB
        if tamanho_arquivo <= tamanho_max:
            # Criar uma nova pasta no mesmo diretório do arquivo
            nome_pasta = f"arquivos-menores-que-{tamanho_max}KB"
            caminho_nova_pasta = os.path.join(os.path.dirname(root), nome_pasta)
            os.makedirs(caminho_nova_pasta, exist_ok=True)
            # Mover o arquivo para a nova pasta
            shutil.move(caminho_arquivo, os.path.join(caminho_nova_pasta, arquivo))
            num_movidos += 1

print(f"\nForam movidos {num_movidos} arquivos.")
print("Processo concluído!")




print("Processo concluído!")

