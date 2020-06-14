FROM python:3.6.9

RUN pip install --upgrade pip \
    && pip3 install Pillow \
    && pip3 install -U pytest matplotlib numpy mpmath

COPY . /usr/src/app
WORKDIR /usr/src/app

CMD ["python3", "/usr/src/app/mandelbrot-orbit.py"]