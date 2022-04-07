FROM python:3.8

COPY requirements.txt /

RUN pip install -r requirements.txt

RUN python -m spacy download en_core_web_sm

COPY Docker/fil_rouge.py fil_rouge.py

CMD [ "python", "./fil_rouge.py" ]