# 🎧 Spotify Big Data Analytics Pipeline

## 👨‍💻 Team Members

* Salma Zakaria

---

## 📌 Project Description

This project implements a **Dockerized end-to-end data pipeline** for analyzing Spotify user behavior.
The pipeline performs data ingestion, preprocessing, analytics, visualization, and clustering automatically.

---

## 🐳 Docker Instructions

### 🔨 Build Docker Image

```bash
docker build -t spotify-big-data-pipeline .
```

### ▶️ Run Container

```bash
docker run --name spotify_pipeline spotify-big-data-pipeline
```

---

## ⚙️ Pipeline Execution Flow

The pipeline runs automatically inside Docker:

```
Ingest → Preprocess → Analytics → Visualization → Clustering
```

---

## 📊 Features Implemented

### 1️⃣ Data Ingestion

* Loads dataset from CSV
* Saves raw data as `data_raw.csv`

### 2️⃣ Data Preprocessing

* Handles missing values
* Removes duplicates
* Encodes categorical variables
* Scales numerical features
* Applies PCA (dimensionality reduction)
* Creates engagement levels (low / medium / high)

### 3️⃣ Analytics

* Generates insights about user engagement
* Saves results into `.txt` files

### 4️⃣ Visualization

* Histogram (engagement distribution)
* Correlation heatmap
* Scatter plot (PC1 vs PC2)

### 5️⃣ Clustering

* Applies K-Means clustering
* Outputs cluster distribution

---

## 📁 Output Files

* `data_preprocessed.csv`
* `insight1.txt`, `insight2.txt`, `insight3.txt`
* `histogram.png`, `heatmap.png`, `scatter.png`
* `clusters.txt`

---

## 📤 Export Results

To copy results from container:

```bash
bash summary.sh
```

---

## 🧠 Notes

* The pipeline is fully automated inside Docker
* No manual steps required after running the container
* Designed for reproducibility and scalability



---
