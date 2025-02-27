# Datos solo en la pila: Copy

Hay otro detalle que no hemos mencionado todavía. Este código que utiliza enteros (parte del cual se mostró en la Lista 4-2) funciona y es válido:

```rust
let x = 5;
let y = x;

println!("x = {x}, y = {y}");
```

Pero este código parece contradecir lo que acabamos de aprender: no tenemos una llamada a `clone`, pero `x` sigue siendo válido y no se movió a `y`.

La razón es que tipos como los enteros, que tienen un tamaño conocido en tiempo de compilación, se almacenan enteramente en la pila, por lo que las copias de los valores reales se realizan rápidamente. Eso significa que no hay razón para evitar que `x` sea válido después de crear la variable `y`. En otras palabras, no hay diferencia entre una copia profunda y una copia superficial aquí, por lo que llamar a `clone` no haría nada diferente a la copia superficial habitual, y podemos omitirlo.

Rust tiene una anotación especial llamada el trato `Copy` que podemos colocar en tipos que se almacenan en la pila, como los enteros (hablaremos más sobre los tratados en el Capítulo 10). Si un tipo implementa el trato `Copy`, las variables que lo usan no se mueven, sino que se copian trivialmente, lo que las hace todavía válidas después de la asignación a otra variable.

Rust no nos permitirá anotar un tipo con `Copy` si el tipo, o alguna de sus partes, ha implementado el trato `Drop`. Si el tipo necesita que algo especial suceda cuando el valor sale del ámbito y agregamos la anotación `Copy` a ese tipo, obtendremos un error en tiempo de compilación. Para aprender cómo agregar la anotación `Copy` a su tipo para implementar el trato, consulte "Tratados derivables".

Entonces, ¿qué tipos implementan el trato `Copy`? Puedes consultar la documentación del tipo dado para estar seguro, pero como regla general, cualquier grupo de valores escalares simples puede implementar `Copy`, y nada que requiera asignación o que sea alguna forma de recurso puede implementar `Copy`. Aquí hay algunos de los tipos que implementan `Copy`:

- Todos los tipos enteros, como `u32`.
- El tipo booleano, `bool`, con los valores `true` y `false`.
- Todos los tipos de punto flotante, como `f64`.
- El tipo de carácter, `char`.
- Las tuplas, si solo contienen tipos que también implementan `Copy`. Por ejemplo, `(i32, i32)` implementa `Copy`, pero `(i32, String)` no.
