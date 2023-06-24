FROM python:latest

WORKDIR /var/www/app

COPY . /var/www/app/

RUN pip install --no-cache-dir -r requirements.txt

ENV PATH="${PATH}:/home/${USER}/.local/bin"

CMD echo "Application successful up"
