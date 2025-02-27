# Tomando rebanadas de cadenas

Indexar en una cadena a menudo es una mala idea porque no está claro cuál debería ser el tipo de retorno de la operación de indexación de cadenas: un valor de byte, un carácter, un cluster de grafemas o una rebanada de cadena. Si realmente necesitas usar índices para crear rebanadas de cadena, por lo tanto, Rust te pide que seas más específico.

En lugar de indexar usando `[]` con un solo número, puedes usar `[]` con un rango para crear una rebanada de cadena que contenga bytes particulares:

```rust
let hello = "Здравствуйте";

let s = &hello[0..4];
```

Aquí, `s` será un `&str` que contiene los primeros cuatro bytes de la cadena. Antes, mencionamos que cada uno de estos caracteres era de dos bytes, lo que significa que `s` será `Зд`.

Si intentáramos tomar una rebanada solo de parte de los bytes de un carácter con algo como `&hello[0..1]`, Rust se detendría en tiempo de ejecución de la misma manera que si se accediera a un índice no válido en un vector:

```rust
thread 'main' panicked at 'byte index 1 is not a char boundary;
it is inside 'З' (bytes 0..2) of `Здравствуйте`', src/main.rs:4:14
```

Debes tener cuidado al crear rebanadas de cadena con rangos, porque hacerlo puede detener tu programa.
