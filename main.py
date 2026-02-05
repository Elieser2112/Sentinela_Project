from config import HOST,USER
import os
import paramiko

def boas_vindas():
    verde = "\033[92m"
    reset = "\033[0m"
    print(f"{verde}[SENTINELA V1.0]{reset} Sistema de Vigilância Ativo.")
    print(f"Alvo configurado: {HOST}")
    print("-" * 30)

def listar_arquivos_locais(diretorio):
    verde = "\033[92m"
    azul = "\033[94m"
    reset = "\033[0m"
    
    print(f"{azul}--- Iniciando Varredura ---{reset}\n")
    
    for raiz, pastas, arquivos in os.walk(diretorio):
        for nome_arquivo in arquivos:
            caminho_completo = os.path.join(raiz, nome_arquivo)

            tamanho_bytes = os.path.getsize(caminho_completo)
            tamanho_mb = tamanho_bytes / (1024*1024)

            relativo = os.path.relpath(caminho_completo, diretorio)
            print(f"{verde}[CONQUISTADO]{reset} {relativo} ({tamanho_mb:.2f} MB)")

if __name__ == "__main__":
    boas_vindas()
    listar_arquivos_locais('../../downloads/Movies')