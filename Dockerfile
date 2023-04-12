FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN pip install rdkit
RUN pip install molfeat
RUN pip install transformers

WORKDIR /repo
COPY . /repo
