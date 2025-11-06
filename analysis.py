import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import warnings

# Suppress warnings
warnings.filterwarnings('ignore')

print("Starting analysis...")


try:
    # Load the dataset from the CSV file 
    data = pd.read_csv('xy_data.csv')
    print(f"Successfully loaded xy_data.csv. Found {len(data)} data points.")
except FileNotFoundError:
    print("Error: xy_data.csv not found.")
    print("Please make sure the file is in the same directory as this script.")
    exit()

# Extract the 'x' and 'y' columns for clustering 
X = data[['x', 'y']]

# Scale the data 
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#  Find the Optimal Number of Clusters (Elbow Method) ---
print("Calculating optimal 'k' using the Elbow Method...")
inertia = []
K_range = range(1, 11)  # We will test k from 1 to 10

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    inertia.append(kmeans.inertia_)

# Plot the Elbow Method results
plt.figure(figsize=(10, 6))
plt.plot(K_range, inertia, 'bo-')
plt.xlabel('Number of clusters (k)')
plt.ylabel('Inertia (Sum of squared distances)')
plt.title('Elbow Method for Optimal k')
plt.grid(True)
plt.savefig('elbow_plot.png')
print("Saved 'elbow_plot.png'.")

# --- Step 3: Run K-Means with the Optimal k ---
# Looking at the elbow plot, the "elbow" (point of diminishing returns)
# appears to be at k=4. We will proceed with 4 clusters.
optimal_k = 4
print(f"Based on the elbow plot, setting optimal k = {optimal_k}")

kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
# Fit the model and predict the cluster for each point
data['cluster'] = kmeans.fit_predict(X_scaled)

# Get the cluster centers (and un-scale them back to original coordinates)
centers_scaled = kmeans.cluster_centers_
centers = scaler.inverse_transform(centers_scaled)

# Visualize the Final Clusters 
print("Visualizing final clusters...")
plt.figure(figsize=(12, 8))
# Plot all data points, colored by their assigned cluster
sns.scatterplot(data=data, x='x', y='y', hue='cluster', palette='viridis', s=100, alpha=0.7, legend='full') 

# Plot the cluster centers
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=250, marker='X', label='Centroids')

plt.title(f'K-Means Clustering (k={optimal_k}) of Spatial Data')
plt.xlabel('X Coordinate') 
plt.ylabel('Y Coordinate') 
plt.legend()
plt.grid(True)
plt.savefig('cluster_plot.png')
print("Saved 'cluster_plot.png'.")
print("\nAnalysis complete. Check the folder for 'elbow_plot.png' and 'cluster_plot.png'.")