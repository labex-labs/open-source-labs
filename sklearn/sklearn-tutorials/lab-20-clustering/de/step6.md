# Bewerten des Clusterings

Um die Clusterergebnisse zu bewerten, können wir die Trägheit (Inertia) der Cluster berechnen, die die Summe der quadrierten Abstände der Proben zu ihrem nächsten Clusterzentrum darstellt.

```python
# Calculate the inertia of the clusters
inertia = kmeans.inertia_
print("Inertia:", inertia)
```
