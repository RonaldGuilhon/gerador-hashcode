#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Interface Gráfica para o Gerador de Hashcode
Uma interface moderna e intuitiva usando tkinter
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import os
from gerador_hash import gerar_hash, gerar_hash_arquivo

class GeradorHashGUI:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.create_widgets()
        
    def setup_window(self):
        """Configura a janela principal"""
        self.root.title("Gerador de Hashcode - Interface Gráfica")
        self.root.geometry("800x600")
        self.root.minsize(600, 500)
        
        # Centraliza a janela na tela
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() // 2) - (800 // 2)
        y = (self.root.winfo_screenheight() // 2) - (600 // 2)
        self.root.geometry(f"800x600+{x}+{y}")
        
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
        main_frame.columnconfigure(1, weight=1)
        
        # Título
        title_label = ttk.Label(main_frame, text="🔐 Gerador de Hashcode", 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Notebook para abas
        notebook = ttk.Notebook(main_frame)
        notebook.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        main_frame.rowconfigure(1, weight=1)
        
        # Aba 1: Hash de Texto
        self.create_text_tab(notebook)
        
        # Aba 2: Hash de Arquivo
        self.create_file_tab(notebook)
        
        # Aba 3: Comparar Hashes
        self.create_compare_tab(notebook)
        
        # Frame para algoritmo (comum a todas as abas)
        algo_frame = ttk.LabelFrame(main_frame, text="Algoritmo de Hash", padding="10")
        algo_frame.grid(row=2, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        
        self.algoritmo_var = tk.StringVar(value="sha256")
        algoritmos = [("MD5", "md5"), ("SHA1", "sha1"), ("SHA256", "sha256"), ("SHA512", "sha512")]
        
        for i, (nome, valor) in enumerate(algoritmos):
            ttk.Radiobutton(algo_frame, text=nome, variable=self.algoritmo_var, 
                           value=valor).grid(row=0, column=i, padx=10)
        
        # Área de resultado
        result_frame = ttk.LabelFrame(main_frame, text="Resultado", padding="10")
        result_frame.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        result_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(3, weight=1)
        
        self.result_text = scrolledtext.ScrolledText(result_frame, height=8, wrap=tk.WORD)
        self.result_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        result_frame.rowconfigure(0, weight=1)
        
        # Botões de ação
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=4, column=0, columnspan=3, pady=(10, 0))
        
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
        
        # Botão para gerar hash
        ttk.Button(text_frame, text="Gerar Hash do Texto", 
                  command=self.gerar_hash_texto).grid(row=2, column=0, pady=10)
        
        # Configura o grid
        text_frame.columnconfigure(0, weight=1)
        text_frame.rowconfigure(1, weight=1)
        
    def create_file_tab(self, notebook):
        """Cria a aba para hash de arquivo"""
        file_frame = ttk.Frame(notebook, padding="10")
        notebook.add(file_frame, text="📁 Hash de Arquivo")
        
        # Seleção de arquivo
        ttk.Label(file_frame, text="Selecione um arquivo:").grid(row=0, column=0, sticky=tk.W, pady=(0, 5))
        
        file_select_frame = ttk.Frame(file_frame)
        file_select_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 10))
        file_select_frame.columnconfigure(0, weight=1)
        
        self.file_path_var = tk.StringVar()
        self.file_entry = ttk.Entry(file_select_frame, textvariable=self.file_path_var, state="readonly")
        self.file_entry.grid(row=0, column=0, sticky=(tk.W, tk.E), padx=(0, 10))
        
        ttk.Button(file_select_frame, text="Procurar...", 
                  command=self.selecionar_arquivo).grid(row=0, column=1)
        
        # Informações do arquivo
        self.file_info_label = ttk.Label(file_frame, text="Nenhum arquivo selecionado", 
                                        foreground="gray")
        self.file_info_label.grid(row=2, column=0, columnspan=2, sticky=tk.W, pady=(0, 10))
        
        # Botão para gerar hash
        ttk.Button(file_frame, text="Gerar Hash do Arquivo", 
                  command=self.gerar_hash_arquivo_gui).grid(row=3, column=0, pady=10)
        
        # Configura o grid
        file_frame.columnconfigure(0, weight=1)
        
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
        resultado = f"=== HASH DE TEXTO ===\n"
        resultado += f"Texto: {texto[:100]}{'...' if len(texto) > 100 else ''}\n"
        resultado += f"Algoritmo: {algoritmo.upper()}\n"
        resultado += f"Hash: {hash_resultado}\n"
        resultado += f"Tamanho: {len(hash_resultado)} caracteres\n\n"
        
        self.adicionar_resultado(resultado)
        
    def selecionar_arquivo(self):
        """Abre diálogo para selecionar arquivo"""
        arquivo = filedialog.askopenfilename(
            title="Selecionar arquivo",
            filetypes=[("Todos os arquivos", "*.*")]
        )
        
        if arquivo:
            self.file_path_var.set(arquivo)
            
            # Mostra informações do arquivo
            try:
                tamanho = os.path.getsize(arquivo)
                tamanho_mb = tamanho / (1024 * 1024)
                
                if tamanho_mb < 1:
                    tamanho_str = f"{tamanho / 1024:.1f} KB"
                else:
                    tamanho_str = f"{tamanho_mb:.1f} MB"
                
                nome_arquivo = os.path.basename(arquivo)
                info = f"Arquivo: {nome_arquivo} | Tamanho: {tamanho_str}"
                self.file_info_label.config(text=info, foreground="black")
                
            except Exception as e:
                self.file_info_label.config(text=f"Erro ao ler arquivo: {str(e)}", 
                                          foreground="red")
        
    def gerar_hash_arquivo_gui(self):
        """Gera hash do arquivo selecionado"""
        arquivo = self.file_path_var.get()
        
        if not arquivo:
            messagebox.showwarning("Aviso", "Por favor, selecione um arquivo!")
            return
        
        if not os.path.exists(arquivo):
            messagebox.showerror("Erro", "Arquivo não encontrado!")
            return
        
        algoritmo = self.algoritmo_var.get()
        
        # Mostra progresso para arquivos grandes
        try:
            tamanho = os.path.getsize(arquivo)
            if tamanho > 10 * 1024 * 1024:  # > 10MB
                messagebox.showinfo("Processando", "Arquivo grande detectado. O processamento pode demorar...")
            
            hash_resultado = gerar_hash_arquivo(arquivo, algoritmo)
            
            # Exibe o resultado
            nome_arquivo = os.path.basename(arquivo)
            tamanho_mb = tamanho / (1024 * 1024)
            
            resultado = f"=== HASH DE ARQUIVO ===\n"
            resultado += f"Arquivo: {nome_arquivo}\n"
            resultado += f"Caminho: {arquivo}\n"
            resultado += f"Tamanho: {tamanho_mb:.2f} MB\n"
            resultado += f"Algoritmo: {algoritmo.upper()}\n"
            resultado += f"Hash: {hash_resultado}\n\n"
            
            self.adicionar_resultado(resultado)
            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao processar arquivo: {str(e)}")
        
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
            resultado = f"=== COMPARAÇÃO DE HASHES ===\n"
            resultado += f"Hash 1: {hash1}\n"
            resultado += f"Hash 2: {hash2}\n"
            resultado += f"Resultado: ✅ IDÊNTICOS - Os dados são iguais\n\n"
        else:
            self.compare_result_label.config(text="❌ HASHES DIFERENTES", foreground="red")
            resultado = f"=== COMPARAÇÃO DE HASHES ===\n"
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
        """Limpa a área de resultado"""
        self.result_text.delete("1.0", tk.END)
        self.compare_result_label.config(text="")
        
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