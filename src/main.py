import tkinter as tk
from menubar import Menu_bar

# Função para criar uma seção de cântico
def create_cantico_section(parent, title):
    section_frame = tk.Frame(parent)
    section_frame.pack(fill=tk.BOTH, padx=10, pady=5)

    label = tk.Label(section_frame, text=title)
    label.pack(side=tk.TOP, pady=5)

    entry = tk.Entry(section_frame, width=3)  # Ajustando o tamanho para 3 caracteres
    entry.pack(side=tk.LEFT, padx=5)

    button = tk.Button(section_frame, text="Tocar", command=lambda: play_cantico(title))
    button.pack(side=tk.LEFT)

# Função para tocar o cântico
def play_cantico(cantico):
    print(f"Tocando {cantico}")

# Criar a janela principal
root = tk.Tk()
root.title("Player de Cânticos")

# Criar barra de menu
menubar = tk.Menu(root)

# Opção "Arquivo"
file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Abrir Arquivo", command=Menu_bar.open_file)
menubar.add_cascade(label="Arquivo", menu=file_menu)

# Opção "Configurações"
settings_menu = tk.Menu(menubar, tearoff=0)
settings_menu.add_command(label="Abrir Configurações", command=Menu_bar.open_settings)
settings_menu.add_command(label="Fixar no Topo", command=Menu_bar.open_fix_on_top)
menubar.add_cascade(label="Configurações", menu=settings_menu)

# Opção "Ajuda"
help_menu = tk.Menu(menubar, tearoff=0)
help_menu.add_command(label="Abrir Ajuda", command=Menu_bar.open_help)
menubar.add_cascade(label="Ajuda", menu=help_menu)

# Associar barra de menu à janela
root.config(menu=menubar)

# Criar seções de cânticos
create_cantico_section(root, "Cântico Inicial")
create_cantico_section(root, "Cântico do Meio")
create_cantico_section(root, "Cântico Final")

# Iniciar loop principal da aplicação
root.mainloop()
