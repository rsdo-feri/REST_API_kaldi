#first you need to build a Docker image

docker build -t kaldi-asr .

#now you can run Docker container

docker run -d --name kaldi-asr -p 5000:5000 server_kaldi
