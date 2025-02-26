# Creando un paquete

En ejercicios anteriores, creó los siguientes archivos relacionados con estructuras con comprobación de tipos, lectura de datos y creación de tablas:

- `structure.py`
- `validate.py`
- `reader.py`
- `tableformat.py`

Su tarea es tomar todos estos archivos y moverlos a un paquete llamado `structly`. Para hacer eso, siga estos pasos:

- Cree un directorio llamado `structly`
- Cree un archivo vacío `__init__.py` y colóqueló en el directorio `structly`
- Mueva los archivos `structure.py`, `validate.py`, `reader.py` y `tableformat.py` al directorio `structly`.
- Corrija cualquier declaración de importación entre módulos (específicamente, el módulo `structure` depende de `validate`).

Una vez que haya hecho eso, modifique el programa `stock.py` para que se vea exactamente así y funcione:

```python
# stock.py

from structly.structure import Structure

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares

if __name__ == '__main__':
    from structly.reader import read_csv_as_instances
    from structly.tableformat import create_formatter, print_table
    portfolio = read_csv_as_instances('portfolio.csv', Stock)
    formatter = create_formatter('text')
    print_table(portfolio, ['name','shares','price'], formatter)
```
