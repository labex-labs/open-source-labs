# Implementando Validação de Propriedades

Propriedades também permitem que você controle como os valores dos atributos são recuperados, definidos e excluídos. Isso é útil para adicionar validação aos seus atributos, garantindo que os valores atendam a critérios específicos.

Em nossa classe `Stock`, queremos garantir que `shares` seja um inteiro não negativo e `price` seja um float não negativo. Usaremos decoradores de propriedade junto com getters e setters para conseguir isso.

**Instruções:**

1.  Abra o arquivo `stock.py` no editor.

2.  Adicione os atributos privados `_shares` e `_price` à classe `Stock` e modifique o construtor para usá-los:

    ```python
    def __init__(self, name, shares, price):
        self.name = name
        self._shares = shares  # Using private attribute
        self._price = price    # Using private attribute
    ```

3.  Defina propriedades para `shares` e `price` com validação:

    ```python
    @property
    def shares(self):
        return self._shares

    @shares.setter
    def shares(self, value):
        if not isinstance(value, int):
            raise TypeError("Expected integer")
        if value < 0:
            raise ValueError("shares must be >= 0")
        self._shares = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise TypeError("Expected float")
        if value < 0:
            raise ValueError("price must be >= 0")
        self._price = value
    ```

4.  Atualize o construtor para usar os setters de propriedade para validação:

    ```python
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares  # Using property setter
        self.price = price    # Using property setter
    ```

5.  Salve o arquivo `stock.py`.

6.  Crie um script de teste chamado `test_validation.py`:

    ```bash
    touch /home/labex/project/test_validation.py
    ```

7.  Adicione o seguinte código ao arquivo `test_validation.py`:

    ```python
    from stock import Stock

    # Create a valid stock instance
    s = Stock('GOOG', 100, 490.10)
    print(f"Initial: Name={s.name}, Shares={s.shares}, Price={s.price}, Cost={s.cost}")

    # Test valid updates
    try:
        s.shares = 50  # Valid update
        print(f"After setting shares=50: Shares={s.shares}, Cost={s.cost}")
    except Exception as e:
        print(f"Error setting shares=50: {e}")

    try:
        s.price = 123.45  # Valid update
        print(f"After setting price=123.45: Price={s.price}, Cost={s.cost}")
    except Exception as e:
        print(f"Error setting price=123.45: {e}")

    # Test invalid updates
    try:
        s.shares = "50"  # Invalid type (string)
        print("This line should not execute")
    except Exception as e:
        print(f"Error setting shares='50': {e}")

    try:
        s.shares = -10  # Invalid value (negative)
        print("This line should not execute")
    except Exception as e:
        print(f"Error setting shares=-10: {e}")

    try:
        s.price = "123.45"  # Invalid type (string)
        print("This line should not execute")
    except Exception as e:
        print(f"Error setting price='123.45': {e}")

    try:
        s.price = -10.0  # Invalid value (negative)
        print("This line should not execute")
    except Exception as e:
        print(f"Error setting price=-10.0: {e}")
    ```

8.  Execute o script de teste:

    ```bash
    python /home/labex/project/test_validation.py
    ```

    Você deve ver a saída mostrando atualizações válidas bem-sucedidas e mensagens de erro apropriadas para atualizações inválidas.

    ```plaintext
    Initial: Name=GOOG, Shares=100, Price=490.1, Cost=49010.0
    After setting shares=50: Shares=50, Cost=24505.0
    After setting price=123.45: Price=123.45, Cost=6172.5
    Error setting shares='50': Expected integer
    Error setting shares=-10: shares must be >= 0
    Error setting price='123.45': Expected float
    Error setting price=-10.0: price must be >= 0
    ```
