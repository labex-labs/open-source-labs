# Comprendiendo la Herencia Simple y Múltiple

En este paso, aprenderemos sobre los dos tipos principales de herencia en Python: herencia simple y herencia múltiple. La herencia es un concepto fundamental en la programación orientada a objetos que permite a una clase heredar atributos y métodos de otras clases. También veremos cómo Python determina qué método llamar cuando hay múltiples candidatos, un proceso conocido como resolución de métodos.

## Herencia Simple

La herencia simple ocurre cuando las clases forman una sola línea de ascendencia. Puedes pensar en ello como en un árbol genealógico donde cada clase tiene solo un padre directo. Vamos a crear un ejemplo para entender cómo funciona.

Primero, abre una nueva terminal en el WebIDE. Una vez abierta la terminal, inicia el intérprete de Python escribiendo el siguiente comando y luego presionando Enter:

```bash
python3
```

Ahora que estás en el intérprete de Python, crearemos tres clases que formen una cadena de herencia simple. Ingresa el siguiente código:

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

En este código, la clase `B` hereda de la clase `A`, y la clase `C` hereda de la clase `B`. La función `super()` se utiliza para llamar al método de la clase padre.

Después de definir estas clases, podemos averiguar el orden en el que Python busca los métodos. Este orden se llama Orden de Resolución de Métodos (Method Resolution Order, MRO). Para ver el MRO de la clase `C`, escribe el siguiente código:

```python
C.__mro__
```

Deberías ver una salida similar a esta:

```
(<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
```

Esta salida muestra que Python busca primero un método en la clase `C`, luego en la clase `B`, luego en la clase `A` y, finalmente, en la clase base `object`.

Ahora, creemos una instancia de la clase `C` y llamemos a su método `spam()`. Escribe el siguiente código:

```python
c = C()
c.spam()
```

Deberías ver la siguiente salida:

```
C.spam
B.spam
A.spam
```

Esta salida demuestra cómo funciona `super()` en una cadena de herencia simple. Cuando `C.spam()` llama a `super().spam()`, llama a `B.spam()`. Luego, cuando `B.spam()` llama a `super().spam()`, llama a `A.spam()`.

## Herencia Múltiple

La herencia múltiple permite que una clase herede de más de una clase padre. Esto da a una clase acceso a los atributos y métodos de todas sus clases padre. Veamos cómo funciona la resolución de métodos en este caso.

Ingresa el siguiente código en tu intérprete de Python:

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

Ahora, crearemos una clase `M` que herede de múltiples clases padre `X`, `Y` y `Z`. Ingresa el siguiente código:

```python
class M(X, Y, Z):
    pass

M.__mro__
```

Deberías ver la siguiente salida:

```
(<class '__main__.M'>, <class '__main__.X'>, <class '__main__.Y'>, <class '__main__.Z'>, <class '__main__.Base'>, <class 'object'>)
```

Esta salida muestra el Orden de Resolución de Métodos para la clase `M`. Python buscará métodos en este orden.

Creemos una instancia de la clase `M` y llamemos a su método `spam()`:

```python
m = M()
m.spam()
```

Deberías ver la siguiente salida:

```
X.spam
Y.spam
Z.spam
Base.spam
```

Observa que `super()` no solo llama al método de la clase padre inmediata. En lugar de eso, sigue el Orden de Resolución de Métodos (MRO) definido por la clase hija.

Creemos otra clase `N` con las clases padre en un orden diferente:

```python
class N(Z, Y, X):
    pass

N.__mro__
```

Deberías ver la siguiente salida:

```
(<class '__main__.N'>, <class '__main__.Z'>, <class '__main__.Y'>, <class '__main__.X'>, <class '__main__.Base'>, <class 'object'>)
```

Ahora, crea una instancia de la clase `N` y llama a su método `spam()`:

```python
n = N()
n.spam()
```

Deberías ver la siguiente salida:

```
Z.spam
Y.spam
X.spam
Base.spam
```

Esto muestra un concepto importante: en la herencia múltiple de Python, el orden de las clases padre en la definición de la clase determina el Orden de Resolución de Métodos. La función `super()` sigue este orden sin importar desde qué clase se llame.

Cuando hayas terminado de explorar estos conceptos, puedes salir del intérprete de Python escribiendo el siguiente código:

```python
exit()
```
