# Базовый образ
FROM python:3.10-slim
ENV HOME /app
WORKDIR HOME
COPY requirements_old1.txt .
COPY utils.py .
COPY configure.py .
COPY entrypoint.sh .
RUN python3 -m pip install -r requirements_old1.txt
COPY app.py .

# Копирование миграций при наличии
#COPY migrations .
# Подмена зависимостей при наличии
#COPY docker_config.py default_config.py

#CMD flask run -h 0.0.0.0 -p 80
CMD ["sh", "entrypoint.sh"]
