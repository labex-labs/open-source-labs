# Crear un nuevo vector

Para crear un nuevo vector vacío, llamamos a la función `Vec::new`, como se muestra en la Lista 8-1.

```rust
let v: Vec<i32> = Vec::new();
```

Lista 8-1: Crear un nuevo vector vacío para almacenar valores del tipo `i32`

Tenga en cuenta que agregamos una anotación de tipo aquí. Dado que no estamos insertando ningún valor en este vector, Rust no sabe de qué tipo de elementos pretendemos almacenar. Este es un punto importante. Los vectores se implementan utilizando genéricos; cubriremos cómo usar genéricos con sus propios tipos en el Capítulo 10. Por ahora, sepa que el tipo `Vec<T>` proporcionado por la biblioteca estándar puede almacenar cualquier tipo. Cuando creamos un vector para almacenar un tipo específico, podemos especificar el tipo dentro de los corchetes angulares. En la Lista 8-1, le hemos dicho a Rust que el `Vec<T>` en `v` contendrá elementos del tipo `i32`.

Con más frecuencia, creará un `Vec<T>` con valores iniciales y Rust inferirá el tipo de valor que desea almacenar, por lo que rara vez necesitará hacer esta anotación de tipo. Rust convenientemente proporciona la macro `vec!`, que creará un nuevo vector que contendrá los valores que le des. La Lista 8-2 crea un nuevo `Vec<i32>` que contiene los valores `1`, `2` y `3`. El tipo entero es `i32` porque ese es el tipo entero predeterminado, como discutimos en "Tipos de datos".

```rust
let v = vec![1, 2, 3];
```

Lista 8-2: Crear un nuevo vector que contiene valores

Dado que hemos dado valores iniciales de `i32`, Rust puede inferir que el tipo de `v` es `Vec<i32>`, y la anotación de tipo no es necesaria. A continuación, veremos cómo modificar un vector.
