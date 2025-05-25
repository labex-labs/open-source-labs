# Criar Eixos Host e Parasitas

Criaremos um eixo host (host axis) e dois eixos parasitas usando as funções `host_subplot()` e `twinx()`. A função `host_subplot()` cria um eixo host, e a função `twinx()` cria eixos parasitas que compartilham o mesmo eixo x com o eixo host.

```python
host = host_subplot(111, axes_class=axisartist.Axes)
plt.subplots_adjust(right=0.75)

par1 = host.twinx()
par2 = host.twinx()
```
