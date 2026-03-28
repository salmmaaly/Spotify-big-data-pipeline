FROM python:3.11-slim

WORKDIR /app/pipeline/

COPY . /app/pipeline/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --default-timeout=100 pandas numpy matplotlib seaborn scikit-learn scipy requests

ENV MPLBACKEND=Agg

CMD ["python", "ingest.py", "spotify_user_behavior_realistic_50000_rows.csv"]