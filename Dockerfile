FROM python:3.10

WORKDIR /

RUN mkdir -p /botEndpoint
RUN apt-get update
RUN apt-get install -y vim
COPY ./botEndpoint /botEndpoint
COPY ./Pipfile /Pipfile
COPY ./Pipfile.lock /Pipfile.lock
COPY ./config.py /config.py
COPY ./db.py /db.py
COPY ./main.py /main.py
COPY ./model.py /model.py

# Install dependencies
RUN pip3 install --upgrade pip
RUN pip3 install pipenv
RUN pipenv --python 3.10
RUN pipenv install

CMD ["pipenv", "run", "python3", "main.py"]
