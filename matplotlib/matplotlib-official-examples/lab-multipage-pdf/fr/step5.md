# Créer la troisième page

Dans cette étape, vous allez créer la troisième page du fichier PDF. La page contiendra un tracé d'une parabole.

```python
plt.rcParams['text.usetex'] = False
fig = plt.figure(figsize=(4, 5))
plt.plot(x, x ** 2, 'ko')
plt.title('Page Three')
pdf.savefig(fig)  # or you can pass a Figure object to pdf.savefig
plt.close()
```
