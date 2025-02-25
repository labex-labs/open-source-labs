# Création d'un tracé de contour

Nous allons maintenant créer le tracé de contour à l'aide de la fonction `contour()`. Nous passerons les données `X`, `Y` et `Z`, et définirons `extend3d=True` pour étendre les courbes verticalement en rubans. Nous définirons également la carte de couleurs sur `cm.coolwarm` pour un joli schéma de couleurs.

```python
ax.contour(X, Y, Z, extend3d=True, cmap=cm.coolwarm)
```
