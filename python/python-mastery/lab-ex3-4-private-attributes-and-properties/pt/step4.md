# Usando `__slots__` para Otimização de Memória

O atributo `__slots__` restringe os atributos que uma classe pode ter. Ele impede a adição de novos atributos às instâncias e reduz o uso de memória.

Em nossa classe `Stock`, usaremos `__slots__` para:

1.  Restringir a criação de atributos apenas aos atributos que definimos.
2.  Melhorar a eficiência da memória, especialmente ao criar muitas instâncias.

**Instruções:**

1.  Abra o arquivo `stock.py` no editor.
2.  Adicione uma variável de classe `__slots__`, listando todos os nomes de atributos privados usados pela classe:

    ```python
    class Stock:
        # Class variable for type conversions
        _types = (str, int, float)

        # Define slots to restrict attribute creation
        __slots__ = ('name', '_shares', '_price')

        # Rest of the class...
    ```

3.  Salve o arquivo.

4.  Crie um script de teste chamado `test_slots.py`:

    ```bash
    touch /home/labex/project/test_slots.py
    ```

5.  Adicione o seguinte código ao arquivo `test_slots.py`:

    ```python
    from stock import Stock

    # Create a stock instance
    s = Stock('GOOG', 100, 490.10)

    # Access existing attributes
    print(f"Name: {s.name}")
    print(f"Shares: {s.shares}")
    print(f"Price: {s.price}")
    print(f"Cost: {s.cost}")

    # Try to add a new attribute
    try:
        s.extra = "This will fail"
        print(f"Extra: {s.extra}")
    except AttributeError as e:
        print(f"Error: {e}")
    ```

6.  Execute o script de teste:

    ```bash
    python /home/labex/project/test_slots.py
    ```

    Você deve ver a saída mostrando que você pode acessar os atributos definidos, mas tentar adicionar um novo atributo levanta um `AttributeError`.

    ```plaintext
    Name: GOOG
    Shares: 100
    Price: 490.1
    Cost: 49010.0
    Error: 'Stock' object has no attribute 'extra'
    ```
