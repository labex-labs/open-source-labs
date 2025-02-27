# Métodos que Producen Otros Iteradores

Los _adaptadores de iterador_ son métodos definidos en el trait `Iterator` que no consumen el iterador. En cambio, producen iteradores diferentes cambiando algún aspecto del iterador original.

La Lista 13-14 muestra un ejemplo de llamada al método de adaptador de iterador `map`, que toma una clausura para llamar en cada elemento a medida que se itera a través de los elementos. El método `map` devuelve un nuevo iterador que produce los elementos modificados. La clausura aquí crea un nuevo iterador en el que cada elemento del vector se incrementará en 1.

Nombre de archivo: `src/main.rs`

```rust
let v1: Vec<i32> = vec![1, 2, 3];

v1.iter().map(|x| x + 1);
```

Lista 13-14: Llamada al adaptador de iterador `map` para crear un nuevo iterador

Sin embargo, este código produce una advertencia:

    advertencia: `Map` no utilizado que debe ser utilizado
     --> src/main.rs:4:5
      |
    4 |     v1.iter().map(|x| x + 1);
      |     ^^^^^^^^^^^^^^^^^^^^^^^^^
      |
      = nota: `#[warn(unused_must_use)]` activado por defecto
      = nota: los iteradores son perezosos y no hacen nada a menos que se consuman

El código de la Lista 13-14 no hace nada; la clausura que hemos especificado nunca se llama. La advertencia nos recuerda por qué: los adaptadores de iterador son perezosos, y aquí necesitamos consumir el iterador.

Para corregir esta advertencia y consumir el iterador, usaremos el método `collect`, que usamos con `env::args` en la Lista 12-1. Este método consume el iterador y recopila los valores resultantes en un tipo de datos de colección.

En la Lista 13-15, recopilamos en un vector los resultados de iterar sobre el iterador que se devuelve de la llamada a `map`. Este vector terminará conteniendo cada elemento del vector original, incrementado en 1.

Nombre de archivo: `src/main.rs`

```rust
let v1: Vec<i32> = vec![1, 2, 3];

let v2: Vec<_> = v1.iter().map(|x| x + 1).collect();

assert_eq!(v2, vec![2, 3, 4]);
```

Lista 13-15: Llamada al método `map` para crear un nuevo iterador, y luego llamada al método `collect` para consumir el nuevo iterador y crear un vector

Debido a que `map` toma una clausura, podemos especificar cualquier operación que queramos realizar en cada elemento. Este es un gran ejemplo de cómo las clausuras te permiten personalizar cierto comportamiento mientras reutilizas el comportamiento de iteración que proporciona el trait `Iterator`.

Puedes encadenar múltiples llamadas a adaptadores de iterador para realizar acciones complejas de manera legible. Pero como todos los iteradores son perezosos, tienes que llamar a uno de los métodos de adaptador consumidor para obtener resultados de las llamadas a adaptadores de iterador.
