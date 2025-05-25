# Trabalho Interativo Rápido

Para um trabalho interativo rápido, pixels geralmente são uma boa unidade de tamanho. Podemos usar o valor padrão de dpi de 100 para converter valores de pixel para polegadas. Em seguida, podemos usar esse valor como o parâmetro `figsize` na função `subplots`. O código abaixo mostra como criar uma figura com um tamanho de 6 polegadas x 2 polegadas usando valores de pixel.

```python
plt.subplots(figsize=(600/100, 200/100))
plt.show()
```
