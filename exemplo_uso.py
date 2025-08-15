#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo de uso do gerador de hashcode
Este arquivo demonstra como usar as funções do gerador_hash.py programaticamente
"""

from gerador_hash import gerar_hash, gerar_hash_arquivo
import os

def exemplo_hash_texto():
    """
    Demonstra como gerar hash de textos
    """
    print("=== Exemplo: Hash de Texto ===")
    
    textos = [
        "Hello World",
        "Python é incrível!",
        "123456",
        "Este é um texto mais longo para demonstrar o gerador de hash"
    ]
    
    algoritmos = ['md5', 'sha1', 'sha256', 'sha512']
    
    for texto in textos:
        print(f"\nTexto: '{texto}'")
        for algoritmo in algoritmos:
            hash_resultado = gerar_hash(texto, algoritmo)
            print(f"  {algoritmo.upper()}: {hash_resultado}")

def exemplo_hash_arquivo():
    """
    Demonstra como gerar hash de arquivos
    """
    print("\n=== Exemplo: Hash de Arquivo ===")
    
    # Cria um arquivo de exemplo
    arquivo_exemplo = "arquivo_teste.txt"
    conteudo = "Este é um arquivo de teste para demonstrar o gerador de hash.\nSegunda linha do arquivo."
    
    try:
        # Escreve o arquivo de exemplo
        with open(arquivo_exemplo, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        
        print(f"\nArquivo criado: {arquivo_exemplo}")
        print(f"Conteúdo: {repr(conteudo)}")
        
        # Gera hash do arquivo com diferentes algoritmos
        algoritmos = ['md5', 'sha1', 'sha256', 'sha512']
        
        for algoritmo in algoritmos:
            hash_resultado = gerar_hash_arquivo(arquivo_exemplo, algoritmo)
            print(f"  {algoritmo.upper()}: {hash_resultado}")
        
        # Remove o arquivo de exemplo
        os.remove(arquivo_exemplo)
        print(f"\nArquivo {arquivo_exemplo} removido.")
        
    except Exception as e:
        print(f"Erro: {str(e)}")

def comparar_hashes():
    """
    Demonstra como comparar hashes para verificar integridade
    """
    print("\n=== Exemplo: Comparação de Hashes ===")
    
    texto_original = "Dados importantes"
    texto_modificado = "Dados importantes!"
    
    hash_original = gerar_hash(texto_original, 'sha256')
    hash_modificado = gerar_hash(texto_modificado, 'sha256')
    
    print(f"Texto original: '{texto_original}'")
    print(f"Hash original: {hash_original}")
    
    print(f"\nTexto modificado: '{texto_modificado}'")
    print(f"Hash modificado: {hash_modificado}")
    
    if hash_original == hash_modificado:
        print("\n✅ Os textos são idênticos (hashes iguais)")
    else:
        print("\n❌ Os textos são diferentes (hashes diferentes)")
        print("Isso demonstra como pequenas mudanças resultam em hashes completamente diferentes.")

def exemplo_verificacao_integridade():
    """
    Demonstra um caso de uso prático: verificação de integridade
    """
    print("\n=== Exemplo: Verificação de Integridade ===")
    
    # Simula um arquivo importante
    arquivo = "documento_importante.txt"
    conteudo_original = "Contrato importante\nValor: R$ 10.000,00\nData: 2024-01-15"
    
    try:
        # Cria o arquivo
        with open(arquivo, 'w', encoding='utf-8') as f:
            f.write(conteudo_original)
        
        # Gera hash inicial (checksum)
        hash_inicial = gerar_hash_arquivo(arquivo, 'sha256')
        print(f"Arquivo criado: {arquivo}")
        print(f"Hash inicial (checksum): {hash_inicial}")
        
        # Simula verificação posterior
        print("\n--- Verificação de integridade ---")
        hash_atual = gerar_hash_arquivo(arquivo, 'sha256')
        
        if hash_inicial == hash_atual:
            print("✅ Arquivo íntegro - não foi modificado")
        else:
            print("❌ Arquivo foi modificado - possível corrupção ou alteração")
        
        # Simula modificação do arquivo
        print("\n--- Simulando modificação do arquivo ---")
        with open(arquivo, 'a', encoding='utf-8') as f:
            f.write("\nLinha adicionada")
        
        hash_modificado = gerar_hash_arquivo(arquivo, 'sha256')
        print(f"Hash após modificação: {hash_modificado}")
        
        if hash_inicial == hash_modificado:
            print("✅ Arquivo íntegro")
        else:
            print("❌ Arquivo foi modificado!")
        
        # Remove o arquivo
        os.remove(arquivo)
        
    except Exception as e:
        print(f"Erro: {str(e)}")

if __name__ == "__main__":
    print("EXEMPLOS DE USO DO GERADOR DE HASHCODE")
    print("=" * 50)
    
    exemplo_hash_texto()
    exemplo_hash_arquivo()
    comparar_hashes()
    exemplo_verificacao_integridade()
    
    print("\n" + "=" * 50)
    print("Exemplos concluídos!")
    print("\nPara usar o gerador interativo, execute: python gerador_hash.py")