FROM ubuntu:20.04
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8
COPY requirements.txt .
WORKDIR .
#EXPOSE 5000
RUN DEBIAN_FRONTEND=noninteractive TZ=Etc/UTC apt-get -y install tzdata
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
        ffmpeg \
        bitstring \
        espeak \
        nano \
        python3 \
        python3-pip && \
    apt-get clean
RUN pip install -r requirements.txt
COPY main.py .

CMD ['python3', './main.py']
