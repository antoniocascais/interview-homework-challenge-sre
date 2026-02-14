FROM python:3-slim
WORKDIR /app
COPY server.py .
RUN useradd -r appuser
USER appuser
EXPOSE 8080
CMD ["python3", "server.py"]
