import numpy as np
from sklearn.datasets import load_iris
from collections import deque

# ---------- Distance Function ----------
def distance(a, b):
    return np.sqrt(np.sum((a - b) ** 2))

# ---------- Region Query ----------
def region_query(X, point_idx, eps):
    neighbors = []
    for i in range(len(X)):
        if distance(X[point_idx], X[i]) <= eps:
            neighbors.append(i)
    return neighbors
# ---------- DBSCAN Algorithm ----------

def dbscan(X, eps, min_pts):
    labels = [0] * len(X) # 0 = unvisited
    cluster_id = 0
    for i in range(len(X)):
        if labels[i] != 0:
            continue
        
        neighbors = region_query(X, i, eps)
        if len(neighbors) < min_pts:
            labels[i] = -1 # mark as noise
        else:
            cluster_id += 1
            labels[i] = cluster_id
            queue = deque(neighbors)
        
            while queue:
                j = queue.popleft()
                if labels[j] == -1:
                    labels[j] = cluster_id

                if labels[j] != 0:
                    continue
                
                labels[j] = cluster_id
                new_neighbors = region_query(X, j, eps)

                if len(new_neighbors) >= min_pts:
                    queue.extend(new_neighbors)
        return labels

# ---------- Load Iris Dataset ----------
iris = load_iris()
X = iris.data # using the 4 features

# ---------- Run DBSCAN ----------
eps = 0.6
min_pts = 5

labels = dbscan(X, eps, min_pts)

print("DBSCAN Cluster Labels:")
print(labels)