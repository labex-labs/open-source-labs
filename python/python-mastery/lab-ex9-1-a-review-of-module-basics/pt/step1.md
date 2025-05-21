# Criando um Módulo Simples

Vamos começar nossa jornada nos módulos Python criando um simples. Em Python, um módulo é essencialmente um arquivo com a extensão `.py` que contém código Python. Pense nele como um contêiner onde você pode agrupar funções, classes e variáveis relacionadas. Isso torna seu código mais organizado e fácil de gerenciar, especialmente à medida que seus projetos crescem em tamanho.

1. Primeiro, abra o WebIDE. Depois de aberto, você precisará criar um novo arquivo. Para fazer isso, clique em "File" na barra de menu e selecione "New File". Nomeie este novo arquivo `simplemod.py` e salve-o no diretório `/home/labex/project`. Este diretório é onde manteremos todos os arquivos relacionados a este experimento.

2. Agora, vamos adicionar algum código ao nosso arquivo `simplemod.py` recém-criado. O código abaixo define alguns elementos básicos que você normalmente encontrará em um módulo Python.

```python
# simplemod.py

x = 42        # Uma variável global

# Uma função simples
def foo():
    print('x is', x)

# Uma classe simples
class Spam:
    def yow(self):
        print('Yow!')

# Uma instrução de script
print('Loaded simplemod')
```

Neste código:

- `x = 42` cria uma variável global chamada `x` e atribui a ela o valor `42`. Variáveis globais podem ser acessadas de qualquer lugar dentro do módulo.
- A função `foo()` é definida para imprimir o valor da variável global `x`. Funções são blocos de código reutilizáveis que executam uma tarefa específica.
- A classe `Spam` é um modelo para criar objetos. Ele tem um método chamado `yow()`, que simplesmente imprime a string 'Yow!'. Métodos são funções que pertencem a uma classe.
- A instrução `print('Loaded simplemod')` é uma instrução de script. Ela será executada assim que o módulo for carregado, o que nos ajuda a confirmar que o módulo foi carregado com sucesso.

3. Depois de adicionar o código, salve o arquivo. Você pode fazer isso pressionando `Ctrl+S` no seu teclado ou selecionando "File" > "Save" no menu. Salvar o arquivo garante que todas as alterações que você fez sejam preservadas.

Vamos dar uma olhada mais de perto no que este módulo contém:

- Uma variável global `x` com o valor `42`. Esta variável pode ser usada em todo o módulo e até mesmo acessada de outros módulos se importada corretamente.
- Uma função `foo()` que imprime o valor de `x`. Funções são úteis para executar tarefas repetitivas sem ter que escrever o mesmo código várias vezes.
- Uma classe `Spam` com um método `yow()`. Classes e métodos são conceitos fundamentais na programação orientada a objetos (object-oriented programming), que permite criar estruturas de dados e comportamentos complexos.
- Uma instrução `print` que é executada quando o módulo é carregado. Esta instrução serve como um indicador visual de que o módulo foi carregado com sucesso no ambiente Python.

A instrução `print` na parte inferior nos ajudará a observar quando o módulo é carregado, o que é importante para depurar e entender como os módulos funcionam em Python.
