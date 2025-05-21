# Atualizando e Testando o Programa stock.py

Agora que criamos nosso pacote e corrigimos as importações internas, é hora de atualizar o arquivo `stock.py` para usar nossa nova estrutura de pacote. Um pacote em Python é uma maneira de organizar módulos relacionados juntos. Ele ajuda a manter seu código organizado e facilita o gerenciamento e a reutilização do código.

Abra o arquivo `stock.py` no editor:

```bash
# Click on stock.py in the file explorer or run:
code stock.py
```

As importações atuais em `stock.py` são baseadas na estrutura antiga, onde todos os arquivos estavam no mesmo diretório. Em Python, quando você importa um módulo, o Python procura o módulo em locais específicos. Na estrutura antiga, como todos os arquivos estavam no mesmo diretório, o Python conseguia encontrar os módulos facilmente. Mas agora, com a nova estrutura do pacote, precisamos atualizar as importações para dizer ao Python onde encontrar os módulos dentro do pacote `structly`.

Atualize o arquivo `stock.py` para ficar exatamente assim:

```python
# stock.py

from structly.structure import Structure, String, PositiveInteger, PositiveFloat

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares

if __name__ == '__main__':
    from structly.reader import read_csv_as_instances
    from structly.tableformat import create_formatter, print_table
    portfolio = read_csv_as_instances('portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
```

As principais mudanças são:

1. Mudou `from structure import Structure, String, PositiveInteger, PositiveFloat` para `from structly.structure import Structure, String, PositiveInteger, PositiveFloat`. Essa alteração diz ao Python para procurar o módulo `structure` dentro do pacote `structly`.
2. Mudou `from reader import read_csv_as_instances` para `from structly.reader import read_csv_as_instances`. Da mesma forma, essa alteração direciona o Python a encontrar o módulo `reader` dentro do pacote `structly`.
3. Mudou `from tableformat import create_formatter, print_table` para `from structly.tableformat import create_formatter, print_table`. Isso garante que o Python localize o módulo `tableformat` no pacote `structly`.

Salve o arquivo após fazer essas alterações. Salvar o arquivo é importante porque garante que as alterações que você fez sejam armazenadas e possam ser usadas quando você executar o programa.

Agora, vamos testar nosso código atualizado para garantir que tudo funcione corretamente:

```bash
python stock.py
```

Você deve ver a seguinte saída:

```
      name      shares       price
---------- ---------- ----------
      MSFT        100      51.23
       IBM         50       91.1
      AAPL         75     145.89
      ACME        125     123.45
       HPE         75       32.2
```

Se você vir essa saída, parabéns! Você criou com sucesso um pacote Python e atualizou seu código para usá-lo. Isso significa que seu código agora está organizado de uma forma mais modular, tornando-o mais fácil de manter e expandir no futuro.
