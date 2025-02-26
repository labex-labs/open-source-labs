# Crea tu primera metaclase

Crea un archivo llamado `mymeta.py` y pon el siguiente código en él (de las diapositivas):

```python
# mymeta.py

class mytype(type):
    @staticmethod
    def __new__(meta, name, bases, __dict__):
        print("Creating class :", name)
        print("Base classes   :", bases)
        print("Attributes     :", list(__dict__))
        return super().__new__(meta, name, bases, __dict__)

class myobject(metaclass=mytype):
    pass
```

Una vez que hayas hecho esto, define una clase que herede de `myobject` en lugar de object. Por ejemplo:

```python
class Stock(myobject):
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
    def cost(self):
        return self.shares * self.price
    def sell(self, nshares):
        self.shares -= nshares
```

Intenta ejecutar tu código y crear instancias de `Stock`. Observa lo que sucede. Deberías ver las declaraciones de impresión de tu `mytype` ejecutándose una vez cuando se define la clase `Stock`.

¿Qué pasa si heredas de `Stock`?

```python
class MyStock(Stock):
    pass
```

Deberías seguir viendo tu metaclase en acción. Las metaclases son "pegajosas" en el sentido de que se aplican a lo largo de toda una jerarquía de herencia.

**Discusión**

¿Por qué quisieras hacer algo así? El principal poder de una metaclase es que le da a un programador la capacidad de capturar detalles sobre las clases justo antes de su creación. Por ejemplo, en el método `__new__()`, se te dan todos los detalles básicos, incluyendo el nombre de la clase, las clases base y los datos de los métodos. Si inspeccionas estos datos, puedes realizar varios tipos de comprobaciones de diagnóstico. Si eres más atrevido, puedes modificar los datos y cambiar lo que se coloca en la definición de la clase cuando se crea. No hace falta decir que hay muchas oportunidades para el horrible mal diabólico.
