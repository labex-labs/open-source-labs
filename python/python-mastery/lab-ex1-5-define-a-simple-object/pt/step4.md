# Trabalhando com Múltiplos Objetos de Ações

Em programação orientada a objetos, uma classe é como um modelo, e as instâncias dessa classe são os objetos reais criados com base nesse modelo. Nossa classe `Stock` é um modelo para representar ações. Podemos criar múltiplas instâncias desta classe `Stock` para representar diferentes ações. Cada instância terá seu próprio conjunto de atributos, como o nome da ação, o número de ações e o preço por ação.

1. Com a sessão interativa do Python ainda em execução, vamos criar outro objeto `Stock`. Desta vez, ele representará a IBM. Para criar uma instância da classe `Stock`, chamamos o nome da classe como se fosse uma função e passamos os argumentos necessários. Os argumentos aqui são o nome da ação, o número de ações e o preço por ação.

```python
t = Stock('IBM', 50, 91.5)
```

Nesta linha de código, estamos criando um novo objeto `Stock` chamado `t` que representa a IBM. Ele tem 50 ações, e cada ação custa $91,5.

2. Agora, queremos calcular o custo desta nova ação. A classe `Stock` tem um método chamado `cost()` que calcula o custo total da ação multiplicando o número de ações pelo preço por ação.

```python
t.cost()
```

Quando você executa este código, o Python chamará o método `cost()` no objeto `t` e retornará o custo total.

Saída:

```
4575.0
```

3. Podemos formatar e exibir nossas informações de ações de uma maneira agradável e organizada usando a formatação de strings do Python. A formatação de strings nos permite especificar como diferentes tipos de dados devem ser apresentados em uma string.

```python
print('%10s %10d %10.2f' % (s.name, s.shares, s.price))
```

Neste código, estamos usando a formatação de strings de estilo antigo no Python. O operador `%` é usado para substituir valores em um modelo de string. O modelo de string `'%10s %10d %10.2f'` define como o nome da ação, o número de ações e o preço devem ser formatados.

Saída:

```
      GOOG        100     490.10
```

Esta string formatada funciona da seguinte forma:

- `%10s` formata uma string em um campo com 10 caracteres de largura (alinhado à direita). Isso significa que o nome da ação será colocado em um espaço que tem 10 caracteres de largura, e será alinhado à direita dentro desse espaço.
- `%10d` formata um inteiro em um campo com 10 caracteres de largura. Portanto, o número de ações será colocado em um espaço com 10 caracteres de largura.
- `%10.2f` formata um float com 2 casas decimais em um campo com 10 caracteres de largura. O preço será mostrado com duas casas decimais e colocado em um espaço com 10 caracteres de largura.

4. Agora, vamos formatar as informações da ação da IBM da mesma maneira. Só precisamos substituir o nome do objeto de `s` para `t` no código de formatação de string.

```python
print('%10s %10d %10.2f' % (t.name, t.shares, t.price))
```

Saída:

```
       IBM         50      91.50
```

5. No Python moderno, também podemos usar f-strings para formatação. F-strings são mais legíveis e fáceis de usar. Vamos comparar os custos de ambas as ações usando f-strings.

```python
print(f"Google stock costs ${s.cost()}, IBM stock costs ${t.cost()}")
```

Nesta f-string, estamos incorporando diretamente expressões dentro de chaves `{}`. O Python avaliará essas expressões e inserirá os resultados na string.

Saída:

```
Google stock costs $49010.0, IBM stock costs $4575.0
```

6. Quando você terminar de experimentar, é hora de sair do modo interativo do Python. Você pode fazer isso usando a função `exit()`.

```python
exit()
```

Cada objeto Stock mantém seu próprio conjunto de atributos, o que demonstra como as instâncias de classe funcionam em programação orientada a objetos. Isso nos permite criar múltiplos objetos de ações, cada um com valores diferentes, enquanto compartilha os mesmos métodos.
