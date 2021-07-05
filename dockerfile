FROM python:3.9-alpine
ADD calc.py /cal/
ADD testing.py /cal/s
ADD requirments.txt /cal/

WORKDIR /cal/

RUN pip install -r requirments.txt 