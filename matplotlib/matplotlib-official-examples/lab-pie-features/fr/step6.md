# Personnaliser les motifs de hachures

Nous pouvons personnaliser les motifs de hachures des tranches en passant une liste de motifs de hachures au paramètre `hatch` de la fonction `pie()`.

```python
fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, hatch=['**O', 'oO', 'O.O', '.||.'])
```
