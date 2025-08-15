# Gerador de Hashcode

Um gerador de hashcode completo e moderno em Python que permite gerar hashes de textos e arquivos usando diferentes algoritmos criptográficos. Aplicação **desktop local** com interface gráfica moderna!

## 🚀 Funcionalidades

- ✅ Gerar hash de textos
- ✅ Gerar hash de arquivos
- ✅ Comparar hashes para verificação de integridade
- ✅ Suporte a múltiplos algoritmos: MD5, SHA1, SHA256, SHA512
- ✅ **2 interfaces disponíveis**: Linha de comando e Interface gráfica (GUI)
- ✅ Processamento eficiente de arquivos grandes
- ✅ Interface moderna e responsiva
- ✅ Uso programático (API)

## 🎯 Como usar

### 1. Interface Gráfica (GUI) - Recomendada

```bash
python interface_grafica.py
```

### 2. Interface de Linha de Comando (CLI)

```bash
python gerador_hash.py
```

### Menu principal

O programa apresenta um menu com as seguintes opções:

1. **Gerar hash de texto** - Digite um texto e escolha o algoritmo
2. **Gerar hash de arquivo** - Informe o caminho do arquivo e escolha o algoritmo
3. **Sair** - Encerra o programa

### Algoritmos suportados

- **MD5** - Rápido, mas não recomendado para segurança
- **SHA1** - Mais seguro que MD5, mas ainda vulnerável
- **SHA256** - Recomendado para a maioria dos casos (padrão)
- **SHA512** - Máxima segurança, hash mais longo

## Exemplos de uso

### Exemplo 1: Hash de texto
```
=== GERADOR DE HASHCODE ===
1. Gerar hash de texto
2. Gerar hash de arquivo
3. Sair

Escolha uma opção (1-3): 1

--- Gerar Hash de Texto ---
Digite o texto: Hello World

Algoritmos disponíveis:
1. MD5
2. SHA1
3. SHA256 (padrão)
4. SHA512

Escolha o algoritmo (1-4, Enter para SHA256): 3

Texto: Hello World
Algoritmo: SHA256
Hash: a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e
```

### Exemplo 2: Hash de arquivo
```
Escolha uma opção (1-3): 2

--- Gerar Hash de Arquivo ---
Digite o caminho do arquivo: C:\exemplo\arquivo.txt

Algoritmos disponíveis:
1. MD5
2. SHA1
3. SHA256 (padrão)
4. SHA512

Escolha o algoritmo (1-4, Enter para SHA256): 1

Processando arquivo 'C:\exemplo\arquivo.txt'...

Arquivo: C:\exemplo\arquivo.txt
Algoritmo: MD5
Hash: 5d41402abc4b2a76b9719d911017c592
```

## Uso programático

Você também pode importar as funções e usar diretamente no seu código:

```python
from gerador_hash import gerar_hash, gerar_hash_arquivo

# Gerar hash de texto
hash_texto = gerar_hash("Meu texto", "sha256")
print(hash_texto)

# Gerar hash de arquivo
hash_arquivo = gerar_hash_arquivo("caminho/para/arquivo.txt", "md5")
print(hash_arquivo)
```

## Requisitos

- Python 3.6 ou superior
- Biblioteca `hashlib` (incluída no Python padrão)
- Biblioteca `os` (incluída no Python padrão)

## Casos de uso

- **Verificação de integridade** - Verificar se arquivos não foram corrompidos
- **Comparação de arquivos** - Identificar arquivos duplicados
- **Segurança** - Gerar checksums para validação
- **Desenvolvimento** - Verificar mudanças em arquivos

## Notas de segurança

- **MD5** e **SHA1** são considerados criptograficamente quebrados para uso em segurança
- Use **SHA256** ou **SHA512** para aplicações que requerem segurança
- Este programa é adequado para verificação de integridade e propósitos gerais

## Licença

Este projeto é de domínio público. Use livremente!