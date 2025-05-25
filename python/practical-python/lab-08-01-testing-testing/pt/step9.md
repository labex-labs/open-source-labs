# Exercício 8.1: Escrevendo Testes Unitários (Unit Tests)

Em um arquivo separado `test_stock.py`, escreva um conjunto de testes unitários para a classe `Stock`. Para começar, aqui está um pequeno fragmento de código que testa a criação de instâncias:

```python
# test_stock.py

import unittest
import stock

class TestStock(unittest.TestCase):
    def test_create(self):
        s = stock.Stock('GOOG', 100, 490.1)
        self.assertEqual(s.name, 'GOOG')
        self.assertEqual(s.shares, 100)
        self.assertEqual(s.price, 490.1)

if __name__ == '__main__':
    unittest.main()
```

Execute seus testes unitários. Você deve obter uma saída semelhante a esta:

    .
    ----------------------------------------------------------------------
    Ran 1 tests in 0.000s

    OK

Depois de se certificar de que funciona, escreva testes unitários adicionais que verifiquem o seguinte:

- Certifique-se de que a propriedade `s.cost` retorna o valor correto (49010.0)
- Certifique-se de que o método `s.sell()` funciona corretamente. Ele deve decrementar o valor de `s.shares` de acordo.
- Certifique-se de que o atributo `s.shares` não pode ser definido com um valor não inteiro.

Para a última parte, você precisará verificar se uma exceção é levantada. Uma maneira fácil de fazer isso é com um código como este:

```python
class TestStock(unittest.TestCase):
    ...
    def test_bad_shares(self):
         s = stock.Stock('GOOG', 100, 490.1)
         with self.assertRaises(TypeError):
             s.shares = '100'
```
