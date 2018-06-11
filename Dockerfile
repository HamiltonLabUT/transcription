# Copyright 2016 Prifysgol Bangor University
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
FROM ubuntu:14.04
MAINTAINER Uned Technolegau Iaith, Prifysgol Bangor

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

ADD HTK-3.4.1.tar.gz /usr/local/src
ADD HTK-samples-3.4.1.tar.gz /usr/local/src/htk/

RUN dpkg --add-architecture i386
RUN apt-get update --fix-missing && apt-get upgrade -y

RUN apt-get install -q -y curl build-essential gcc-multilib libx11-dev:i386 \
	python python3 \
	perl wget zip unzip sox sqlite curl \
	zlib1g-dev libtool autotools-dev automake

RUN curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash \
	&& apt-get update && apt-get install -y git-lfs \
	&& apt-get clean \
	&& git lfs install \
 	&& rm -rf /var/lib/apt/lists/* 

# Install HTK
WORKDIR /usr/local/src/htk

RUN ./configure
RUN make all
RUN make install
