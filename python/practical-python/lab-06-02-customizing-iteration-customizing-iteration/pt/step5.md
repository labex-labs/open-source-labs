# Exercício 6.6: Usando um gerador para produzir dados

Se você olhar para o código no Exercício 6.5, a primeira parte do código está produzindo linhas de dados, enquanto as instruções no final do loop `while` estão consumindo os dados. Uma característica importante das funções geradoras (generator functions) é que você pode mover todo o código de produção de dados para uma função reutilizável.

Modifique o código no Exercício 6.5 para que a leitura do arquivo seja realizada por uma função geradora `follow(filename)`. Faça com que o seguinte código funcione:

```python
>>> for line in follow('stocklog.csv'):
          print(line, end='')

... Deve ver linhas de saída produzidas aqui ...
```

Modifique o código do ticker de ações para que ele se pareça com isto:

```python
if __name__ == '__main__':
    for line in follow('stocklog.csv'):
        fields = line.split(',')
        name = fields[0].strip('"')
        price = float(fields[1])
        change = float(fields[4])
        if change < 0:
            print(f'{name:>10s} {price:>10.2f} {change:>10.2f}')
```
