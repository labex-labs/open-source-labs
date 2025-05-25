# Criar uma Função para Definir Parâmetros Padrão

Para criar uma função que define os parâmetros padrão para suas figuras, você pode usar o método `rcParams.update()`. Este método recebe um dicionário de nomes e valores de parâmetros e atualiza os valores padrão atuais com os novos. Aqui está um exemplo de uma função que define alguns parâmetros padrão para figuras de publicação:

```python
def set_pub():
    rcParams.update({
        "font.weight": "bold",  # bold fonts
        "tick.labelsize": 15,   # large tick labels
        "lines.linewidth": 1,   # thick lines
        "lines.color": "k",     # black lines
        "grid.color": "0.5",    # gray gridlines
        "grid.linestyle": "-",  # solid gridlines
        "grid.linewidth": 0.5,  # thin gridlines
        "savefig.dpi": 300,     # higher resolution output.
    })
```
