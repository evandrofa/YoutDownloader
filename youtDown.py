
from pytubefix import YouTube
import time
import sys
import os
from moviepy.editor import AudioFileClip

def show_progress(downloaded, total):
    percentage = downloaded / total * 100
    bar_length = 50
    block = int(bar_length * percentage / 100)
    progress_bar = f"\r[{'#' * block}{'-' * (bar_length - block)}] {percentage:.2f}%"
    sys.stdout.write(progress_bar)
    sys.stdout.flush()

def main():
    yt = YouTube(input('Cole a URL do vídeo aqui: '))

    print(f'Título: {yt.title}')
    print(f'Thumbnail: {yt.thumbnail_url}')

    # Perguntar ao usuário se deseja baixar apenas o áudio ou o vídeo
    download_type = input("Deseja baixar apenas o áudio (a) ou o vídeo (v)? ").strip().lower()

    if download_type == 'a':
        stream = yt.streams.filter(only_audio=True).first()
        output_path = 'Musicas'  
    else:
        stream = yt.streams.get_highest_resolution()  
        output_path = 'Videos' 

    # Cria a pasta se não existir
    os.makedirs(output_path, exist_ok=True)

    total_size = stream.filesize

    # Baixar o vídeo ou áudio
    print('Iniciando o download...')
    file_path = stream.download(output_path=output_path, filename=stream.default_filename)

    # Simulação de progresso
    for i in range(0, total_size + 1, total_size // 100):
        show_progress(i, total_size)
        time.sleep(0.1)

    # Se for áudio, converter para MP3
    if download_type == 'a':
        mp3_file_path = os.path.splitext(file_path)[0] + '.mp3'
        audio_clip = AudioFileClip(file_path)
        audio_clip.write_audiofile(mp3_file_path)
        audio_clip.close()
        os.remove(file_path)  # Remove o arquivo original
        file_path = mp3_file_path  # Atualiza o caminho do arquivo para o MP3

    # Perguntar se quer abrir o arquivo após o download
    def play_movie(path):
        from os import startfile
        startfile(path)

    class Media:
        def __init__(self, path):
            self.path = path

        def play(self):
            try:
                from os import startfile
                startfile(self.path)
            except Exception as e:
                print(f"Erro ao tentar abrir o arquivo: {e}")

    # Criação do objeto Media com o nome correto
    media = Media(file_path)
    if input("Aperte 'ENTER' para reproduzir o arquivo, ou qualquer outra tecla para sair!") == '':
        media.play()

    print('\nDownload concluído! Use sem moderação!!')

if __name__ == "__main__":
    main()