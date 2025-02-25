# Création d'un DataFrame

L'autre structure de données fondamentale est le DataFrame. C'est une structure de données étiquetée à deux dimensions avec des colonnes de types potentiellement différents.

```python
# Create a DataFrame
df = pd.DataFrame(np.random.randn(6, 4), columns=list('ABCD'))
```
