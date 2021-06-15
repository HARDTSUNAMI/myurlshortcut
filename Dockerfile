FROM python:3
WORKDIR /firstsite
ENV pythondontwritebytecode 1
ENV pythonunbuffered 1
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY ./wait-for-it.sh /bin/wait-for-it.sh
RUN chmod +x /bin/wait-for-it.sh





