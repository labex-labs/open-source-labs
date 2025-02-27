# Zeichnen der Anzahl der Knoten und der Tiefe des Baums

Wir werden die Anzahl der Knoten und die Tiefe des Baums als Alpha zunimmt aufzeichnen.

```python
node_counts = [clf.tree_.node_count for clf in clfs]
depth = [clf.tree_.max_depth for clf in clfs]
fig, ax = plt.subplots(2, 1)
ax[0].plot(ccp_alphas, node_counts, marker="o", drawstyle="steps-post")
ax[0].set_xlabel("alpha")
ax[0].set_ylabel("Anzahl der Knoten")
ax[0].set_title("Anzahl der Knoten gegen alpha")
ax[1].plot(ccp_alphas, depth, marker="o", drawstyle="steps-post")
ax[1].set_xlabel("alpha")
ax[1].set_ylabel("Tiefe des Baums")
ax[1].set_title("Tiefe gegen alpha")
fig.tight_layout()
```
