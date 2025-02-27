# Graficar el número de nodos y la profundidad del árbol

Graficaremos el número de nodos y la profundidad del árbol a medida que aumenta el alfa.

```python
node_counts = [clf.tree_.node_count for clf in clfs]
depth = [clf.tree_.max_depth for clf in clfs]
fig, ax = plt.subplots(2, 1)
ax[0].plot(ccp_alphas, node_counts, marker="o", drawstyle="steps-post")
ax[0].set_xlabel("alpha")
ax[0].set_ylabel("número de nodos")
ax[0].set_title("Número de nodos vs alpha")
ax[1].plot(ccp_alphas, depth, marker="o", drawstyle="steps-post")
ax[1].set_xlabel("alpha")
ax[1].set_ylabel("profundidad del árbol")
ax[1].set_title("Profundidad vs alpha")
fig.tight_layout()
```
