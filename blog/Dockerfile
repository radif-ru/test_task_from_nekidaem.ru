FROM python:3.9

RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean

WORKDIR /usr/src/app

RUN chmod ugo+x entrypoint.sh

COPY requirements.txt .
COPY entrypoint.sh .

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
