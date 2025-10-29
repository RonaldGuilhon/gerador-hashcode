#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interface Gráfica para o Gerador de Hashcode
Uma interface moderna e intuitiva usando tkinter
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os
from gerador_hash import gerar_hash, gerar_hash_arquivo, identificar_tipo_hash

class GeradorHashGUI:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.create_widgets()
        
    def setup_window(self):
        """Configura a janela principal"""
        self.root.title("Gerador de Hashcode - Interface Gráfica")
        self.root.geometry("900x700")
        self.root.minsize(700, 600)
        
        # Centraliza a janela na tela
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (900 // 2)
        y = (self.root.winfo_screenheight() // 2) - (700 // 2)
        self.root.geometry(f"900x700+{x}+{y}")
        
        # Configura o estilo
        style = ttk.Style()
        style.theme_use('clam')
        
    def create_widgets(self):
        """Cria todos os widgets da interface"""
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configura o grid para ser responsivo
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        main_frame.columnconfigure(2, weight=1)
        
        # Título
        title_label = ttk.Label(main_frame, text="🔐 Gerador de Hashcode", 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Notebook para abas
        notebook = ttk.Notebook(main_frame)
        notebook.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        main_frame.rowconfigure(1, weight=2)
        
        # Aba 1: Hash de Texto
        self.create_text_tab(notebook)
        
        # Aba 2: Identificador de Hash
        self.create_hash_identifier_tab(notebook)
        
        # Aba 3: Comparar Hashes
        self.create_compare_tab(notebook)
        
        # Área de resultado
        result_frame = ttk.LabelFrame(main_frame, text="Resultado", padding="10")
        result_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        result_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=3)
        
        self.result_text = scrolledtext.ScrolledText(result_frame, height=12, wrap=tk.WORD)
        self.result_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        result_frame.rowconfigure(0, weight=1)
        
        # Botões de ação
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, columnspan=3, pady=(10, 0))
        
        ttk.Button(button_frame, text="Copiar Resultado", 
                  command=self.copiar_resultado).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(button_frame, text="Limpar", 
                  command=self.limpar_resultado).pack(side=tk.LEFT, padx=(0, 10))
        ttk.Button(button_frame, text="Salvar Resultado", 
                  command=self.salvar_resultado).pack(side=tk.LEFT)
        
    def create_text_tab(self, notebook):
        """Cria a aba para hash de texto"""
        text_frame = ttk.Frame(notebook, padding="10")
        notebook.add(text_frame, text="📝 Hash de Texto")
        
        # Label e entrada de texto
        ttk.Label(text_frame, text="Digite o texto:").grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        self.text_input = scrolledtext.ScrolledText(text_frame, height=6, wrap=tk.WORD)
        self.text_input.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        
        # Frame para algoritmo
        algo_frame = ttk.LabelFrame(text_frame, text="Algoritmo de Hash", padding="10")
        algo_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.algoritmo_var = tk.StringVar(value="sha256")
        algoritmos = [("MD5", "md5"), ("SHA1", "sha1"), ("SHA256", "sha256"), ("SHA512", "sha512")]
        
        for i, (nome, valor) in enumerate(algoritmos):
            ttk.Radiobutton(algo_frame, text=nome, variable=self.algoritmo_var, 
                           value=valor).grid(row=0, column=i, padx=10)
        
        # Botão para gerar hash
        ttk.Button(text_frame, text="Gerar Hash do Texto", 
                  command=self.gerar_hash_texto).grid(row=3, column=0, pady=10)
        
        # Configura o grid
        text_frame.columnconfigure(0, weight=1)
        text_frame.rowconfigure(1, weight=1)
        
    def create_hash_identifier_tab(self, notebook):
        """Cria a aba para identificar tipos de hash"""
        identifier_frame = ttk.Frame(notebook, padding="10")
        notebook.add(identifier_frame, text="🔍 Identificador de Hash")
        
        # Label e entrada de hash
        ttk.Label(identifier_frame, text="Cole o hash para identificar:").grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        self.hash_input = scrolledtext.ScrolledText(identifier_frame, height=4, wrap=tk.WORD)
        self.hash_input.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        
        # Botão para identificar hash
        ttk.Button(identifier_frame, text="Identificar Tipo de Hash", 
                  command=self.identificar_hash).grid(row=2, column=0, pady=10)
        
        # Frame para resultados da identificação
        result_id_frame = ttk.LabelFrame(identifier_frame, text="Informações do Hash", padding="10")
        result_id_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(10, 20))
        result_id_frame.columnconfigure(0, weight=1)
        result_id_frame.columnconfigure(1, weight=1)
        result_id_frame.rowconfigure(2, weight=1)
        
        # Coluna 1 - Informações básicas
        basic_frame = ttk.Frame(result_id_frame)
        basic_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(0, 10))
        
        ttk.Label(basic_frame, text="Tipo:", font=('Arial', 8, 'bold')).grid(row=0, column=0, sticky=tk.W, pady=1)
        self.tipo_label = ttk.Label(basic_frame, text="-", foreground="blue", font=('Arial', 8))
        self.tipo_label.grid(row=0, column=1, sticky=tk.W, pady=1, padx=(10, 0))
        
        ttk.Label(basic_frame, text="Comprimento:", font=('Arial', 8, 'bold')).grid(row=1, column=0, sticky=tk.W, pady=1)
        self.comprimento_label = ttk.Label(basic_frame, text="-", font=('Arial', 8))
        self.comprimento_label.grid(row=1, column=1, sticky=tk.W, pady=1, padx=(10, 0))
        
        ttk.Label(basic_frame, text="Formato:", font=('Arial', 8, 'bold')).grid(row=2, column=0, sticky=tk.W, pady=1)
        self.formato_label = ttk.Label(basic_frame, text="-", font=('Arial', 8))
        self.formato_label.grid(row=2, column=1, sticky=tk.W, pady=1, padx=(10, 0))
        
        # Coluna 2 - Informações detalhadas
        detail_frame = ttk.Frame(result_id_frame)
        detail_frame.grid(row=0, column=1, sticky=(tk.W, tk.E, tk.N, tk.S), padx=(10, 0))
        detail_frame.columnconfigure(1, weight=1)
        detail_frame.rowconfigure(1, weight=1)
        
        ttk.Label(detail_frame, text="Algoritmos Possíveis:", font=('Arial', 8, 'bold')).grid(row=0, column=0, sticky=tk.W, pady=1)
        self.algoritmos_label = ttk.Label(detail_frame, text="-", font=('Arial', 8))
        self.algoritmos_label.grid(row=0, column=1, sticky=tk.W, pady=1, padx=(10, 0))
        
        ttk.Label(detail_frame, text="Descrição:", font=('Arial', 8, 'bold')).grid(row=1, column=0, sticky=tk.NW, pady=1)
        self.descricao_label = ttk.Label(detail_frame, text="-", wraplength=300, justify=tk.LEFT, font=('Arial', 8))
        self.descricao_label.grid(row=1, column=1, sticky=(tk.W, tk.N), pady=1, padx=(10, 0))
        
        # Configura o grid
        identifier_frame.columnconfigure(0, weight=1)
        identifier_frame.rowconfigure(1, weight=1)
        identifier_frame.rowconfigure(3, weight=3)
        
    def create_compare_tab(self, notebook):
        """Cria a aba para comparar hashes"""
        compare_frame = ttk.Frame(notebook, padding="10")
        notebook.add(compare_frame, text="⚖️ Comparar Hashes")
        
        # Hash 1
        ttk.Label(compare_frame, text="Hash 1:").grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        self.hash1_entry = ttk.Entry(compare_frame, width=70)
        self.hash1_entry.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Hash 2
        ttk.Label(compare_frame, text="Hash 2:").grid(row=2, column=0, sticky=tk.W, pady=(0, 5))
        self.hash2_entry = ttk.Entry(compare_frame, width=70)
        self.hash2_entry.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        
        # Botão para comparar
        ttk.Button(compare_frame, text="Comparar Hashes", 
                  command=self.comparar_hashes).grid(row=4, column=0, pady=10)
        
        # Resultado da comparação
        self.compare_result_label = ttk.Label(compare_frame, text="", font=('Arial', 12, 'bold'))
        self.compare_result_label.grid(row=5, column=0, columnspan=2, pady=10)
        
        # Configura o grid
        compare_frame.columnconfigure(0, weight=1)
        
    def gerar_hash_texto(self):
        """Gera hash do texto inserido"""
        texto = self.text_input.get("1.0", tk.END).strip()
        
        if not texto:
            messagebox.showwarning("Aviso", "Por favor, digite um texto!")
            return
        
        algoritmo = self.algoritmo_var.get()
        hash_resultado = gerar_hash(texto, algoritmo)
        
        # Exibe o resultado
        resultado = f"\n=== HASH DE TEXTO ===\n"
        resultado += f"Texto: {texto[:100]}{'...' if len(texto) > 100 else ''}\n"
        resultado += f"Algoritmo: {algoritmo.upper()}\n"
        resultado += f"Hash: {hash_resultado}\n"
        resultado += f"Tamanho: {len(hash_resultado)} caracteres\n\n"
        
        self.adicionar_resultado(resultado)
        
    def identificar_hash(self):
        """Identifica o tipo de hash inserido pelo usuário"""
        hash_texto = self.hash_input.get("1.0", tk.END).strip()
        
        if not hash_texto:
            messagebox.showwarning("Aviso", "Por favor, cole um hash para identificar!")
            return
        
        try:
            # Identifica o tipo de hash
            resultado = identificar_tipo_hash(hash_texto)
            
            # Atualiza os labels com as informações
            self.tipo_label.config(text=resultado['tipo'])
            self.comprimento_label.config(text=f"{resultado['comprimento']} caracteres")
            self.formato_label.config(text=resultado['formato'])
            
            if resultado['algoritmos_possiveis']:
                algoritmos_str = ", ".join(resultado['algoritmos_possiveis'])
            else:
                algoritmos_str = "Nenhum"
            self.algoritmos_label.config(text=algoritmos_str)
            
            self.descricao_label.config(text=resultado['descricao'])
            
            # Define cor baseada no tipo
            if resultado['tipo'] == 'Inválido' or resultado['tipo'] == 'Erro':
                cor = "red"
            elif resultado['tipo'] == 'Desconhecido':
                cor = "orange"
            else:
                cor = "green"
            
            self.tipo_label.config(foreground=cor)
            
            # Adiciona resultado à área de resultado principal
            resultado_texto = f"\n=== IDENTIFICAÇÃO DE HASH ===\n"
            resultado_texto += f"Hash analisado: {hash_texto[:50]}{'...' if len(hash_texto) > 50 else ''}\n"
            resultado_texto += f"Tipo identificado: {resultado['tipo']}\n"
            resultado_texto += f"Comprimento: {resultado['comprimento']} caracteres\n"
            resultado_texto += f"Formato: {resultado['formato']}\n"
            resultado_texto += f"Algoritmos possíveis: {algoritmos_str}\n"
            resultado_texto += f"Descrição: {resultado['descricao']}\n\n"
            
            self.adicionar_resultado(resultado_texto)
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao identificar hash: {str(e)}")
            # Limpa os labels em caso de erro
            self.tipo_label.config(text="Erro", foreground="red")
            self.comprimento_label.config(text="-")
            self.formato_label.config(text="-")
            self.algoritmos_label.config(text="-")
            self.descricao_label.config(text="Erro na análise")
        

        
    def comparar_hashes(self):
        """Compara dois hashes"""
        hash1 = self.hash1_entry.get().strip()
        hash2 = self.hash2_entry.get().strip()
        
        if not hash1 or not hash2:
            messagebox.showwarning("Aviso", "Por favor, insira ambos os hashes!")
            return
        
        # Remove espaços e converte para minúsculas
        hash1 = hash1.replace(" ", "").lower()
        hash2 = hash2.replace(" ", "").lower()
        
        if hash1 == hash2:
            self.compare_result_label.config(text="✅ HASHES IDÊNTICOS", foreground="green")
            resultado = f"\n=== COMPARAÇÃO DE HASHES ===\n"
            resultado += f"Hash 1: {hash1}\n"
            resultado += f"Hash 2: {hash2}\n"
            resultado += f"Resultado: ✅ IDÊNTICOS - Os dados são iguais\n\n"
        else:
            self.compare_result_label.config(text="❌ HASHES DIFERENTES", foreground="red")
            resultado = f"\n=== COMPARAÇÃO DE HASHES ===\n"
            resultado += f"Hash 1: {hash1}\n"
            resultado += f"Hash 2: {hash2}\n"
            resultado += f"Resultado: ❌ DIFERENTES - Os dados foram modificados\n\n"
        
        self.adicionar_resultado(resultado)
        
    def adicionar_resultado(self, texto):
        """Adiciona texto à área de resultado"""
        self.result_text.insert(tk.END, texto)
        self.result_text.see(tk.END)
        
    def copiar_resultado(self):
        """Copia o resultado para a área de transferência"""
        try:
            resultado = self.result_text.get("1.0", tk.END).strip()
            if resultado:
                self.root.clipboard_clear()
                self.root.clipboard_append(resultado)
                messagebox.showinfo("Sucesso", "Resultado copiado para a área de transferência!")
            else:
                messagebox.showwarning("Aviso", "Nenhum resultado para copiar!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao copiar: {str(e)}")
        
    def limpar_resultado(self):
        """Limpa a área de resultado e todos os campos de entrada de todas as abas"""
        # Limpa a área de resultado
        self.result_text.delete("1.0", tk.END)
        
        # Limpa campos da aba "Hash de Texto"
        self.text_input.delete("1.0", tk.END)
        
        # Limpa campos da aba "Identificador de Hash"
        self.hash_input.delete("1.0", tk.END)
        self.tipo_label.config(text="-", foreground="black")
        self.comprimento_label.config(text="-")
        self.formato_label.config(text="-")
        self.algoritmos_label.config(text="-")
        self.descricao_label.config(text="-")
        
        # Limpa campos da aba "Comparar Hashes"
        self.hash1_entry.delete(0, tk.END)
        self.hash2_entry.delete(0, tk.END)
        self.compare_result_label.config(text="")
        
        # Reset do algoritmo para o padrão (SHA256)
        self.algoritmo_var.set("sha256")
        
    def salvar_resultado(self):
        """Salva o resultado em um arquivo"""
        resultado = self.result_text.get("1.0", tk.END).strip()
        
        if not resultado:
            messagebox.showwarning("Aviso", "Nenhum resultado para salvar!")
            return
        
        arquivo = filedialog.asksaveasfilename(
            title="Salvar resultado",
            defaultextension=".txt",
            filetypes=[("Arquivo de texto", "*.txt"), ("Todos os arquivos", "*.*")]
        )
        
        if arquivo:
            try:
                with open(arquivo, 'w', encoding='utf-8') as f:
                    f.write(resultado)
                messagebox.showinfo("Sucesso", f"Resultado salvo em: {arquivo}")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao salvar arquivo: {str(e)}")

def main():
    """Função principal"""
    root = tk.Tk()
    app = GeradorHashGUI(root)
    
    # Tenta definir o ícone da janela
    try:
        # Se houver um ícone disponível
        pass
    except:
        pass
    
    root.mainloop()

if __name__ == "__main__":
    main()