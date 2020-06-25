FROM python:3.6.9

RUN pip install --upgrade pip \
    && pip3 install -U pytest

COPY . /usr/src/app
WORKDIR /usr/src/app

RUN ./bin/install

CMD ["python3", "/usr/src/app/mandelbrot-orbit-runner.py"]