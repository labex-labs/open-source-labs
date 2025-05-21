# Criando um Gerenciador de Contexto

Um gerenciador de contexto é um tipo especial de objeto em Python. Em Python, os objetos podem ter diferentes métodos que definem seu comportamento. Um gerenciador de contexto define especificamente dois métodos importantes: `__enter__` e `__exit__`. Esses métodos trabalham juntos com a instrução `with`. A instrução `with` é usada para configurar um contexto específico para um bloco de código. Pense nisso como a criação de um pequeno ambiente onde certas coisas acontecem e, quando o bloco de código é finalizado, o gerenciador de contexto cuida da limpeza.

Nesta etapa, vamos criar um gerenciador de contexto que tem uma função muito útil. Ele redirecionará temporariamente a saída padrão (`sys.stdout`). A saída padrão é onde a saída normal do seu programa Python vai, geralmente o console. Ao redirecioná-la, podemos enviar a saída para um arquivo em vez disso. Isso é útil quando você deseja salvar a saída que, de outra forma, seria exibida apenas no console.

Primeiro, precisamos criar um novo arquivo para escrever nosso código do gerenciador de contexto. Vamos nomear este arquivo `redirect.py`. Você pode criá-lo usando o seguinte comando no terminal:

```bash
touch /home/labex/project/redirect.py
```

Agora que o arquivo foi criado, abra-o em um editor. Depois de aberto, adicione o seguinte código Python ao arquivo:

```python
import sys

class redirect_stdout:
    def __init__(self, out_file):
        self.out_file = out_file

    def __enter__(self):
        self.stdout = sys.stdout
        sys.stdout = self.out_file
        return self.out_file

    def __exit__(self, ty, val, tb):
        sys.stdout = self.stdout
```

Vamos detalhar o que este gerenciador de contexto faz:

1. `__init__`: Este é o método de inicialização. Quando criamos uma instância da classe `redirect_stdout`, passamos um objeto de arquivo. Este método armazena esse objeto de arquivo na variável de instância `self.out_file`. Portanto, ele lembra para onde queremos redirecionar a saída.
2. `__enter__`:
   - Primeiro, ele salva o `sys.stdout` atual. Isso é importante porque precisamos restaurá-lo mais tarde.
   - Em seguida, ele substitui o `sys.stdout` atual pelo nosso objeto de arquivo. A partir deste ponto, qualquer saída que normalmente iria para o console irá para o arquivo.
   - Finalmente, ele retorna o objeto de arquivo. Isso é útil porque podemos querer usar o objeto de arquivo dentro do bloco `with`.
3. `__exit__`:
   - Este método restaura o `sys.stdout` original. Portanto, após o bloco `with` ser finalizado, a saída voltará para o console como normal.
   - Ele recebe três parâmetros: tipo de exceção (`ty`), valor da exceção (`val`) e traceback (`tb`). Esses parâmetros são exigidos pelo protocolo do gerenciador de contexto. Eles são usados para lidar com quaisquer exceções que possam ocorrer dentro do bloco `with`.

Agora, vamos testar nosso gerenciador de contexto. Vamos usá-lo para redirecionar a saída de uma tabela para um arquivo. Primeiro, inicie o interpretador Python:

```bash
python3
```

Em seguida, execute o seguinte código Python no interpretador:

```python
>>> import stock, reader, tableformat
>>> from redirect import redirect_stdout
>>> portfolio = reader.read_csv_as_instances('portfolio.csv', stock.Stock)
>>> formatter = tableformat.create_formatter('text')
>>> with redirect_stdout(open('out.txt', 'w')) as file:
...     tableformat.print_table(portfolio, ['name','shares','price'], formatter)
...     file.close()
...
>>> # Let's check the content of the output file
>>> print(open('out.txt').read())
      name     shares      price
---------- ---------- ----------
        AA        100       32.2
       IBM         50       91.1
       CAT        150      83.44
      MSFT        200      51.23
        GE         95      40.37
      MSFT         50       65.1
       IBM        100      70.44
```

Ótimo! Nosso gerenciador de contexto funcionou como esperado. Ele redirecionou com sucesso a saída da tabela para o arquivo `out.txt`.

Os gerenciadores de contexto são um recurso muito poderoso em Python. Eles ajudam você a gerenciar recursos adequadamente. Aqui estão alguns casos de uso comuns para gerenciadores de contexto:

- Operações de arquivo: Quando você abre um arquivo, um gerenciador de contexto pode garantir que o arquivo seja fechado corretamente, mesmo que ocorra um erro.
- Conexões de banco de dados: Ele pode garantir que a conexão do banco de dados seja fechada depois que você terminar de usá-la.
- Locks em programas encadeados: Os gerenciadores de contexto podem lidar com o bloqueio e desbloqueio de recursos de forma segura.
- Alterar temporariamente as configurações do ambiente: Você pode alterar algumas configurações para um bloco de código e, em seguida, restaurá-las automaticamente.

Este padrão é muito importante porque garante que os recursos sejam limpos adequadamente, mesmo que ocorra uma exceção dentro do bloco `with`.

Quando terminar de testar, você pode sair do interpretador Python:

```python
>>> exit()
```
