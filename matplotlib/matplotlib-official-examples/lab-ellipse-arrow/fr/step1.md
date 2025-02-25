# Import Matplotlib et créer une figure et un axe

Tout d'abord, vous devez importer Matplotlib et créer une figure et un axe. La figure et l'axe sont les conteneurs de votre tracé.

```python
import matplotlib.pyplot as plt

# Crée une figure et un axe
fig, ax = plt.subplots(subplot_kw={"aspect": "equal"})
```
