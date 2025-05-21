# Lidando com Exceções em Geradores

Nesta etapa, vamos aprender como lidar com exceções em geradores e corrotinas. Mas, primeiro, vamos entender o que são exceções. Uma exceção é um evento que ocorre durante a execução de um programa e interrompe o fluxo normal das instruções do programa. Em Python, podemos usar o método `throw()` para lidar com exceções em geradores e corrotinas.

## Compreendendo Corrotinas

Uma corrotina é um tipo especial de gerador. Ao contrário dos geradores regulares que principalmente produzem valores, as corrotinas podem consumir valores (usando o método `send()`) e produzir valores. O arquivo `cofollow.py` tem uma implementação simples de uma corrotina.

Vamos abrir o arquivo `cofollow.py` no editor WebIDE. Aqui está o código dentro:

```python
def consumer(func):
    def start(*args,**kwargs):
        c = func(*args,**kwargs)
        next(c)
        return c
    return start

@consumer
def printer():
    while True:
        item = yield
        print(item)
```

Agora, vamos analisar este código. O `consumer` é um decorador. Um decorador é uma função que recebe outra função como argumento, adiciona alguma funcionalidade a ela e, em seguida, retorna a função modificada. Neste caso, o decorador `consumer` move automaticamente o gerador para sua primeira instrução `yield`. Isso é importante porque torna o gerador pronto para receber valores.

A corrotina `printer()` é definida com o decorador `@consumer`. Dentro da função `printer()`, temos um loop `while` infinito. A instrução `item = yield` é onde a mágica acontece. Ela pausa a execução da corrotina e espera receber um valor. Quando um valor é enviado para a corrotina, ela retoma a execução e imprime o valor recebido.

## Adicionando Tratamento de Exceções à Corrotina

Agora, vamos modificar a corrotina `printer()` para lidar com exceções. Vamos atualizar a função `printer()` em `cofollow.py` assim:

```python
@consumer
def printer():
    while True:
        try:
            item = yield
            print(item)
        except Exception as e:
            print('ERROR: %r' % e)
```

O bloco `try` contém o código que pode lançar uma exceção. Em nosso caso, é o código que recebe e imprime o valor. Se uma exceção ocorrer no bloco `try`, a execução salta para o bloco `except`. O bloco `except` captura a exceção e imprime uma mensagem de erro. Após fazer essas alterações, salve o arquivo.

## Experimentando com Tratamento de Exceções em Corrotinas

Vamos começar a experimentar o lançamento de exceções na corrotina. Abra um terminal e execute o interpretador Python usando os seguintes comandos:

```bash
cd ~/project
python3
```

### Experimento 1: Uso Básico de Corrotina

```python
>>> from cofollow import printer
>>> p = printer()
>>> p.send('hello')  # Send a value to the coroutine
hello
>>> p.send(42)  # Send another value
42
```

Aqui, primeiro importamos a corrotina `printer` do módulo `cofollow`. Em seguida, criamos uma instância da corrotina `printer` chamada `p`. Usamos o método `send()` para enviar valores para a corrotina. Como você pode ver, a corrotina processa os valores que enviamos para ela sem problemas.

### Experimento 2: Lançando uma Exceção na Corrotina

```python
>>> p.throw(ValueError('It failed'))  # Throw an exception into the coroutine
ERROR: ValueError('It failed')
```

Neste experimento, usamos o método `throw()` para injetar uma exceção `ValueError` na corrotina. O bloco `try-except` na corrotina `printer()` captura a exceção e imprime uma mensagem de erro. Isso mostra que nosso tratamento de exceção está funcionando como esperado.

### Experimento 3: Lançando uma Exceção Real na Corrotina

```python
>>> try:
...     int('n/a')  # This will raise a ValueError
... except ValueError as e:
...     p.throw(e)  # Throw the caught exception into the coroutine
...
ERROR: ValueError("invalid literal for int() with base 10: 'n/a'")
```

Aqui, primeiro tentamos converter a string `'n/a'` em um inteiro, o que lança um `ValueError`. Capturamos essa exceção e, em seguida, usamos o método `throw()` para passá-la para a corrotina. A corrotina captura a exceção e imprime a mensagem de erro.

### Experimento 4: Verificando se a Corrotina Continua em Execução

```python
>>> p.send('still working')  # The coroutine continues to run after handling exceptions
still working
```

Após lidar com as exceções, enviamos outro valor para a corrotina usando o método `send()`. A corrotina ainda está ativa e pode processar o novo valor. Isso mostra que nossa corrotina pode continuar em execução mesmo após encontrar erros.

## Principais Conclusões

1. Geradores e corrotinas podem lidar com exceções no ponto da instrução `yield`. Isso significa que podemos capturar e lidar com erros que ocorrem quando a corrotina está esperando ou processando um valor.
2. O método `throw()` permite que você injete exceções em um gerador ou corrotina. Isso é útil para testes e para lidar com erros que ocorrem fora da corrotina.
3. Lidar adequadamente com exceções em geradores permite que você crie geradores robustos e tolerantes a erros que podem continuar em execução mesmo quando ocorrem erros. Isso torna seu código mais confiável e fácil de manter.

Para sair do interpretador Python, você pode digitar `exit()` ou pressionar `Ctrl+D`.
