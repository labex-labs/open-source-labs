# Daten vorbereiten

Wir werden die Daten für unseren SkewT-logP-Diagramm vorbereiten. Wir werden das StringIO-Modul verwenden, um die Daten aus einem String zu lesen, und NumPy, um sie in Arrays zu laden.

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
