#git clone https://github.com/jlalus/phonemizer-docker
cd ~
git clone https://github.com/bootphon/phonemizer

cp phonemizer-docker/Dockerfile phonemizer/Dockerfile
cp phonemizer-docker/app.py phonemizer/app.py

cd phonemizer

sudo docker build -t phonemizer .
sudo docker run --name PhonemizerApp --expose 5000 phonemizer

