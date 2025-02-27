# Tuplas

Una tupla es una colección de valores de diferentes tipos. Las tuplas se construyen utilizando paréntesis `()`, y cada tupla en sí misma es un valor con una firma de tipo `(T1, T2,...)`, donde `T1`, `T2` son los tipos de sus miembros. Las funciones pueden usar tuplas para devolver múltiples valores, ya que las tuplas pueden contener cualquier número de valores.

```rust
// Las tuplas se pueden usar como argumentos de función y como valores de retorno.
fn reverse(pair: (i32, bool)) -> (bool, i32) {
    // `let` se puede usar para enlazar los miembros de una tupla a variables.
    let (int_param, bool_param) = pair;

    (bool_param, int_param)
}

// La siguiente estructura es para la actividad.
#[derive(Debug)]
struct Matrix(f32, f32, f32, f32);

fn main() {
    // Una tupla con una variedad de diferentes tipos.
    let long_tuple = (1u8, 2u16, 3u32, 4u64,
                      -1i8, -2i16, -3i32, -4i64,
                      0.1f32, 0.2f64,
                      'a', true);

    // Los valores se pueden extraer de la tupla usando el índice de tupla.
    println!("Primer valor de la tupla larga: {}", long_tuple.0);
    println!("Segundo valor de la tupla larga: {}", long_tuple.1);

    // Las tuplas pueden ser miembros de otras tuplas.
    let tuple_of_tuples = ((1u8, 2u16, 2u32), (4u64, -1i8), -2i16);

    // Las tuplas son imprimibles.
    println!("Tupla de tuplas: {:?}", tuple_of_tuples);

    // Pero las tuplas largas (más de 12 elementos) no se pueden imprimir.
    //let too_long_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13);
    //println!("Tupla demasiado larga: {:?}", too_long_tuple);
    // TODO ^ Descomenta las dos líneas anteriores para ver el error del compilador

    let pair = (1, true);
    println!("La pareja es {:?}", pair);

    println!("La pareja invertida es {:?}", reverse(pair));

    // Para crear tuplas de un solo elemento, se requiere una coma para distinguirlas
    // de un literal rodeado de paréntesis.
    println!("Tupla de un solo elemento: {:?}", (5u32,));
    println!("Solo un entero: {:?}", (5u32));

    // Las tuplas se pueden desestructurar para crear enlaces.
    let tuple = (1, "hello", 4.5, true);

    let (a, b, c, d) = tuple;
    println!("{:?}, {:?}, {:?}, {:?}", a, b, c, d);

    let matrix = Matrix(1.1, 1.2, 2.1, 2.2);
    println!("{:?}", matrix);
}
```

## Actividad

1.  _Recapitulación_: Agrega el trato `fmt::Display` a la estructura `Matrix` en el ejemplo anterior, de modo que si cambias de imprimir el formato de depuración `{:?}` al formato de visualización `{}`, veas la siguiente salida:

    ```plaintext
    ( 1.1 1.2 )
    ( 2.1 2.2 )
    ```

    Puedes consultar de nuevo el ejemplo para la impresión de visualización.

2.  Agrega una función `transpose` usando la función `reverse` como plantilla, que acepta una matriz como argumento y devuelve una matriz en la que dos elementos han sido intercambiados. Por ejemplo:

    ```rust
    println!("Matriz:\n{}", matrix);
    println!("Transpuesta:\n{}", transpose(matrix));
    ```

    Da como resultado la salida:

    ```plaintext
    Matriz:
    ( 1.1 1.2 )
    ( 2.1 2.2 )
    Transpuesta:
    ( 1.1 2.1 )
    ( 1.2 2.2 )
    ```
