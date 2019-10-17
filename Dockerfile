FROM python:3.6
ENV PYTHONUNBUFFERED 1

# create directory in which code will be present inside container
RUN mkdir /code
WORKDIR /code

# install requirements.txt
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy source code
COPY src/ .

CMD ["echo", "installed requirements and code copied, run app or custom python commands"]
