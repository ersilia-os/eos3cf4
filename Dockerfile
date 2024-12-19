FROM bentoml/model-server:0.11.0-py310
MAINTAINER ersilia

RUN pip install molfeat[transformer]==0.10.0

WORKDIR /repo
COPY . /repo
