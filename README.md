## REST API KALDI

First Build Docker image:

``` docker build -t kaldi-asr .```

Run Docker container:

``` docker run -d --name kaldi-asr -p 5000:5000 server_kaldi```
