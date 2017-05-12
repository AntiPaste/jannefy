FROM    python:alpine

ENV     HOME=/app
ENV     PYTHONPATH=${HOME}
ENV     PYTHONUNBUFFERED=true
ENV     LIBRARY_PATH=/lib:/usr/lib

WORKDIR ${HOME}

COPY    ./jannefy/requirements.txt ${HOME}/jannefy/

RUN     pip3 install -r ${HOME}/jannefy/requirements.txt

COPY    ./jannefy/ ${HOME}/jannefy/

CMD     ["python3", "-m", "jannefy"]
