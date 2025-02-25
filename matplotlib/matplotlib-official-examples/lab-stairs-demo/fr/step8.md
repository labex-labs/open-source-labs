# Créez un artiste StepPatch

```python
patch = StepPatch(values=[1, 2, 3, 2, 1],
                  edges=range(1, 7),
                  label=('Patch dérivé de l\'objet sous-jacent\n'
                         'avec le comportement par défaut de la couleur de bord/couleur de face'))
plt.gca().add_patch(patch)
plt.xlim(0, 7)
plt.ylim(-1, 5)
plt.legend()
plt.show()
```
