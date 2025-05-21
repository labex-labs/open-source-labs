# Importando e Usando Módulos

Agora que criamos um módulo, é hora de entender como importá-lo e usar seus componentes. Em Python, um módulo é um arquivo que contém definições e instruções Python. Quando você importa um módulo, você ganha acesso a todas as funções, classes e variáveis definidas nele. Isso permite que você reutilize código e organize seus programas de forma mais eficaz.

1. Primeiro, precisamos abrir um novo terminal no WebIDE. Este terminal servirá como nosso espaço de trabalho onde podemos executar comandos Python. Para abrir um novo terminal, clique em "Terminal" > "New Terminal".

2. Depois que o terminal estiver aberto, precisamos iniciar o interpretador Python. O interpretador Python é um programa que lê e executa código Python. Para iniciá-lo, digite o seguinte comando no terminal e pressione Enter:

```bash
python3
```

3. Agora que o interpretador Python está em execução, podemos importar nosso módulo. Em Python, usamos a instrução `import` para trazer um módulo para nosso programa atual. Digite o seguinte comando no interpretador Python:

```python
>>> import simplemod
Loaded simplemod
```

Você notará que "Loaded simplemod" aparece na saída. Isso ocorre porque a instrução `print` em nosso módulo `simplemod` é executada quando o módulo é carregado. Quando o Python importa um módulo, ele executa todo o código de nível superior nesse módulo, incluindo quaisquer instruções `print`.

4. Depois de importar o módulo, podemos acessar seus componentes usando a notação de ponto. A notação de ponto é uma maneira de acessar atributos (variáveis e funções) de um objeto em Python. Neste caso, o módulo é um objeto, e suas funções, variáveis e classes são seus atributos. Aqui estão alguns exemplos de como acessar diferentes componentes do módulo `simplemod`:

```python
>>> simplemod.x
42
>>> simplemod.foo()
x is 42
>>> spam_instance = simplemod.Spam()
>>> spam_instance.yow()
Yow!
```

Na primeira linha, acessamos a variável `x` definida no módulo `simplemod`. Na segunda linha, chamamos a função `foo` do módulo `simplemod`. Nas terceira e quarta linhas, criamos uma instância da classe `Spam` definida no módulo `simplemod` e chamamos seu método `yow`.

5. Às vezes, você pode encontrar um `ImportError` ao tentar importar um módulo. Este erro ocorre quando o Python não consegue encontrar o módulo que você está tentando importar. Para descobrir onde o Python está procurando módulos, você pode examinar a variável `sys.path`. A variável `sys.path` é uma lista de diretórios que o Python pesquisa ao procurar módulos. Digite os seguintes comandos no interpretador Python:

```python
>>> import sys
>>> sys.path
['', '/usr/lib/python310.zip', '/usr/lib/python3.10', '/usr/lib/python3.10/lib-dynload', '/usr/local/lib/python3.10/dist-packages', '/usr/lib/python3/dist-packages']
```

O primeiro elemento da lista (a string vazia) representa o diretório de trabalho atual. É aqui que o Python procura o arquivo `simplemod.py`. Se seu módulo não estiver em um dos diretórios listados em `sys.path`, o Python não conseguirá encontrá-lo e você receberá um `ImportError`. Certifique-se de que seu arquivo `simplemod.py` esteja no diretório de trabalho atual ou em um dos outros diretórios em `sys.path`.
