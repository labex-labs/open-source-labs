# Criando Seu Primeiro Teste Unitário

O módulo `unittest` do Python é uma ferramenta poderosa que oferece uma maneira estruturada de organizar e executar testes. Antes de mergulharmos na escrita do nosso primeiro teste unitário, vamos entender alguns conceitos-chave. _Test fixtures_ (estruturas de teste) são métodos como `setUp` e `tearDown` que ajudam a preparar o ambiente antes de um teste e limpá-lo depois. _Test cases_ (casos de teste) são unidades individuais de teste, _test suites_ (suítes de teste) são coleções de casos de teste, e _test runners_ (executores de teste) são responsáveis por executar esses testes e apresentar os resultados.

Neste primeiro passo, vamos criar um arquivo de teste básico para a classe `Stock`, que já está definida no arquivo `stock.py`.

1.  Primeiro, vamos abrir o arquivo `stock.py`. Isso nos ajudará a entender a classe `Stock` que testaremos. Ao olhar o código em `stock.py`, podemos ver como a classe é estruturada, quais atributos ela tem e quais métodos ela fornece. Para visualizar o conteúdo do arquivo `stock.py`, execute o seguinte comando no seu terminal:

```bash
cat stock.py
```

2.  Agora, é hora de criar um novo arquivo chamado `teststock.py` usando seu editor de texto preferido. Este arquivo conterá nossos casos de teste para a classe `Stock`. Aqui está o código que você precisa escrever no arquivo `teststock.py`:

```python
# teststock.py

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

Vamos detalhar os componentes-chave deste código:

- `import unittest`: Esta linha importa o módulo `unittest`, que fornece as ferramentas e classes necessárias para escrever e executar testes em Python.
- `import stock`: Isso importa o módulo que contém nossa classe `Stock`. Sem esta importação, não seríamos capazes de acessar a classe `Stock` em nosso código de teste.
- `class TestStock(unittest.TestCase)`: Criamos uma nova classe chamada `TestStock` que herda de `unittest.TestCase`. Isso torna nossa classe `TestStock` uma classe de caso de teste, que pode conter vários métodos de teste.
- `def test_create(self)`: Este é um método de teste. No framework `unittest`, todos os métodos de teste devem começar com o prefixo `test_`. Este método cria uma instância da classe `Stock` e, em seguida, usa o método `assertEqual` para verificar se os atributos da instância `Stock` correspondem aos valores esperados.
- `assertEqual`: Este é um método fornecido pela classe `TestCase`. Ele verifica se dois valores são iguais. Se eles não forem iguais, o teste falhará.
- `unittest.main()`: Quando este script é executado diretamente, `unittest.main()` executará todos os métodos de teste na classe `TestStock` e exibirá os resultados.

3.  Depois de escrever o código no arquivo `teststock.py`, salve-o. Em seguida, execute o seguinte comando no seu terminal para executar o teste:

```bash
python3 teststock.py
```

Você deve ver uma saída semelhante a esta:

```
.
----------------------------------------------------------------------
Ran 1 test in 0.001s

OK
```

O ponto único (`.`) na saída indica que um teste passou com sucesso. Se um teste falhar, você verá um `F` em vez do ponto, juntamente com informações detalhadas sobre o que deu errado no teste. Esta saída ajuda você a identificar rapidamente se seu código está funcionando como esperado ou se há algum problema que precisa ser corrigido.
