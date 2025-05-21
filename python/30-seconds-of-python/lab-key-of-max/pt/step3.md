# Criando Testes Unitários: Testes Básicos

Agora, vamos escrever alguns testes para garantir que nossa função funcione corretamente. Usaremos o módulo `unittest` do Python. Crie um novo arquivo chamado `test_key_of_max.py` e adicione o seguinte código:

```python
import unittest
from key_of_max import key_of_max  # Importa nossa função

class TestKeyOfMax(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(key_of_max({'a': 4, 'b': 0, 'c': 13}), 'c')

    def test_another_case(self):
        self.assertEqual(key_of_max({'apple': 10, 'banana': 5, 'orange': 10}), 'apple')

if __name__ == '__main__':
    unittest.main()
```

Explicação:

1.  **`import unittest`**: Importa o framework de testes.
2.  **`from key_of_max import key_of_max`**: Importa a função que queremos testar.
3.  **`class TestKeyOfMax(unittest.TestCase):`**: Define uma _classe de teste_. Classes de teste agrupam testes relacionados.
4.  **`def test_basic_case(self):`**: Define um _método de teste_. Cada método de teste verifica um aspecto específico da nossa função. Os nomes dos métodos de teste _devem_ começar com `test_`.
5.  **`self.assertEqual(...)`**: Esta é uma _asserção_ (assertion). Ela verifica se dois valores são iguais. Se eles não forem iguais, o teste falha. Neste caso, estamos verificando se `key_of_max({'a': 4, 'b': 0, 'c': 13})` retorna `'c'`, o que deveria acontecer.
6.  **`def test_another_case(self):`**: Adicionado outro caso de teste para verificar a chave do valor máximo, que pode não ser único.
7.  **`if __name__ == '__main__': unittest.main()`**: Este idioma Python padrão executa os testes quando você executa o script diretamente (por exemplo, `python3 test_key_of_max.py`).

Execute os testes do seu terminal: `python3 test_key_of_max.py`. Você deve ver a saída indicando que os dois testes passaram.

```python
python3 test_key_of_max.py
```

```plaintext
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
```
