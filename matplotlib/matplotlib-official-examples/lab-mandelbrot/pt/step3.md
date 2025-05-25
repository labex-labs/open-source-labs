# Gerar o Conjunto de Mandelbrot

Agora, geraremos o conjunto de Mandelbrot chamando a função `mandelbrot_set` com nossos parâmetros desejados. Isso nos dará dois arrays:

- `Z`: os valores finais dos números complexos sobre os quais iteramos
- `N`: o número de iterações realizadas para cada ponto antes de ser determinado como parte do conjunto

```python
xmin, xmax, xn = -2.25, +0.75, 3000 // 2
ymin, ymax, yn = -1.25, +1.25, 2500 // 2
maxiter = 200
horizon = 2.0 ** 40
log_horizon = np.log2(np.log(horizon))
Z, N = mandelbrot_set(xmin, xmax, ymin, ymax, xn, yn, maxiter, horizon)
```
