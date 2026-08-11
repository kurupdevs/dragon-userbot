FROM python:3.11-slim AS builder
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

FROM python:3.11-slim
RUN groupadd -r botuser && useradd -r -g botuser botuser
WORKDIR /app
COPY --from=builder /root/.local /home/botuser/.local
COPY --chown=botuser:botuser . .
ENV PATH=/home/botuser/.local/bin:$PATH
USER botuser
HEALTHCHECK --interval=30s --timeout=10s --retries=3 CMD python -c "import sys; sys.exit(0)"
CMD ["python", "main.py"]
