# Expandindo Seus Casos de Teste

Agora que você criou um caso de teste básico, é hora de expandir seu escopo de teste. Adicionar mais testes ajudará você a cobrir a funcionalidade restante da classe `Stock`. Dessa forma, você pode garantir que todos os aspectos da classe funcionem como esperado. Vamos modificar a classe `TestStock` para incluir testes para vários métodos e propriedades.

1.  Abra o arquivo `teststock.py`. Dentro da classe `TestStock`, vamos adicionar alguns novos métodos de teste. Esses métodos testarão diferentes partes da classe `Stock`. Aqui está o código que você precisa adicionar:

```python
def test_create_keyword_args(self):
    s = stock.Stock(name='GOOG', shares=100, price=490.1)
    self.assertEqual(s.name, 'GOOG')
    self.assertEqual(s.shares, 100)
    self.assertEqual(s.price, 490.1)

def test_cost(self):
    s = stock.Stock('GOOG', 100, 490.1)
    self.assertEqual(s.cost, 49010.0)

def test_sell(self):
    s = stock.Stock('GOOG', 100, 490.1)
    s.sell(20)
    self.assertEqual(s.shares, 80)

def test_from_row(self):
    row = ['GOOG', '100', '490.1']
    s = stock.Stock.from_row(row)
    self.assertEqual(s.name, 'GOOG')
    self.assertEqual(s.shares, 100)
    self.assertEqual(s.price, 490.1)

def test_repr(self):
    s = stock.Stock('GOOG', 100, 490.1)
    self.assertEqual(repr(s), "Stock('GOOG', 100, 490.1)")

def test_eq(self):
    s1 = stock.Stock('GOOG', 100, 490.1)
    s2 = stock.Stock('GOOG', 100, 490.1)
    self.assertEqual(s1, s2)
```

Vamos dar uma olhada mais de perto no que cada um desses testes faz:

- `test_create_keyword_args`: Este teste verifica se você pode criar um objeto `Stock` usando argumentos de palavra-chave. Ele verifica se os atributos do objeto são definidos corretamente.
- `test_cost`: Este teste verifica se a propriedade `cost` de um objeto `Stock` retorna o valor correto, que é calculado como o número de ações multiplicado pelo preço.
- `test_sell`: Este teste verifica se o método `sell()` de um objeto `Stock` atualiza corretamente o número de ações após a venda de algumas.
- `test_from_row`: Este teste verifica se o método de classe `from_row()` pode criar uma nova instância `Stock` a partir de uma linha de dados.
- `test_repr`: Este teste verifica se o método `__repr__()` de um objeto `Stock` retorna a representação de string esperada.
- `test_eq`: Este teste verifica se o método `__eq__()` compara corretamente dois objetos `Stock` para ver se eles são iguais.

2.  Depois de adicionar esses métodos de teste, salve o arquivo `teststock.py`. Em seguida, execute os testes novamente usando o seguinte comando no seu terminal:

```bash
python3 teststock.py
```

Se todos os testes passarem, você deverá ver uma saída como esta:

```
......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```

Os sete pontos na saída representam cada teste. Cada ponto indica que um teste passou com sucesso. Portanto, se você vir sete pontos, significa que todos os sete testes passaram.
