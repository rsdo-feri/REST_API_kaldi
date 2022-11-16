## REST API KALDI

First build Docker image:

``` docker build -t kaldi-asr .```

Run Docker container:

``` docker run -d --name kaldi-asr-server -p 5000:5000 kaldi-asr```
