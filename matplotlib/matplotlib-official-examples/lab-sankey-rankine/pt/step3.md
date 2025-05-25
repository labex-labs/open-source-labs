# Criar a Figura e os Eixos

Criaremos um objeto de figura e adicionaremos um único conjunto de eixos a ele. Também definiremos o título do gráfico.

```python
fig = plt.figure(figsize=(8, 9))
ax = fig.add_subplot(1, 1, 1, xticks=[], yticks=[],
                     title="Ciclo de Potência Rankine: Exemplo 8.6 de Moran e "
                     "Shapiro\n\x22Fundamentals of Engineering Thermodynamics "
                     "\x22, 6th ed., 2008")
```
