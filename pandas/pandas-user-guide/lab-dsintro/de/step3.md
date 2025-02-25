# Erstellen eines DataFrames

Die andere grundlegende Datenstruktur ist der DataFrame. Es ist eine zweidimensionale markierte Datenstruktur mit Spalten, die möglicherweise unterschiedliche Typen aufweisen.

```python
# Create a DataFrame
df = pd.DataFrame(np.random.randn(6, 4), columns=list('ABCD'))
```
