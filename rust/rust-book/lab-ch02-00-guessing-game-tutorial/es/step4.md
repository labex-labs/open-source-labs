# Almacenando valores con variables

A continuación, crearemos una _variable_ para almacenar la entrada del usuario, así:

```rust
let mut guess = String::new();
```

¡Ahora el programa está resultando interesante! Hay muchas cosas sucediendo en esta pequeña línea. Usamos la declaración `let` para crear la variable. Aquí hay otro ejemplo:

```rust
let apples = 5;
```

Esta línea crea una nueva variable llamada `apples` y la asocia con el valor 5. En Rust, las variables son inmutables por defecto, lo que significa que una vez que le damos un valor a una variable, ese valor no cambiará. Vamos a discutir este concepto en detalle en "Variables y Mutabilidad". Para hacer una variable mutable, agregamos `mut` antes del nombre de la variable:

```rust
let apples = 5; // inmutable
let mut bananas = 5; // mutable
```

> Nota: La sintaxis `//` inicia un comentario que continúa hasta el final de la línea. Rust ignora todo lo que está en los comentarios. Vamos a discutir los comentarios con más detalle en el Capítulo 3.

Volviendo al programa del juego de adivinanza, ahora sabes que `let mut guess` introducirá una variable mutable llamada `guess`. El signo igual (`=`) le dice a Rust que queremos asociar algo a la variable ahora. A la derecha del signo igual está el valor al que `guess` está asociado, que es el resultado de llamar a `String::new`, una función que devuelve una nueva instancia de un `String`. `String` es un tipo de cadena proporcionado por la librería estándar que es un trozo de texto codificado en UTF-8 y que puede crecer.

La sintaxis `::` en la línea `::new` indica que `new` es una función asociada del tipo `String`. Una _función asociada_ es una función que se implementa en un tipo, en este caso `String`. Esta función `new` crea una nueva cadena vacía. Encontrarás una función `new` en muchos tipos porque es un nombre común para una función que crea un nuevo valor de algún tipo.

En resumen, la línea `let mut guess = String::new();` ha creado una variable mutable que actualmente está asociada a una nueva instancia vacía de un `String`. ¡Puff!
