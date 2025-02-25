# Créez deux histogrammes avec des barres empilées

Nous pouvons créer deux histogrammes avec des barres empilées en appelant la fonction `hist` deux fois et en définissant le paramètre `histtype` sur `'barstacked'`. Dans cet exemple, nous allons créer deux histogrammes avec des barres empilées.

```python
plt.hist(x, density=True, histtype='barstacked', rwidth=0.8)
plt.hist(w, density=True, histtype='barstacked', rwidth=0.8)
plt.show()
```
