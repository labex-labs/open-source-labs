# Verwenden von Unicode-Zeichen

Matplotlib unterstützt auch die direkte Verwendung von Unicode-Zeichen in Zeichenketten.

```python
import matplotlib.pyplot as plt

# Unicode-Demo
fig, ax = plt.subplots()
ax.set_title("GISCARD CHAHUTÉ À L'ASSEMBLÉE")
ax.set_xlabel("LE COUP DE DÉ DE DE GAULLE")
ax.set_ylabel('André war hier!')
ax.text(0.2, 0.8, 'Institut für Festkörperphysik', rotation=45)
ax.text(0.4, 0.2, 'AVA (prüfe die Kerning)')

plt.show()
```
