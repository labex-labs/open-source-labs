# Alcance de variables

Ahora que ya hemos pasado por la sintaxis básica de Rust, no incluiremos todo el código `fn main() {` en los ejemplos, así que si estás siguiendo, asegúrate de poner los siguientes ejemplos manualmente dentro de una función `main`. Como resultado, nuestros ejemplos serán un poco más concisos, lo que nos permitirá centrar nuestra atención en los detalles reales en lugar del código repetitivo.

Como primer ejemplo de propiedad, vamos a ver el _alcance_ de algunas variables. Un alcance es el rango dentro de un programa para el cual un elemento es válido. Tomemos la siguiente variable:

```rust
let s = "hello";
```

La variable `s` se refiere a un literal de cadena, donde el valor de la cadena está codificado en el texto de nuestro programa. La variable es válida desde el momento en que se declara hasta el final del _alcance_ actual. La Lista 4-1 muestra un programa con comentarios que indican dónde la variable `s` sería válida.

    {                      // s no es válida aquí, ya que aún no está declarada
        let s = "hello";   // s es válida a partir de este momento en adelante

        // haz cosas con s
    }                      // este alcance ha terminado, y s ya no es válida

Lista 4-1: Una variable y el alcance en el que es válida

En otras palabras, hay dos momentos importantes aquí:

- Cuando `s` entra en _alcance_, es válida.
- Sigue siendo válida hasta que sale del _alcance_.

En este momento, la relación entre los alcances y cuándo las variables son válidas es similar a la de otros lenguajes de programación. Ahora construiremos sobre esta comprensión al introducir el tipo `String`.
