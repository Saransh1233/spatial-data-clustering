# spatial-data-clustering

A Python project that uses K-Means clustering to analyze the `xy_data.csv` file and identify 4 distinct spatial clusters.

## 📝 Overview

This project applies the K-Means unsupervised clustering algorithm to a dataset of 1,000 spatial (x, y) coordinates. The script automatically determines the optimal number of clusters using the Elbow Method and then generates a final plot visualizing the distinct groups.

This repository contains all necessary code, data, and deliverables for the project submission.

## 🗂️ Files in This Repository

* `analysis.py`: The main Python script that loads the data, runs the analysis, and saves the plots.
* `xy_data.csv`: The input dataset containing 1,501 (x, y) coordinate pairs.
* `final_report.docx`: The final 3-page project report detailing the methodology and results.
* `presentation_video.mp4`: A 5-minute video presentation summarizing the project.
* `elbow_plot.png`: Output image showing the Elbow Method results, justifying k=4.
* `cluster_plot.png`: Output image showing the final 4 identified clusters.

## 🚀 How to Run

### 1. Prerequisites

You must have Python 3 installed, along with the following libraries:
* pandas
* scikit-learn
* matplotlib
* seaborn

You can install these dependencies using pip:
```
pip install pandas scikit-learn matplotlib seaborn
```
## Execute the Script
To run the analysis, clone this repository, navigate to the project directory in your terminal, and run the analysis.py script. Ensure xy_data.csv is in the same folder.
The script will print its progress to the console and will automatically generate two image files: elbow_plot.png and cluster_plot.png.


## Methodology
Data Loading & Preprocessing: The xy_data.csv file is loaded. The 'x' and 'y' features are scaled using StandardScaler to ensure the K-Means algorithm weights both axes equally.

Optimal 'k': The Elbow Method is used to find the optimal number of clusters ('k'). The script calculates and plots the inertia (sum of squared distances) for k-values from 1 to 10.

Clustering: The K-Means algorithm is run using the optimal k=4, as determined by the Elbow Method and required by the project.


## Results
The analysis successfully identifies 4 distinct clusters from the spatial data.

###Elbow Method (Justifying k=4)
The script generates elbow_plot.png, which clearly shows a "bend" or "elbow" at k=4, indicating that this is the optimal number of clusters.

###Final Clusters
The script generates cluster_plot.png, which visualizes the 4 final clusters (color-coded) and their calculated centroids (marked with a red 'X').
