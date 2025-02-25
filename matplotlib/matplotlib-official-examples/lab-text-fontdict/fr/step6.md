# Personnalisez les étiquettes des axes

Nous pouvons également personnaliser les étiquettes des axes de notre tracé en utilisant le dictionnaire de police. Nous allons définir le paramètre fontdict des fonctions xlabel() et ylabel() sur notre dictionnaire de police.

```python
plt.xlabel('Time (s)', fontdict=font)
plt.ylabel('Voltage (mV)', fontdict=font)
```
