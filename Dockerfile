from ubuntu:18.04
MAINTAINER cagojeiger@naver.com

ENV LC_ALL C.UTF-8

RUN apt-get update -y
RUN apt-get install git \
                    vim -y

RUN apt-get install python3-pip -y
RUN pip3 install sanic plotly pandas

RUN git clone https://github.com/kangheeyong/PROJECT-SPDRC-ui.git /root/PROJECT-SPDRC-ui


EXPOSE 8070
WORKDIR /root/PROJECT-SPDRC-ui
CMD ["make", "run"]


