# Testando Exceções

Testar é uma parte crucial do desenvolvimento de software, e um aspecto importante disso é garantir que seu código possa lidar com condições de erro adequadamente. Em Python, o módulo `unittest` fornece uma maneira conveniente de testar se exceções específicas são levantadas conforme o esperado.

1.  Abra o arquivo `teststock.py`. Vamos adicionar alguns métodos de teste que são projetados para verificar exceções. Esses testes nos ajudarão a garantir que nosso código se comporte corretamente quando encontrar uma entrada inválida.

```python
def test_shares_type(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(TypeError):
        s.shares = '50'

def test_shares_value(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(ValueError):
        s.shares = -50

def test_price_type(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(TypeError):
        s.price = '490.1'

def test_price_value(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(ValueError):
        s.price = -490.1

def test_attribute_error(self):
    s = stock.Stock('GOOG', 100, 490.1)
    with self.assertRaises(AttributeError):
        s.share = 100  # 'share' is incorrect, should be 'shares'
```

Agora, vamos entender como esses testes de exceção funcionam.

- A instrução `with self.assertRaises(ExceptionType):` cria um gerenciador de contexto (_context manager_). Este gerenciador de contexto verifica se o código dentro do bloco `with` levanta a exceção especificada.
- Se a exceção esperada for levantada dentro do bloco `with`, o teste passa. Isso significa que nosso código está detectando corretamente a entrada inválida e levantando o erro apropriado.
- Se nenhuma exceção for levantada ou uma exceção diferente for levantada, o teste falha. Isso indica que nosso código pode não estar lidando com a entrada inválida conforme o esperado.

Esses testes são projetados para verificar os seguintes cenários:

- Definir o atributo `shares` como uma string deve levantar um `TypeError` porque `shares` deve ser um número.
- Definir o atributo `shares` como um número negativo deve levantar um `ValueError`, pois o número de ações não pode ser negativo.
- Definir o atributo `price` como uma string deve levantar um `TypeError` porque `price` deve ser um número.
- Definir o atributo `price` como um número negativo deve levantar um `ValueError`, pois o preço não pode ser negativo.
- Tentar definir um atributo inexistente `share` (observe a falta de 's') deve levantar um `AttributeError` porque o nome correto do atributo é `shares`.

2.  Depois de adicionar esses métodos de teste, salve o arquivo `teststock.py`. Em seguida, execute todos os testes usando o seguinte comando no seu terminal:

```bash
python3 teststock.py
```

Se tudo estiver funcionando corretamente, você deverá ver uma saída indicando que todos os 12 testes foram aprovados. A saída terá esta aparência:

```
............
----------------------------------------------------------------------
Ran 12 tests in 0.002s

OK
```

Os doze pontos representam todos os testes que você escreveu até agora. Havia 7 testes da etapa anterior, e acabamos de adicionar 5 novos. Esta saída mostra que seu código está lidando com exceções conforme o esperado, o que é um ótimo sinal de um programa bem testado.
