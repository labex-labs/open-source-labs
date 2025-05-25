# Criar Subplots para Gráficos de Exemplo

Criaremos uma grade de subplots 3 x 3 para exibir nossos gráficos de exemplo.

```python
fig, axs = plt.subplots(
    3, 3, figsize=(9, 9), layout="constrained", gridspec_kw={"hspace": 0.1})
```
