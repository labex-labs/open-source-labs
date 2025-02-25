# Trie

## Problema

Su tarea es implementar un trie con los siguientes métodos:

- `find(word)` - devuelve `True` si la palabra dada está en el trie, `False` en caso contrario.
- `insert(word)` - inserta la palabra dada en el trie.
- `remove(word)` - elimina la palabra dada del trie.
- `list_words()` - devuelve una lista de todas las palabras en el trie que terminan con un carácter de terminación.

## Requisitos

Para completar este desafío, deben cumplirse los siguientes requisitos:

- La implementación debe funcionar con cadenas.
- Se asume que las cadenas están en ASCII.
- El método `find` solo debe coincidir con palabras exactas con un carácter de terminación.
- El método `list_words` solo debe devolver palabras con un carácter de terminación.
- Se asume que la implementación ajusta en memoria.

## Uso de ejemplo

Los siguientes ejemplos demuestran el uso de los métodos del trie:

```txt

         raíz
       /  |  \
      h   a*  m
     / \   \   \
    a   e*  t*  e*
   / \         / \
  s*  t*      n*  t*
             /
            s*

buscar

* Buscar en un trie vacío
* Buscar sin coincidencia
* Buscar con coincidencia

insertar

* Insertar en un trie vacío
* Insertar para crear un carácter de terminador de hoja
* Insertar para extender un carácter de terminador existente

eliminar

* Eliminar mí
* Eliminar mens
* Eliminar a
* Eliminar has

listar_palabras

* Listar vacío
* Listar caso general
```
