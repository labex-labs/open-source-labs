# Créez des données pour le tracé

Ensuite, nous devons créer des données à tracer. Dans ce laboratoire, nous utiliserons la fonction sinus pour créer nos données. Nous allons générer 500 points régulièrement espacés entre 0 et 10 et calculer le sinus de chaque point en utilisant la fonction `np.sin()`.

```python
x = np.linspace(0, 10, 500)
y = np.sin(x)
```
