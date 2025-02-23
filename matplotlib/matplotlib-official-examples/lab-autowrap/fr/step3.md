# Enveloppement automatique du texte

Maintenant, explorons comment envelopper automatiquement le texte dans Matplotlib. Remplacez la ligne `plt.text()` de votre code par la suivante :

```python
t = ("This is a really long string that I'd rather have wrapped so that it "
     "doesn't go outside of the figure, but if it's long enough it will go "
     "off the top or bottom!")
plt.text(5, 5, t, ha='center', wrap=True)
```

L'argument `wrap=True` indique à Matplotlib d'envelopper automatiquement le texte.
