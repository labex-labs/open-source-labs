# Использование символов Unicode

Matplotlib также поддерживает использование символов Unicode непосредственно в строках.

```python
import matplotlib.pyplot as plt

# Демонстрация Unicode
fig, ax = plt.subplots()
ax.set_title("GISCARD CHAHUTÉ À L'ASSEMBLÉE")
ax.set_xlabel("LE COUP DE DÉ DE DE GAULLE")
ax.set_ylabel('André был здесь!')
ax.text(0.2, 0.8, 'Institut für Festkörperphysik', rotation=45)
ax.text(0.4, 0.2, 'AVA (проверьте кернинг)')

plt.show()
```
