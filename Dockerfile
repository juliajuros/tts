FROM ubuntu:20.04
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

WORKDIR .
COPY requirements.txt .
#EXPOSE 5000
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update && apt-get upgrade -y && apt-get install -y \
        ffmpeg \
        espeak \
        nano \
        python3 \
        libespeak1 \
        python3-pip && \
    apt-get clean
RUN pip install -r requirements.txt
COPY main.py .

CMD ["python3", "./main.py"]
