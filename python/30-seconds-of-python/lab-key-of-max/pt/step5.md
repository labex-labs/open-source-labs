# Testando com Todos os Valores Negativos

Como um teste final, vamos lidar com um caso em que todos os valores no dicionário são negativos. Adicione este método a `TestKeyOfMax`:

```python
    def test_all_negative_values(self):
        self.assertEqual(key_of_max({'x': -5, 'y': -2, 'z': -10}), 'y')
```

Este teste garante que nossa função identifique corretamente o valor _menos negativo_ (que é o máximo neste caso) e retorne sua chave associada.

Execute seus testes mais uma vez (`python3 test_key_of_max.py`). Todos os quatro testes devem passar. Isso nos dá alta confiança de que nossa função está funcionando corretamente.

Seu `test_key_of_max.py` completo agora deve ser assim:

```python
import unittest
from key_of_max import key_of_max

class TestKeyOfMax(unittest.TestCase):

    def test_basic_case(self):
        self.assertEqual(key_of_max({'a': 4, 'b': 0, 'c': 13}), 'c')

    def test_another_case(self):
        self.assertEqual(key_of_max({'apple': 10, 'banana': 5, 'orange': 10}), 'apple')

    def test_empty_dictionary(self):
        self.assertIsNone(key_of_max({}))

    def test_all_negative_values(self):
        self.assertEqual(key_of_max({'x': -5, 'y': -2, 'z': -10}), 'y')

if __name__ == '__main__':
    unittest.main()
```

Execute os testes novamente (`python3 test_key_of_max.py`). Todos os quatro testes devem passar. Isso nos dá alta confiança de que nossa função está funcionando corretamente.

```python
python3 test_key_of_max.py
```

```plaintext
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```
