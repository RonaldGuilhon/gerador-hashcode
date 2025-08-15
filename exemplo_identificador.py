#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exemplo de uso do Identificador de Hash
Demonstra como usar a nova funcionalidade para identificar tipos de hash
"""

from gerador_hash import gerar_hash, identificar_tipo_hash

def demonstrar_identificador():
    """Demonstra o uso do identificador de hash"""
    print("=== DEMONSTRAÇÃO DO IDENTIFICADOR DE HASH ===")
    print()
    
    # Gera alguns hashes de exemplo
    texto_exemplo = "Hello, World!"
    
    print(f"Texto de exemplo: '{texto_exemplo}'")
    print()
    
    # Gera hashes com diferentes algoritmos
    algoritmos = ['md5', 'sha1', 'sha256', 'sha512']
    hashes_exemplo = {}
    
    for algoritmo in algoritmos:
        hash_resultado = gerar_hash(texto_exemplo, algoritmo)
        hashes_exemplo[algoritmo] = hash_resultado
        print(f"Hash {algoritmo.upper()}: {hash_resultado}")
    
    print("\n" + "="*60)
    print("IDENTIFICANDO OS HASHES GERADOS:")
    print("="*60)
    
    # Identifica cada hash
    for algoritmo, hash_valor in hashes_exemplo.items():
        print(f"\n--- Analisando hash {algoritmo.upper()} ---")
        resultado = identificar_tipo_hash(hash_valor)
        
        print(f"Hash: {hash_valor}")
        print(f"Tipo identificado: {resultado['tipo']}")
        print(f"Comprimento: {resultado['comprimento']} caracteres")
        print(f"Formato: {resultado['formato']}")
        print(f"Algoritmos possíveis: {', '.join(resultado['algoritmos_possiveis'])}")
        print(f"Descrição: {resultado['descricao']}")
    
    print("\n" + "="*60)
    print("TESTANDO HASHES INVÁLIDOS:")
    print("="*60)
    
    # Testa hashes inválidos
    hashes_invalidos = [
        "abc123xyz",  # Muito curto e caracteres inválidos
        "123456789012345678901234567890123456789012345678901234567890123g",  # Caractere inválido
        "",  # Vazio
        "Hello World!",  # Texto normal
    ]
    
    for i, hash_invalido in enumerate(hashes_invalidos, 1):
        print(f"\n--- Teste {i}: Hash inválido ---")
        resultado = identificar_tipo_hash(hash_invalido)
        
        print(f"Input: '{hash_invalido}'")
        print(f"Tipo identificado: {resultado['tipo']}")
        print(f"Comprimento: {resultado['comprimento']} caracteres")
        print(f"Formato: {resultado['formato']}")
        print(f"Descrição: {resultado['descricao']}")

if __name__ == "__main__":
    demonstrar_identificador()