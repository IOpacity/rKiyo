FROM python:3.12-rc-slim-buster

ENV TZ=Asia/Kolkata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

WORKDIR /app

RUN apt update -y 
RUN apt-get -y install gcc
COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .

RUN apt autoremove -y 

CMD [ "python3", "-m" , "Main"]
