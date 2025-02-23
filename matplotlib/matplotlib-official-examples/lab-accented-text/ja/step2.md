# Unicode文字の使用

Matplotlibは、文字列に直接Unicode文字を使用することもサポートしています。

```python
import matplotlib.pyplot as plt

# Unicodeのデモ
fig, ax = plt.subplots()
ax.set_title("GISCARD CHAHUTÉ À L'ASSEMBLÉE")
ax.set_xlabel("LE COUP DE DÉ DE DE GAULLE")
ax.set_ylabel('André was here!')
ax.text(0.2, 0.8, 'Institut für Festkörperphysik', rotation=45)
ax.text(0.4, 0.2, 'AVA (check kerning)')

plt.show()
```
