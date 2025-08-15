import hashlib
import os
import sys

def gerar_hash(texto, algoritmo='sha256'):
    """
    Gera hash de uma string usando o algoritmo especificado
    
    Args:
        texto (str): Texto para gerar o hash
        algoritmo (str): Algoritmo de hash (md5, sha1, sha256, sha512)
    
    Returns:
        str: Hash gerado
    """
    try:
        # Converte o texto para bytes
        texto_bytes = texto.encode('utf-8')
        
        # Cria o objeto hash baseado no algoritmo
        if algoritmo.lower() == 'md5':
            hash_obj = hashlib.md5(texto_bytes)
        elif algoritmo.lower() == 'sha1':
            hash_obj = hashlib.sha1(texto_bytes)
        elif algoritmo.lower() == 'sha256':
            hash_obj = hashlib.sha256(texto_bytes)
        elif algoritmo.lower() == 'sha512':
            hash_obj = hashlib.sha512(texto_bytes)
        else:
            raise ValueError(f"Algoritmo '{algoritmo}' não suportado")
        
        return hash_obj.hexdigest()
    
    except Exception as e:
        return f"Erro ao gerar hash: {str(e)}"

def gerar_hash_arquivo(caminho_arquivo, algoritmo='sha256'):
    """
    Gera hash de um arquivo usando o algoritmo especificado
    
    Args:
        caminho_arquivo (str): Caminho para o arquivo
        algoritmo (str): Algoritmo de hash (md5, sha1, sha256, sha512)
    
    Returns:
        str: Hash gerado
    """
    try:
        # Verifica se o arquivo existe
        if not os.path.exists(caminho_arquivo):
            return f"Erro: Arquivo '{caminho_arquivo}' não encontrado"
        
        # Cria o objeto hash baseado no algoritmo
        if algoritmo.lower() == 'md5':
            hash_obj = hashlib.md5()
        elif algoritmo.lower() == 'sha1':
            hash_obj = hashlib.sha1()
        elif algoritmo.lower() == 'sha256':
            hash_obj = hashlib.sha256()
        elif algoritmo.lower() == 'sha512':
            hash_obj = hashlib.sha512()
        else:
            raise ValueError(f"Algoritmo '{algoritmo}' não suportado")
        
        # Lê o arquivo em blocos para economizar memória
        with open(caminho_arquivo, 'rb') as arquivo:
            while bloco := arquivo.read(8192):
                hash_obj.update(bloco)
        
        return hash_obj.hexdigest()
    
    except Exception as e:
        return f"Erro ao gerar hash do arquivo: {str(e)}"

def menu_principal():
    """
    Menu principal do gerador de hash
    """
    print("\n=== GERADOR DE HASHCODE ===")
    print("1. Gerar hash de texto")
    print("2. Gerar hash de arquivo")
    print("3. Sair")
    
    while True:
        try:
            opcao = input("\nEscolha uma opção (1-3): ").strip()
            
            if opcao == '1':
                gerar_hash_texto()
            elif opcao == '2':
                gerar_hash_arquivo_menu()
            elif opcao == '3':
                print("Saindo...")
                break
            else:
                print("Opção inválida! Escolha 1, 2 ou 3.")
        
        except KeyboardInterrupt:
            print("\nSaindo...")
            break
        except Exception as e:
            print(f"Erro: {str(e)}")

def gerar_hash_texto():
    """
    Interface para gerar hash de texto
    """
    print("\n--- Gerar Hash de Texto ---")
    
    texto = input("Digite o texto: ")
    if not texto:
        print("Texto não pode estar vazio!")
        return
    
    print("\nAlgoritmos disponíveis:")
    print("1. MD5")
    print("2. SHA1")
    print("3. SHA256 (padrão)")
    print("4. SHA512")
    
    algoritmos = {'1': 'md5', '2': 'sha1', '3': 'sha256', '4': 'sha512'}
    
    escolha = input("Escolha o algoritmo (1-4, Enter para SHA256): ").strip()
    if not escolha:
        escolha = '3'
    
    if escolha not in algoritmos:
        print("Opção inválida! Usando SHA256.")
        algoritmo = 'sha256'
    else:
        algoritmo = algoritmos[escolha]
    
    hash_resultado = gerar_hash(texto, algoritmo)
    
    print(f"\nTexto: {texto}")
    print(f"Algoritmo: {algoritmo.upper()}")
    print(f"Hash: {hash_resultado}")

def gerar_hash_arquivo_menu():
    """
    Interface para gerar hash de arquivo
    """
    print("\n--- Gerar Hash de Arquivo ---")
    
    caminho = input("Digite o caminho do arquivo: ").strip()
    if not caminho:
        print("Caminho não pode estar vazio!")
        return
    
    print("\nAlgoritmos disponíveis:")
    print("1. MD5")
    print("2. SHA1")
    print("3. SHA256 (padrão)")
    print("4. SHA512")
    
    algoritmos = {'1': 'md5', '2': 'sha1', '3': 'sha256', '4': 'sha512'}
    
    escolha = input("Escolha o algoritmo (1-4, Enter para SHA256): ").strip()
    if not escolha:
        escolha = '3'
    
    if escolha not in algoritmos:
        print("Opção inválida! Usando SHA256.")
        algoritmo = 'sha256'
    else:
        algoritmo = algoritmos[escolha]
    
    print(f"\nProcessando arquivo '{caminho}'...")
    hash_resultado = gerar_hash_arquivo(caminho, algoritmo)
    
    print(f"\nArquivo: {caminho}")
    print(f"Algoritmo: {algoritmo.upper()}")
    print(f"Hash: {hash_resultado}")

if __name__ == "__main__":
    menu_principal()