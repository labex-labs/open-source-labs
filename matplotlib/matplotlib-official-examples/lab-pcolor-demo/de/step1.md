# Einfaches Pcolor-Demo

Der erste Schritt besteht darin, ein einfaches Pcolor-Demo zu erstellen. Dies wird Ihnen zeigen, wie ein grundlegender Pcolor-Plot erstellt wird.

```python
Z = np.random.rand(6, 10)

fig, (ax0, ax1) = plt.subplots(2, 1)

c = ax0.pcolor(Z)
ax0.set_title('standardmäßig: keine Kanten')

c = ax1.pcolor(Z, edgecolors='k', linewidths=4)
ax1.set_title('dicke Kanten')

fig.tight_layout()
plt.show()
```
