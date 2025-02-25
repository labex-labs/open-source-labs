# Configure la police Matplotlib

Nous devons configurer la police à utiliser pour le texte Matplotlib. Nous utiliserons la police Computer Modern et la définirons comme police par défaut pour Matplotlib.

```python
plt.rcParams.update({"mathtext.fontset": "cm", "mathtext.rm": "serif"})
```
