# Criar Barras de Erro

Nesta etapa, criaremos barras de erro no nosso eixo polar. Usaremos a função `errorbar()` para criar barras de erro tanto para o raio quanto para theta.

```python
ax.errorbar(theta, r, xerr=0.25, yerr=0.1, capsize=7, fmt="o", c="seagreen")
```
