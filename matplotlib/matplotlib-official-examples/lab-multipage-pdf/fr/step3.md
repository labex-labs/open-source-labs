# Créer la première page

Dans cette étape, vous allez créer la première page du fichier PDF. La page contiendra un tracé d'un graphique simple.

```python
plt.figure(figsize=(3, 3))
plt.plot(range(7), [3, 1, 4, 1, 5, 9, 2], 'r-o')
plt.title('Page One')
pdf.savefig()
plt.close()
```
