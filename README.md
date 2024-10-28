# YouTube Downloader by Evandro

Um projeto simples em Python para fazer download de vídeos e músicas diretamente do YouTube. Utiliza as bibliotecas `pytubefix` e `moviepy` para facilitar o processo de download e manipulação de arquivos de mídia.

## Pré-requisitos

Antes de começar, você precisa ter o Python instalado em sua máquina. Você pode baixa-lo neste link: https://www.python.org/downloads/

### Instalação das bibliotecas

Para instalar as bibliotecas necessárias, você pode usar o `pip`. Execute os seguintes comandos no terminal:

```bash
pip install pytubefix moviepy
```

## Criando um Executável
Se você quiser criar um executável para o seu código, pode usar a biblioteca PyInstaller. Isso permitirá que você utilize seu aplicativo sem precisar rodar o script em um editor de cógido ou terminal.

Instalação do PyInstaller
Para instalar o PyInstaller, execute o seguinte comando:

```bash
pip install pytubefix moviepy
```

## Criando o Executável
Para gerar o executável, navegue até o diretório do seu projeto no terminal e execute:

```bash
pyinstaller --onefile seu_script.py
```

Substitua seu_script.py pelo nome do seu arquivo Python. Após a execução do comando, o executável será criado na pasta dist.

## Como Usar
Ao iniciar o script ele pedira uma 'URL' do youtube, em seguida solicitará se o usuario deseja baixar apenas o Video(Pressione 'v' ) ou apenas o Audio(Pressione 'a).
Para finalizar ele mostra a opção de abrir o arquivo baixado ou encerrar o script.

