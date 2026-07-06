FROM python:3.12-slim
WORKDIR /app_root
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY app/ app/
ENTRYPOINT ["python", "-u", "-m"]
CMD ["app.primera_carga"]
