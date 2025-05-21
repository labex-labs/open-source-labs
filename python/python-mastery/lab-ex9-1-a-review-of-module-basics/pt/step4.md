# Usando a Sintaxe `from module import`

Em Python, existem várias maneiras de importar componentes de módulos. Uma dessas maneiras é a sintaxe `from module import`, que exploraremos nesta seção.

Ao importar componentes de um módulo, geralmente é uma boa ideia começar com uma tela limpa. Isso garante que não haja variáveis ou configurações residuais de interações anteriores que possam interferir em nosso experimento atual.

1. Reinicie o interpretador Python para obter um estado limpo:

```python
>>> exit()
```

Este comando sai da sessão atual do interpretador Python. Depois de sair, iniciaremos uma nova sessão para garantir um ambiente limpo.

```bash
python3
```

Este comando bash inicia uma nova sessão do interpretador Python 3. Agora que temos um ambiente Python limpo, podemos começar a importar componentes de um módulo.

2. Importe componentes específicos de um módulo usando a sintaxe `from module import`:

```python
>>> from simplemod import foo
Loaded simplemod
>>> foo()
x is 42
```

Aqui, estamos usando a instrução `from simplemod import foo` para importar apenas a função `foo` do módulo `simplemod`. Observe que, embora tenhamos solicitado apenas a função `foo`, todo o módulo `simplemod` foi carregado. Isso é indicado pela saída "Loaded simplemod". A razão para isso é que o Python precisa carregar todo o módulo para acessar a função `foo`.

3. Ao usar `from module import`, você não pode acessar o próprio módulo:

```python
>>> simplemod.foo()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'simplemod' is not defined
```

Quando usamos a sintaxe `from module import`, estamos apenas trazendo os componentes especificados diretamente para nosso namespace. O próprio nome do módulo não é importado. Portanto, quando tentamos acessar `simplemod.foo()`, o Python não reconhece `simplemod` porque ele não foi importado dessa maneira.

4. Você pode importar vários componentes de uma vez:

```python
>>> from simplemod import x, foo
>>> x
42
>>> foo()
x is 42
```

A sintaxe `from module import` nos permite importar vários componentes de um módulo em uma única instrução. Aqui, estamos importando a variável `x` e a função `foo` do módulo `simplemod`. Após a importação, podemos acessar diretamente esses componentes em nosso código.

5. Ao importar uma variável de um módulo, você está criando uma nova referência ao objeto, não um link para a variável no módulo:

```python
>>> x = 13  # Change the local variable x
>>> x
13
>>> foo()
x is 42  # The function still uses the module's x, not your local x
```

Quando importamos uma variável de um módulo, estamos essencialmente criando uma nova referência ao mesmo objeto em nosso namespace local. Portanto, quando alteramos a variável local `x` para `13`, isso não afeta a variável `x` dentro do módulo `simplemod`. A função `foo()` ainda se refere à variável `x` do módulo, que é `42`. Entender esse conceito é crucial para evitar confusão em seu código.
