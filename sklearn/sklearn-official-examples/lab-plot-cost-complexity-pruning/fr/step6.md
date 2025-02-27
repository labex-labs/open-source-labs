# Tracer le nombre de nœuds et la profondeur de l'arbre

Nous allons tracer le nombre de nœuds et la profondeur de l'arbre au fur et à mesure que alpha augmente.

```python
node_counts = [clf.tree_.node_count for clf in clfs]
depth = [clf.tree_.max_depth for clf in clfs]
fig, ax = plt.subplots(2, 1)
ax[0].plot(ccp_alphas, node_counts, marker="o", drawstyle="steps-post")
ax[0].set_xlabel("alpha")
ax[0].set_ylabel("nombre de nœuds")
ax[0].set_title("Nombre de nœuds vs alpha")
ax[1].plot(ccp_alphas, depth, marker="o", drawstyle="steps-post")
ax[1].set_xlabel("alpha")
ax[1].set_ylabel("profondeur de l'arbre")
ax[1].set_title("Profondeur vs alpha")
fig.tight_layout()
```
