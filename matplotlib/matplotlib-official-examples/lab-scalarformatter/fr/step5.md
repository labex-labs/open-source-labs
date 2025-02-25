# Configurer la mise en forme des étiquettes d'échelle

Nous allons configurer la mise en forme des étiquettes d'échelle pour nos sous-graphiques. Le premier sous-graphique utilisera les paramètres par défaut, le second sous-graphique utilisera une mise en forme élégante d'expressions mathématiques et le troisième sous-graphique n'utilisera pas la notation d'offset.

```python
# Sous-graphique 1 (paramètres par défaut)
axs[0, 0].set_title("paramètres par défaut")

# Sous-graphique 2 (useMathText=True)
for ax in axs[:, 1]:
    ax.ticklabel_format(useMathText=True)
axs[0, 1].set_title("useMathText=True")

# Sous-graphique 3 (useOffset=False)
for ax in axs[:, 2]:
    ax.ticklabel_format(useOffset=False)
axs[0, 2].set_title("useOffset=False")
```
