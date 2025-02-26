# División de Módulos

El archivo `structly/tableformat.py` contiene código para crear tablas en diferentes formatos. Específicamente:

- Una clase base `TableFormatter`.
- Una clase `TextTableFormatter`.
- Una clase `CSVTableFormatter`.
- Una clase `HTMLTableFormatter`.

En lugar de tener todas estas clases en un solo archivo `.py`, quizás tenga sentido mover cada formateador concreto a su propio archivo. Para hacer esto, vamos a dividir el archivo `tableformat.py` en partes. Siga estas instrucciones con cuidado:

Primero, elimina el directorio `structly/__pycache__`.

    % cd structly
    % rm -rf __pycache__

Luego, crea el directorio `structly/tableformat`. Este directorio debe tener exactamente el mismo nombre que el módulo que está reemplazando (`tableformat.py`).

```bash
mkdir tableformat
```

Mueve el archivo `tableformat.py` original al nuevo directorio `tableformat` y cámbialo por `formatter.py`.

```bash
mv tableformat.py tableformat/formatter.py
```

En el directorio `tableformat`, divide el código de `tableformat.py` en los siguientes archivos y directorios:

- `formatter.py` - Contiene la clase base `TableFormatter`, mixines y varias funciones.
- `formats/text.py` - Contiene la clase `TextTableFormatter`.
- `formats/csv.py` - Contiene la clase `CSVTableFormatter`.
- `formats/html.py` - Contiene la clase `HTMLTableFormatter`.

Agrega un archivo `__init__.py` a los directorios `tableformat/` y `tableformat/formats`. Haz que el `tableformat/__init__.py` exporte los mismos símbolos que el archivo `tableformat.py` original exportó.

Después de haber hecho todos estos cambios, deberías tener una estructura de paquete que se vea así:

    structly/
          __init__.py
          validate.py
          reader.py
          structure.py
          tableformat/
               __init__.py
               formatter.py
               formats/
                   __init__.py
                   text.py
                   csv.py
                   html.py

Para los usuarios, todo debería funcionar exactamente como antes. Por ejemplo, tu archivo `stock.py` anterior debería funcionar:

```python
# stock.py

from structly import *

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares):
        self.shares -= nshares

if __name__ == '__main__':
    portfolio = read_csv_as_instances('portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
```
