# Implementando Atributos Privados

Em Python, usamos uma convenção de nomenclatura para indicar que um atributo se destina ao uso interno dentro de uma classe. Prefixamos esses atributos com um sublinhado (`_`). Isso sinaliza a outros desenvolvedores que esses atributos não fazem parte da API pública e não devem ser acessados diretamente de fora da classe.

Vamos analisar a classe `Stock` atual no arquivo `stock.py`. Ela possui uma variável de classe chamada `types`.

```python
class Stock:
    # Class variable for type conversions
    types = (str, int, float)

    # Rest of the class...
```

A variável de classe `types` é usada internamente para converter dados de linha. Para indicar que este é um detalhe de implementação, vamos marcá-la como privada.

**Instruções:**

1.  Abra o arquivo `stock.py` no editor.

2.  Modifique a variável de classe `types` adicionando um sublinhado inicial, alterando-a para `_types`.

    ```python
    class Stock:
        # Class variable for type conversions
        _types = (str, int, float)

        # Rest of the class...
    ```

3.  Atualize o método `from_row` para usar a variável renomeada `_types`.

    ```python
    @classmethod
    def from_row(cls, row):
        values = [func(val) for func, val in zip(cls._types, row)]
        return cls(*values)
    ```

4.  Salve o arquivo `stock.py`.

5.  Crie um script Python chamado `test_stock.py` para testar suas alterações. Você pode criar o arquivo no editor usando o seguinte comando:

    ```bash
    touch /home/labex/project/test_stock.py
    ```

6.  Adicione o seguinte código ao arquivo `test_stock.py`. Este código cria instâncias da classe `Stock` e imprime informações sobre elas.

    ```python
    from stock import Stock

    # Create a stock instance
    s = Stock('GOOG', 100, 490.10)
    print(f"Name: {s.name}, Shares: {s.shares}, Price: {s.price}")
    print(f"Cost: {s.cost()}")

    # Create from row
    row = ['AAPL', '50', '142.5']
    apple = Stock.from_row(row)
    print(f"Name: {apple.name}, Shares: {apple.shares}, Price: {apple.price}")
    print(f"Cost: {apple.cost()}")
    ```

7.  Execute o script de teste usando o seguinte comando no terminal:

    ```bash
    python /home/labex/project/test_stock.py
    ```

    Você deve ver uma saída semelhante a:

    ```
    Name: GOOG, Shares: 100, Price: 490.1
    Cost: 49010.0
    Name: AAPL, Shares: 50, Price: 142.5
    Cost: 7125.0
    ```
