# Usando folhas de estilo (style sheets)

Outra maneira de alterar a aparência visual dos gráficos é definir os rcParams em uma folha de estilo e importar essa folha de estilo com `matplotlib.style.use`. Uma folha de estilo é um arquivo que contém um conjunto de rcParams relacionados ao estilo de um gráfico. Matplotlib fornece vários estilos predefinidos que você pode usar. Por exemplo, o estilo "ggplot" emula a estética da biblioteca ggplot em R. Você pode aplicar uma folha de estilo assim:

```python
import matplotlib.pyplot as plt

print(plt.style.available)
plt.style.use('Solarize_Light2')
```

Você também pode definir seus próprios estilos personalizados e usá-los chamando `.style.use` com o caminho ou URL para a folha de estilo.
