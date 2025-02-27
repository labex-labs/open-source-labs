# Desestructuración de structs y tuplas

Podemos mezclar, combinar y anidar patrones de desestructuración de maneras aún más complejas. El siguiente ejemplo muestra una desestructuración complicada donde anidamos structs y tuplas dentro de una tupla y desestructuramos todos los valores primitivos:

```rust
let ((feet, inches), Point { x, y }) =
    ((3, 10), Point { x: 3, y: -10 });
```

Este código nos permite descomponer tipos complejos en sus partes componentes para que podamos usar por separado los valores en los que estamos interesados.

La desestructuración con patrones es una forma conveniente de usar fragmentos de valores, como el valor de cada campo en un struct, de forma independiente los unos de los otros.
