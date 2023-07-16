FROM python:3.11-alpine
RUN apk add curl

WORKDIR /api

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 CMD curl --fail http://localhost:6000/ || exit 1

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "6000"]
EXPOSE 6000