# Min Heap

## Problema

Implementa un min heap con los siguientes métodos:

- `extract_min()`: elimina y devuelve el valor mínimo en el heap
- `insert(value)`: inserta un nuevo valor en el heap mientras mantiene la propiedad de heap

## Requisitos

La implementación debe cumplir con los siguientes requisitos:

- Las entradas son enteros
- La implementación debe caber en memoria

## Uso de ejemplo

Considera el siguiente min heap:

```txt
          _5_
        /     \
       20     15
      / \    /  \
     22  40 25
```

- `extract_min()`: elimina y devuelve el valor mínimo en el heap, que es 5. El heap resultante es:

```txt
          _15_
        /      \
       20      25
      / \     /  \
     22  40
```

- `insert(2)`: inserta el valor 2 en el heap mientras mantiene la propiedad de heap. El heap resultante es:

```txt
          _2_
        /     \
       20      5
      / \     / \
     22  40  25  15
```
