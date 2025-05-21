# Compreendendo a Complexidade da Importação de Pacotes

Ao começar a trabalhar com pacotes Python, você perceberá rapidamente que importar módulos pode se tornar bastante complicado e prolixo. Essa complexidade pode tornar seu código mais difícil de ler e escrever. Neste laboratório, analisaremos de perto essa questão e aprenderemos como simplificar o processo de importação.

## Estrutura de Importação Atual

Primeiro, vamos abrir o terminal. O terminal é uma ferramenta poderosa que permite interagir com o sistema operacional do seu computador. Depois que o terminal estiver aberto, precisamos navegar até o diretório do projeto. O diretório do projeto é onde todos os arquivos relacionados ao nosso projeto Python são armazenados. Para fazer isso, usaremos o comando `cd`, que significa "change directory" (mudar diretório).

```bash
cd ~/project
```

Agora que estamos no diretório do projeto, vamos examinar a estrutura atual do pacote `structly`. Um pacote em Python é uma maneira de organizar módulos relacionados. Podemos usar o comando `ls -la` para listar todos os arquivos e diretórios dentro do pacote `structly`, incluindo arquivos ocultos.

```bash
ls -la structly
```

Você notará que existem vários módulos Python dentro do pacote `structly`. Esses módulos contêm funções e classes que podemos usar em nosso código. No entanto, se quisermos usar a funcionalidade desses módulos, atualmente precisamos usar instruções de importação longas. Por exemplo:

```python
from structly.structure import Structure
from structly.reader import read_csv_as_instances
from structly.tableformat import create_formatter, print_table
```

Esses caminhos de importação longos podem ser problemáticos de escrever, especialmente se você precisar usá-los várias vezes em seu código. Eles também tornam seu código menos legível, o que pode ser um problema quando você está tentando entender ou depurar seu código. Neste laboratório, aprenderemos como organizar o pacote de uma forma que simplifique essas importações.

Vamos começar olhando o conteúdo do arquivo `__init__.py` do pacote. O arquivo `__init__.py` é um arquivo especial em pacotes Python. Ele é executado quando o pacote é importado e pode ser usado para inicializar o pacote e configurar quaisquer importações necessárias.

```bash
cat structly/__init__.py
```

Você provavelmente descobrirá que o arquivo `__init__.py` está vazio ou contém muito pouco código. Nos próximos passos, modificaremos este arquivo para simplificar nossas instruções de importação.

## O Objetivo

Ao final deste laboratório, nosso objetivo é poder usar instruções de importação muito mais simples. Em vez dos longos caminhos de importação que vimos anteriormente, poderemos usar instruções como:

```python
from structly import Structure, read_csv_as_instances, create_formatter, print_table
```

Ou mesmo:

```python
from structly import *
```

Usar essas instruções de importação mais simples tornará nosso código mais limpo e fácil de trabalhar. Também nos economizará tempo e esforço ao escrever e manter nosso código.
