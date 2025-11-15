FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y git && apt-get clean && apt-get install -y nut-client

RUN git clone https://github.com/Vitapostigo/fast_ups_api.git .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 18000

CMD ["python3", "cod.py"]
