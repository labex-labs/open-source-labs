# Générer l'ensemble de Mandelbrot

Maintenant, nous allons générer l'ensemble de Mandelbrot en appelant la fonction `mandelbrot_set` avec les paramètres souhaités. Cela nous donnera deux tableaux :

- `Z` : les valeurs finales des nombres complexes sur lesquels nous avons itéré
- `N` : le nombre d'itérations effectuées pour chaque point avant qu'il ne soit déterminé comme faisant partie de l'ensemble

```python
xmin, xmax, xn = -2.25, +0.75, 3000 // 2
ymin, ymax, yn = -1.25, +1.25, 2500 // 2
maxiter = 200
horizon = 2.0 ** 40
log_horizon = np.log2(np.log(horizon))
Z, N = mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon)
```
