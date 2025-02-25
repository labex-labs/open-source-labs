# Créer la deuxième page

Dans cette étape, vous allez créer la deuxième page du fichier PDF. La page contiendra un tracé d'une onde sinusoïdale.

```python
plt.rcParams['text.usetex'] = True
plt.figure(figsize=(8, 6))
x = np.arange(0, 5, 0.1)
plt.plot(x, np.sin(x), 'b-')
plt.title('Page Two')
pdf.attach_note("plot of sin(x)")  # attach metadata (as pdf note) to page
pdf.savefig()
plt.close()
```
