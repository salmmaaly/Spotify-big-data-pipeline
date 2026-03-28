FROM python:3.11-slim

# Set working directory
WORKDIR /app/pipeline/

# Copy all files (including dataset)
COPY . /app/pipeline/

# Install required libraries
RUN pip install --no-cache-dir pandas numpy matplotlib seaborn scikit-learn scipy requests

# Prevent plotting issues inside Docker
ENV MPLBACKEND=Agg

# Run the full pipeline automatically
CMD ["python", "ingest.py", "spotify_user_behavior_realistic_50000_rows.csv"]