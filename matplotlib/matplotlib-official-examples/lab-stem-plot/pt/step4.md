# Personalizando o Gráfico

Podemos personalizar o gráfico ajustando a linha de base usando o parâmetro `bottom`. Também podemos ajustar as propriedades de formato do gráfico usando os parâmetros `linefmt`, `markerfmt` e `basefmt`.

```python
markerline, stemlines, baseline = plt.stem(
    x, y, linefmt='grey', markerfmt='D', bottom=1.1)
markerline.set_markerfacecolor('none')
plt.show()
```

Isso gerará um gráfico com um formato de linha cinza e marcadores em forma de diamante. A linha de base também foi ajustada para 1.1.
