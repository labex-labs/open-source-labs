# Création de la figure 1

Nous allons commencer par créer la première figure, qui contiendra deux sous-graphiques. Nous allons tracer la première onde sinusoïdale dans le sous-graphique supérieur et le double de l'amplitude de la première onde sinusoïdale dans le sous-graphique inférieur.

```python
plt.figure(1)

# Sous-graphique supérieur
plt.subplot(211)
plt.plot(t, s1)

# Sous-graphique inférieur
plt.subplot(212)
plt.plot(t, 2*s1)
```
