# !! require build !!
# docker build -t ubuntu1604py36

# Base image
FROM ubuntu:16.04

# Env setting
ARG proj_dir=/app/service/

# App files copy
ADD service.py $proj_dir

# Update
RUN apt-get update
RUN apt-get install -y software-properties-common vim
RUN add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update

# Install packages
RUN apt-get install -y build-essential python3.6 python3.6-dev python3-pip python3.6-venv
RUN apt-get install -y git vim

# Update pip
RUN python3.6 -m pip install pip --upgrade
RUN python3.6 -m pip install wheel

# Install packages written in the retuirements.txt
WORKDIR $proj_dir
RUN pip install flask
