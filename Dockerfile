#
# HTK (Hidden Markov Model Toolkit) Docker
# v3.4.1
# @author Loreto Parisi (loretoparisi at gmail dot com)
# v1.0.0
#
# Copyright (c) 2017 Loreto Parisi - https://github.com/loretoparisi/docker
#

FROM ubuntu:16.04

# working directory
ENV HOME /home/joyvan
WORKDIR $HOME

# packages list
RUN \
	apt-get update && apt-get install -y \
    libc6-dev-i386 \
    libx11-dev \
    gawk \
    python-dev \
    python-pip \
    curl \
    git

# pip
RUN pip install --upgrade pip

WORKDIR $HOME/htk/
RUN echo $HOME
RUN $HOME/htk/configure --disable-hslab --prefix=${HOME}/htk && \
    make all && \
    make install

CMD ["bash"]
