FROM python:3

ENV HOME /Users/anastasiiamonakhova/.jenkins/workspace/opencart-tests

RUN apt update
RUN apt install -y libnss3

RUN apt-get install -y wget
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb
RUN echo "Chrome: " && google-chrome --version