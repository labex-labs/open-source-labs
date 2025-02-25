# Préparer les données

Nous allons préparer les données pour notre diagramme SkewT-logP. Nous utiliserons le module StringIO pour lire les données à partir d'une chaîne de caractères et NumPy pour les charger dans des tableaux.

```python
data_txt = '''
        978.0    345    7.8    0.8
        971.0    404    7.2    0.2
        946.7    610    5.2   -1.8
     ...
    '''
sound_data = StringIO(data_txt)
p, h, T, Td = np.loadtxt(sound_data, unpack=True)
```
