FROM ubuntu:20.04
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
COPY ./requirements.txt ./requirements.txt
WORKDIR .
EXPOSE 5000
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
        python3 \
        python3-pip && \
        nano \
    apt-get clean
RUN pip install Flask
COPY main2.py .

CMD ['python3', './main2.py']
