# YouTube to MP3 Downloader 🎵

Um script em Python simples e eficiente para baixar o áudio de vídeos do YouTube e convertê-los automaticamente para o formato MP3 com alta qualidade.

## Funcionalidades

- Baixa apenas o áudio (economiza dados e tempo).
- Conversão automática para `.mp3` via FFmpeg.
- Nomeia o arquivo automaticamente com o título do vídeo.
- Compatível com as atualizações mais recentes do YouTube (via `yt-dlp`).

## Pré-requisitos

Antes de começar, você precisará ter instalado em sua máquina:

1.  **Python 3.x**
2.  **FFmpeg**: Essencial para a conversão de áudio.
    - *Dica:* Certifique-se de que o FFmpeg esteja no seu PATH do sistema.
3.  **Node.js** (Opcional, mas recomendado): Ajuda o script a lidar com as proteções de JavaScript do YouTube.

## 📦 Instalação

1. Clone o repositório:
   ```bash
   git clone [https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git](https://github.com/SEU_USUARIO/NOME_DO_REPOSITORIO.git)

2. Entre na pasta do projeto:
  cd NOME_DO_REPOSITORIO

3. Instale a biblioteca necessária:
  pip install yt-dlp

4. Rode normalmente:
  python baixar_musica.py
