FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/blog

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /usr/src/blog
RUN chmod +x /usr/src/blog/entrypoint.sh

ENTRYPOINT ["/usr/src/blog/entrypoint.sh"]

