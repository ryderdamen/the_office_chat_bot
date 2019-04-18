FROM python:3.7
RUN mkdir /code
WORKDIR /code
ADD ./app/requirements.txt .
RUN pip install -r requirements.txt
ADD ./app .
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
