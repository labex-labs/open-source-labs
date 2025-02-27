# Arrays y Slices

Un array es una colección de objetos del mismo tipo `T`, almacenados en memoria contigua. Los arrays se crean utilizando corchetes `[]`, y su longitud, que es conocida en tiempo de compilación, es parte de su firma de tipo `[T; longitud]`.

Los slices son similares a los arrays, pero su longitud no es conocida en tiempo de compilación. En lugar de eso, un slice es un objeto de dos palabras; la primera palabra es un puntero a los datos, la segunda palabra es la longitud del slice. El tamaño de la palabra es el mismo que usize, determinado por la arquitectura del procesador, por ejemplo, 64 bits en un x86-64. Los slices se pueden utilizar para prestar una sección de un array y tienen la firma de tipo `&[T]`.

```rust
use std::mem;

// Esta función presta un slice.
fn analizar_slice(slice: &[i32]) {
    println!("Primer elemento del slice: {}", slice[0]);
    println!("El slice tiene {} elementos", slice.len());
}

fn main() {
    // Array de tamaño fijo (la firma de tipo es superfluous).
    let xs: [i32; 5] = [1, 2, 3, 4, 5];

    // Todos los elementos se pueden inicializar con el mismo valor.
    let ys: [i32; 500] = [0; 500];

    // El índice comienza en 0.
    println!("Primer elemento del array: {}", xs[0]);
    println!("Segundo elemento del array: {}", xs[1]);

    // `len` devuelve la cantidad de elementos en el array.
    println!("Número de elementos en el array: {}", xs.len());

    // Los arrays se asignan en la pila.
    println!("El array ocupa {} bytes", mem::size_of_val(&xs));

    // Los arrays se pueden prestar automáticamente como slices.
    println!("Prestar todo el array como un slice.");
    analizar_slice(&xs);

    // Los slices pueden apuntar a una sección de un array.
    // Tienen la forma [índice_inicial..índice_final].
    // `índice_inicial` es la primera posición en el slice.
    // `índice_final` es uno más que la última posición en el slice.
    println!("Prestar una sección del array como un slice.");
    analizar_slice(&ys[1..4]);

    // Ejemplo de slice vacío `&[]`:
    let empty_array: [u32; 0] = [];
    assert_eq!(&empty_array, &[]);
    assert_eq!(&empty_array, &[][..]); // Lo mismo pero más detallado

    // Los arrays se pueden acceder de manera segura utilizando `.get`, que devuelve un
    // `Option`. Esto se puede coincidir como se muestra a continuación, o utilizarse con
    // `.expect()` si desea que el programa salga con un mensaje agradable
    // en lugar de continuar felizmente.
    for i in 0..xs.len() + 1 { // Oops, un elemento de más!
        match xs.get(i) {
            Some(xval) => println!("{}: {}", i, xval),
            None => println!("¡Desacelera! {} es demasiado lejos!", i),
        }
    }

    // El índice fuera de los límites en el array causa un error en tiempo de compilación.
    //println!("{}", xs[5]);
    // El índice fuera de los límites en el slice causa un error en tiempo de ejecución.
    //println!("{}", xs[..][5]);
}
```
