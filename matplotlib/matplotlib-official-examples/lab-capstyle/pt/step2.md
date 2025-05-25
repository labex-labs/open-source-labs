# Criar um Gráfico

Em seguida, criaremos um gráfico simples para demonstrar as diferentes opções de `CapStyle`.

```python
fig, ax = plt.subplots()

# Plotando a linha com diferentes opções de CapStyle
for i, cap_style in enumerate(CapStyle):
    ax.plot([0, 1], [i, i], label=str(cap_style), linewidth=10, solid_capstyle=cap_style)

# Adicionando legenda e título
ax.legend(title='CapStyle')
ax.set_title('Demonstração de CapStyle')
```
