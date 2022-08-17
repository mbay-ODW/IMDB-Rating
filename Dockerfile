FROM python:3.11-slim

COPY server.py /
COPY templates/* templates/
COPy requirements.txt requirements.txt
RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["server.py"]