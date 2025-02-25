# Définir la fonction d'onde sinusoïdale

Ensuite, nous allons définir la fonction qui générera notre onde sinusoïdale. La fonction prendra deux paramètres, amplitude et fréquence, et renverra l'onde sinusoïdale à un moment donné.

```python
def f(t, amplitude, frequency):
    return amplitude * np.sin(2 * np.pi * frequency * t)
```
