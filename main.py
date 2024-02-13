import tkinter as tk
from tkinter import filedialog
import os
import platform
import subprocess

class ConfiguracoesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Configurações")

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=20, pady=20)

        # Título
        self.label_titulo = tk.Label(self.frame, text="Configurações")
        self.label_titulo.config(font=("Arial", 16))
        self.label_titulo.grid(row=0, column=0, columnspan=3)

        # Entrada de número para tocar
        self.label_numero = tk.Label(self.frame, text="Número:")
        self.label_numero.grid(row=1, column=0, sticky="e")

        self.entry_numero = tk.Entry(self.frame, width=10)
        self.entry_numero.grid(row=1, column=1)

        # Botão para tocar
        self.button_tocar = tk.Button(self.frame, text="Tocar", command=self.tocar_audio_video)
        self.button_tocar.grid(row=1, column=2)

        # Entrada de caminho para vídeos
        self.label_videos = tk.Label(self.frame, text="Caminho dos Vídeos:")
        self.label_videos.grid(row=2, column=0, sticky="e")

        self.entry_videos = tk.Entry(self.frame, width=50)
        self.entry_videos.grid(row=2, column=1)

        self.button_videos = tk.Button(self.frame, text="Selecionar", command=self.selecionar_video)
        self.button_videos.grid(row=2, column=2)

        # Entrada de caminho para áudios
        self.label_audios = tk.Label(self.frame, text="Caminho dos Áudios:")
        self.label_audios.grid(row=3, column=0, sticky="e")

        self.entry_audios = tk.Entry(self.frame, width=50)
        self.entry_audios.grid(row=3, column=1)

        self.button_audios = tk.Button(self.frame, text="Selecionar", command=self.selecionar_audio)
        self.button_audios.grid(row=3, column=2)

        # Botão para salvar configurações
        self.button_salvar = tk.Button(self.frame, text="Salvar", command=self.salvar_configuracoes)
        self.button_salvar.grid(row=4, column=0, columnspan=3, pady=10)

    def selecionar_video(self):
        video_path = filedialog.askdirectory()
        self.entry_videos.delete(0, tk.END)
        self.entry_videos.insert(0, video_path)

    def selecionar_audio(self):
        audio_path = filedialog.askdirectory()
        self.entry_audios.delete(0, tk.END)
        self.entry_audios.insert(0, audio_path)

    def salvar_configuracoes(self):
        video_path = self.entry_videos.get()
        audio_path = self.entry_audios.get()
        # Aqui você pode implementar a lógica para salvar os caminhos em um arquivo de configuração
        print("Caminho dos vídeos:", video_path)
        print("Caminho dos áudios:", audio_path)
        # Exemplo: salvar em um arquivo de texto
        with open("config.txt", "w") as f:
            f.write(f"video_path={video_path}\n")
            f.write(f"audio_path={audio_path}")

    def tocar_audio_video(self):
        numero = self.entry_numero.get()
        video_path = self.entry_videos.get()
        audio_path = self.entry_audios.get()

        # Verificar se os campos estão vazios
        if not numero or not video_path or not audio_path:
            print("Por favor, preencha todos os campos.")
            return

        # Formar os caminhos completos para o vídeo e áudio
        video_file = os.path.join(video_path, f"sjj_LSB_{numero}_r720P.mp4")
        audio_file = os.path.join(audio_path, f"sjjm_T_{numero}.mp3")

        # Verificar se os arquivos existem
        if not os.path.exists(video_file) or not os.path.exists(audio_file):
            print("Arquivos de áudio ou vídeo não encontrados.")
            return

        # Tocar o vídeo e o áudio
        if platform.system() == "Windows":
            subprocess.Popen(['start', video_file], shell=True)
            subprocess.Popen(['start', audio_file], shell=True)
        elif platform.system() == "Darwin":  # Mac
            subprocess.Popen(['open', video_file])
            subprocess.Popen(['open', audio_file])
        else:  # Linux
            subprocess.Popen(['xdg-open', video_file])
            subprocess.Popen(['xdg-open', audio_file])

def main():
    root = tk.Tk()
    app = ConfiguracoesApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
