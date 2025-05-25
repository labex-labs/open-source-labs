# Criar o gráfico

Agora, criamos um gráfico com dois eixos y usando a função `subplots()` de `matplotlib.pyplot`. Também conectamos o evento `ylim_changed` do primeiro eixo à função `convert_ax_c_to_celsius()`.

```python
fig, ax_f = plt.subplots()
ax_c = ax_f.twinx()

ax_f.callbacks.connect("ylim_changed", convert_ax_c_to_celsius)
```
