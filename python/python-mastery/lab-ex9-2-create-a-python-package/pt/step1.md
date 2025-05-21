# Entendendo Pacotes Python

Antes de começarmos a criar um pacote Python, vamos entender o que é um pacote Python. Um pacote Python é essencialmente um diretório. Dentro deste diretório, existem múltiplos arquivos de módulo Python, que são apenas arquivos `.py` contendo código Python. Adicionalmente, existe um arquivo especial chamado `__init__.py`. Este arquivo pode estar vazio, mas sua presença indica que o diretório é um pacote Python. O propósito desta estrutura é ajudá-lo a organizar código relacionado em uma única hierarquia de diretórios.

Pacotes oferecem diversos benefícios. Primeiro, eles permitem que você estruture seu código logicamente. Em vez de ter todos os seus arquivos Python espalhados, você pode agrupar funcionalidades relacionadas em um pacote. Segundo, eles ajudam a evitar conflitos de nomes entre módulos. Uma vez que pacotes criam um namespace, você pode ter módulos com o mesmo nome em pacotes diferentes sem nenhum problema. Terceiro, eles tornam a importação e o uso do seu código mais convenientes. Você pode importar um pacote inteiro ou módulos específicos dele com facilidade.

Agora, vamos dar uma olhada nos arquivos que temos atualmente em nosso diretório de projeto. Para listar os arquivos, usaremos o seguinte comando no terminal:

```bash
ls -l
```

Quando você executar este comando, deverá ver os seguintes arquivos:

```
portfolio.csv
reader.py
stock.py
structure.py
tableformat.py
validate.py
```

Estes arquivos Python estão todos relacionados e trabalham juntos, mas atualmente, eles são apenas módulos separados. Neste laboratório, nosso objetivo é organizá-los em um pacote coeso chamado `structly`.

Vamos entender brevemente o que cada arquivo faz:

- `structure.py`: Este arquivo define uma classe base `Structure` e vários descritores. Estes descritores são usados para validação de tipo, o que significa que eles ajudam a garantir que os dados usados em seu programa tenham o tipo correto.
- `validate.py`: Ele contém funcionalidades de validação que são usadas pelo módulo `structure`. Isso ajuda na validação dos dados de acordo com certas regras.
- `reader.py`: Este arquivo fornece funções que são usadas para ler dados CSV. CSV (Valores Separados por Vírgula) é um formato de arquivo comum para armazenar dados tabulares.
- `tableformat.py`: Ele contém classes e funções que são usadas para formatar dados em tabelas. Isso é útil quando você deseja exibir dados de uma maneira mais organizada.
- `stock.py`: Este arquivo usa os outros módulos para definir uma classe `Stock` e processar dados de ações. Ele combina a funcionalidade dos outros módulos para realizar tarefas específicas relacionadas a dados de ações.

No próximo passo, criaremos nossa estrutura de pacote.
