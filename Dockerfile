FROM python:3.9

WORKDIR /fin_parsing

RUN git clone https://github.com/IvanPozd/fin_parsing.git

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "master.py"]