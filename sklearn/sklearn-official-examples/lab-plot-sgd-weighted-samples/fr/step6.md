# Ajouter une légende et afficher le tracé

Nous ajoutons une légende au tracé pour différencier les modèles non pondéré et pondéré. Nous affichons ensuite le tracé.

```python
no_weights_handles, _ = no_weights.legend_elements()
weights_handles, _ = samples_weights.legend_elements()
ax.legend(
    [no_weights_handles[0], weights_handles[0]],
    ["sans pondération", "avec pondération"],
    loc="bas à gauche",
)

ax.set(xticks=(), yticks=())
plt.show()
```
