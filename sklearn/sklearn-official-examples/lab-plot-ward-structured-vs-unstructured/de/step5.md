# Strukturierte hierarchische Cluster darstellen

Wir stellen die strukturierten hierarchischen Cluster mit der Bibliothek `matplotlib` dar.

```python
fig2 = plt.figure()
ax2 = fig2.add_subplot(111, projection="3d", elev=7, azim=-80)
for l in np.unique(label):
    ax2.scatter(
        X[label == l, 0],
        X[label == l, 1],
        X[label == l, 2],
        color=plt.cm.jet(float(l) / np.max(label + 1)),
        s=20,
        edgecolor="k",
    )
```
