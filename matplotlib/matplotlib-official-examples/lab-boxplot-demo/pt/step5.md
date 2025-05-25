# Adicionar rótulos e títulos

Finalmente, podemos adicionar rótulos e títulos ao nosso boxplot para torná-lo mais informativo. Podemos adicionar rótulos aos eixos x e y, bem como um título ao gráfico. Também podemos alterar o tamanho e o estilo da fonte dos rótulos e do título. Aqui está um exemplo de como adicionar rótulos e títulos:

```python
plt.boxplot([data1, data2, data3])
plt.xlabel('Grupo')
plt.ylabel('Valor')
plt.title('Comparação de Três Grupos')
plt.xticks([1, 2, 3], ['Grupo 1', 'Grupo 2', 'Grupo 3'])
plt.show()
```
