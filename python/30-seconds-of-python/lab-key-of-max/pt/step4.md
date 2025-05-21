# Testando o Dicionário Vazio (Caso de Borda)

Vamos adicionar um teste especificamente para o caso de dicionário vazio. Adicione este método à sua classe `TestKeyOfMax` em `test_key_of_max.py`:

```python
    def test_empty_dictionary(self):
        self.assertIsNone(key_of_max({}))
```

- **`self.assertIsNone(...)`**: Esta asserção verifica se o valor é especificamente `None`. Isso é importante porque `self.assertEqual(..., None)` poderia passar para coisas que _avaliam_ para `None`, mas na verdade não são `None`. `assertIsNone` é mais rigoroso.

Execute os testes novamente (`python3 test_key_of_max.py`). Todos os três testes (os dois testes básicos e o teste do dicionário vazio) devem agora passar.

```python
python3 test_key_of_max.py
```

```plaintext
----------------------------------------------------------------------
Ran 3 tests in 0.000s

OK
```
