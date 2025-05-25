# Criar um diagrama de Sankey simples

Começaremos criando um diagrama de Sankey simples que demonstra como usar a classe Sankey.

```python
Sankey(flows=[0.25, 0.15, 0.60, -0.20, -0.15, -0.05, -0.50, -0.10],
       labels=['', '', '', 'First', 'Second', 'Third', 'Fourth', 'Fifth'],
       orientations=[-1, 1, 0, 1, 1, 1, 0, -1]).finish()
plt.title("The default settings produce a diagram like this.")
```

Este código produzirá um diagrama de Sankey com as configurações padrão, que incluem os rótulos e orientações dos fluxos. O diagrama resultante será exibido com o título "The default settings produce a diagram like this."
