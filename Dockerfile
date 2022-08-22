# Базовый образ
FROM python:3.7-slim
ENV HOME /app
WORKDIR HOME
COPY requirements.txt .
RUN pip install --upgrade pip
RUN python3 -m pip install -r requirements.txt
COPY utils.py .
COPY configure.py .
COPY entrypoint.sh .
COPY . .

# Копирование миграций при наличии
#COPY migrations .
# Подмена зависимостей при наличии
#COPY docker_config.py default_config.py

CMD flask run -h 0.0.0.0 -p 80
#CMD ["sh", "entrypoint.sh"]
