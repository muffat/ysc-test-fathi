#!/bin/bash

sudo docker build -t yousician .
sudo docker run -it --rm -p 5000:5000 yousician