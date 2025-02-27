# Comenzando Rutas Relativas con super

Podemos construir rutas relativas que empiecen en el módulo padre, en lugar del módulo actual o la raíz del crat, usando `super` al principio de la ruta. Esto es como comenzar una ruta de sistema de archivos con la sintaxis `..`. Usar `super` nos permite referirnos a un elemento que sabemos que está en el módulo padre, lo que puede facilitar la reorganización del árbol de módulos cuando el módulo está estrechamente relacionado con el padre pero el padre podría ser movido a otro lugar en el árbol de módulos algún día.

Considere el código de la Lista 7-8 que modela la situación en la que un chef corrige una orden incorrecta y la lleva personalmente al cliente. La función `fix_incorrect_order` definida en el módulo `back_of_house` llama a la función `deliver_order` definida en el módulo padre especificando la ruta a `deliver_order`, comenzando con `super`.

Nombre del archivo: `src/lib.rs`

```rust
fn deliver_order() {}

mod back_of_house {
    fn fix_incorrect_order() {
        cook_order();
        super::deliver_order();
    }

    fn cook_order() {}
}
```

Lista 7-8: Llamando a una función usando una ruta relativa que comienza con `super`

La función `fix_incorrect_order` está en el módulo `back_of_house`, por lo que podemos usar `super` para ir al módulo padre de `back_of_house`, que en este caso es `crate`, la raíz. A partir de ahí, buscamos `deliver_order` y lo encontramos. ¡Éxito! Pensamos que el módulo `back_of_house` y la función `deliver_order` probablemente permanecerán en la misma relación y se moverán juntos si decidimos reorganizar el árbol de módulos del crat. Por lo tanto, usamos `super` para tener menos lugares donde actualizar el código en el futuro si este código se mueve a un módulo diferente.
