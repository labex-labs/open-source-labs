# Titel setzen

In diesem Schritt müssen Sie den Titel jedes Diagramms setzen.

```python
axs[0, 0].set_title('Linear normalization')

for ax, gamma in zip(axs.flat[1:], gammas):
    ax.set_title(r'Potenzgesetz $(\gamma=%1.1f)$' % gamma)
```
