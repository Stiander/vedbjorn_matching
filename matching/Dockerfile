FROM python:3.6
ENV PYTHONUNBUFFERED 1
RUN mkdir -p /home/matching/
COPY ./requirements.txt /home/matching/
RUN pip install -r /home/matching/requirements.txt
COPY ./src/ /home/matching/
WORKDIR /home/matching
CMD python3 main.py
