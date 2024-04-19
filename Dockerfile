# Use a imagem oficial do Python
FROM python:3.9-slim

# Defina o diretório de trabalho como /app
WORKDIR /app

# Copie o script Python para dentro do contêiner
COPY Atividade02.py .

# Execute o script Python
CMD ["python", "Atividade02.py"]


