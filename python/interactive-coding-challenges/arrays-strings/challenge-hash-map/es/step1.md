# Tabla Hash

## Problema

Implementar una tabla hash con métodos de inserción, búsqueda y eliminación. La tabla hash debe utilizar encadenamiento para la resolución de colisiones. Las claves son solo enteros. No tenemos que preocuparnos por los factores de carga ni validar las entradas. Podemos asumir que la tabla hash cabe en memoria.

## Requisitos

- Las claves son solo enteros.
- Se utiliza encadenamiento para la resolución de colisiones.
- No es necesario considerar los factores de carga.
- No es necesario validar las entradas.
- La tabla hash cabe en memoria.

## Uso de ejemplo

- Método `get`:
  - Si no hay una clave coincidente, se lanza una excepción KeyError.
  - Si hay una clave coincidente, se devuelve el valor correspondiente.
- Método `set`:
  - Si no hay una clave coincidente, se agrega un nuevo par clave-valor a la tabla hash.
  - Si hay una clave coincidente, se actualiza el valor correspondiente.
- Método `remove`:
  - Si no hay una clave coincidente, se lanza una excepción KeyError.
  - Si hay una clave coincidente, el par clave-valor correspondiente se elimina de la tabla hash.
