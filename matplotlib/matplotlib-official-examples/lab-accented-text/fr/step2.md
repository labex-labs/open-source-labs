# Utilisation de caractères Unicode

Matplotlib prend également en charge l'utilisation directe de caractères Unicode dans les chaînes de caractères.

```python
import matplotlib.pyplot as plt

# Démo Unicode
fig, ax = plt.subplots()
ax.set_title("GISCARD CHAHUTÉ À L'ASSEMBLÉE")
ax.set_xlabel("LE COUP DE DÉ DE DE GAULLE")
ax.set_ylabel('André était ici!')
ax.text(0.2, 0.8, 'Institut für Festkörperphysik', rotation=45)
ax.text(0.4, 0.2, 'AVA (vérifiez la mise en forme des caractères)')

plt.show()
```
