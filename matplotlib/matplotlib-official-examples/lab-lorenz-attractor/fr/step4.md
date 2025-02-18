# Calcul de l'attracteur de Lorenz

Nous calculons l'attracteur de Lorenz en avançant dans le temps et en estimant le point suivant en utilisant le point précédent et la fonction de Lorenz.

```python
for i in range(num_steps):
    xyzs[i + 1] = xyzs[i] + lorenz(xyzs[i]) * dt
```
