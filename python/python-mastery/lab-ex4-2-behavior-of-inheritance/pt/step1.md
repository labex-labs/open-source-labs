# Compreendendo Herança Simples e Múltipla

Nesta etapa, aprenderemos sobre os dois principais tipos de herança em Python: herança simples e herança múltipla. Herança é um conceito fundamental na programação orientada a objetos que permite que uma classe herde atributos e métodos de outras classes. Também veremos como o Python determina qual método chamar quando há vários candidatos, um processo conhecido como resolução de método.

## Herança Simples

Herança simples é quando as classes formam uma única linha de ancestralidade. Pense nisso como uma árvore genealógica onde cada classe tem apenas um pai direto. Vamos criar um exemplo para entender como funciona.

Primeiro, abra um novo terminal no WebIDE. Depois que o terminal estiver aberto, inicie o interpretador Python digitando o seguinte comando e pressionando Enter:

```bash
python3
```

Agora que você está no interpretador Python, criaremos três classes que formam uma única cadeia de herança. Digite o seguinte código:

```python
class A:
    def spam(self):
        print('A.spam')

class B(A):
    def spam(self):
        print('B.spam')
        super().spam()

class C(B):
    def spam(self):
        print('C.spam')
        super().spam()
```

Neste código, a classe `B` herda da classe `A`, e a classe `C` herda da classe `B`. A função `super()` é usada para chamar o método da classe pai.

Depois de definir essas classes, podemos descobrir a ordem em que o Python procura por métodos. Essa ordem é chamada de Ordem de Resolução de Método (MRO - _Method Resolution Order_). Para ver o MRO da classe `C`, digite o seguinte código:

```python
C.__mro__
```

Você deve ver uma saída semelhante a esta:

```
(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
```

Esta saída mostra que o Python primeiro procura um método na classe `C`, depois na classe `B`, depois na classe `A` e, finalmente, na classe base `object`.

Agora, vamos criar uma instância da classe `C` e chamar seu método `spam()`. Digite o seguinte código:

```python
c = C()
c.spam()
```

Você deve ver a seguinte saída:

```
C.spam
B.spam
A.spam
```

Esta saída demonstra como `super()` funciona em uma cadeia de herança simples. Quando `C.spam()` chama `super().spam()`, ele chama `B.spam()`. Então, quando `B.spam()` chama `super().spam()`, ele chama `A.spam()`.

## Herança Múltipla

Herança múltipla permite que uma classe herde de mais de uma classe pai. Isso dá a uma classe acesso aos atributos e métodos de todas as suas classes pai. Vamos ver como a resolução de método funciona neste caso.

Digite o seguinte código no seu interpretador Python:

```python
class Base:
    def spam(self):
        print('Base.spam')

class X(Base):
    def spam(self):
        print('X.spam')
        super().spam()

class Y(Base):
    def spam(self):
        print('Y.spam')
        super().spam()

class Z(Base):
    def spam(self):
        print('Z.spam')
        super().spam()
```

Agora, criaremos uma classe `M` que herda de várias classes pai `X`, `Y` e `Z`. Digite o seguinte código:

```python
class M(X, Y, Z):
    pass

M.__mro__
```

Você deve ver a seguinte saída:

```
(<class '__main__.M'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class '__main__.Base'>, <class 'object'>)
```

Esta saída mostra a Ordem de Resolução de Método para a classe `M`. O Python procurará por métodos nesta ordem.

Vamos criar uma instância da classe `M` e chamar seu método `spam()`:

```python
m = M()
m.spam()
```

Você deve ver a seguinte saída:

```
X.spam
Y.spam
Z.spam
Base.spam
```

Observe que `super()` não apenas chama o método da classe pai imediata. Em vez disso, ele segue a Ordem de Resolução de Método (MRO) definida pela classe filha.

Vamos criar outra classe `N` com as classes pai em uma ordem diferente:

```python
class N(Z, Y, X):
    pass

N.__mro__
```

Você deve ver a seguinte saída:

```
(<class '__main__.N'>, <class '__main__.Z'>, <class '__main__.Y'>, <class '__main__.X'>, <class '__main__.Base'>, <class 'object'>)
```

Agora, crie uma instância da classe `N` e chame seu método `spam()`:

```python
n = N()
n.spam()
```

Você deve ver a seguinte saída:

```
Z.spam
Y.spam
X.spam
Base.spam
```

Isso mostra um conceito importante: na herança múltipla do Python, a ordem das classes pai na definição da classe determina a Ordem de Resolução de Método. A função `super()` segue esta ordem, não importa de qual classe ela é chamada.

Quando terminar de explorar esses conceitos, você pode sair do interpretador Python digitando o seguinte código:

```python
exit()
```
