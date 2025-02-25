# Contrôler la taille

Nous pouvons contrôler la taille du diagramme circulaire à secteurs en configurant le paramètre `radius` de la fonction `pie()`.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%.0f%%',
       textprops={'size':'smaller'}, radius=0.5)
```
