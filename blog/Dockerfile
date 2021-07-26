FROM python:3.9

# устанавливаем переменные окружения
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# устанавливаем рабочий каталог
WORKDIR /home/app/web

RUN pip install --upgrade pip

# устанавливаем зависимости для psycopg2 (необходимо только при python:-alpine)
#RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt .
RUN pip install -r requirements.txt

# разрешение на запуск файла
COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

# копируем проект
COPY . .


# запуск entrypoint.sh
ENTRYPOINT ["/home/app/web/entrypoint.sh"]
