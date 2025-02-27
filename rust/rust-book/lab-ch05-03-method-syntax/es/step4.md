# Funciones Asociadas

Todas las funciones definidas dentro de un bloque `impl` se llaman _funciones asociadas_ porque están asociadas con el tipo nombrado después del `impl`. Podemos definir funciones asociadas que no tienen `self` como su primer parámetro (y por lo tanto no son métodos) porque no necesitan una instancia del tipo para funcionar. Ya hemos usado una función así: la función `String::from` que está definida en el tipo `String`.

Las funciones asociadas que no son métodos a menudo se usan para constructores que devolverán una nueva instancia del struct. A menudo se llaman `new`, pero `new` no es un nombre especial y no está integrado en el lenguaje. Por ejemplo, podríamos elegir proporcionar una función asociada llamada `square` que tendría un parámetro de dimensión y lo usaría como tanto ancho como alto, lo que haría más fácil crear un `Rectangle` cuadrado en lugar de tener que especificar el mismo valor dos veces:

Nombre de archivo: `src/main.rs`

```rust
impl Rectangle {
    fn square(size: u32) -> 1 Self  {
      2 Self  {
            width: size,
            height: size,
        }
    }
}
```

Las palabras clave `Self` en el tipo de retorno \[1\] y en el cuerpo de la función \[2\] son alias para el tipo que aparece después de la palabra clave `impl`, que en este caso es `Rectangle`.

Para llamar a esta función asociada, usamos la sintaxis `::` con el nombre del struct; `let sq = Rectangle::square(3);` es un ejemplo. Esta función está en un espacio de nombres del struct: la sintaxis `::` se utiliza tanto para funciones asociadas como para los espacios de nombres creados por los módulos. Discutiremos los módulos en el Capítulo 7.
