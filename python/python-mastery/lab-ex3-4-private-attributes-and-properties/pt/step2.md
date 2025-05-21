# Convertendo Métodos em Propriedades

Propriedades em Python permitem que você acesse valores computados como atributos. Isso elimina a necessidade de parênteses ao chamar um método, tornando seu código mais limpo e consistente.

Atualmente, nossa classe `Stock` possui um método `cost()` que calcula o custo total das ações.

```python
def cost(self):
    return self.shares * self.price
```

Para obter o valor do custo, precisamos chamá-lo com parênteses:

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost())  # Calls the method
```

Podemos melhorar isso convertendo o método `cost()` em uma propriedade, permitindo que acessemos o valor do custo sem parênteses:

```python
s = Stock('GOOG', 100, 490.10)
print(s.cost)  # Accesses the property
```

**Instruções:**

1.  Abra o arquivo `stock.py` no editor.

2.  Substitua o método `cost()` por uma propriedade usando o decorador `@property`:

    ```python
    @property
    def cost(self):
        return self.shares * self.price
    ```

3.  Salve o arquivo `stock.py`.

4.  Crie um novo arquivo chamado `test_property.py` no editor:

    ```bash
    touch /home/labex/project/test_property.py
    ```

5.  Adicione o seguinte código ao arquivo `test_property.py` para criar uma instância de `Stock` e acessar a propriedade `cost`:

    ```python
    from stock import Stock

    # Create a stock instance
    s = Stock('GOOG', 100, 490.10)

    # Access cost as a property (no parentheses)
    print(f"Stock: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price}")
    print(f"Cost: {s.cost}")  # Using the property
    ```

6.  Execute o script de teste:

    ```bash
    python /home/labex/project/test_property.py
    ```

    Você deve ver uma saída semelhante a:

    ```
    Stock: GOOG
    Shares: 100
    Price: 490.1
    Cost: 49010.0
    ```
