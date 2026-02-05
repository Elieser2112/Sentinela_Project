from config import HOST,USER

def boas_vindas():
    verde = "\033[92m"
    reset = "\033[0m"
    print(f"{verde}[SENTINELA V1.0]{reset} Sistema de Vigilância Ativo.")
    print(f"Alvo configurado: {HOST}")
    print("-" * 30)

if __name__ == "__main__":
    boas_vindas()