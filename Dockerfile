FROM python:3

ENV HOME /Users/anastasiiamonakhova/.jenkins/workspace/opencart-tests

RUN apt update
RUN apt install -y libnss3