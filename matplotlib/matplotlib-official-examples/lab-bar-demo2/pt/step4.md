# Definir as Unidades x e y para o Gráfico de Barras

Nesta etapa, definiremos as unidades x e y para o gráfico de barras usando várias palavras-chave. Usaremos os parâmetros `xunits` e `yunits` para definir as unidades x e y para centímetros e polegadas.

```python
axs[0, 1].bar(cms, cms, bottom=bottom, width=width, xunits=cm, yunits=inch)
```
