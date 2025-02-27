# Sintaxis de anotación de lifetimes

Las anotaciones de lifetimes no cambian la duración de ninguna de las referencias. En cambio, describen las relaciones de los lifetimes de múltiples referencias entre sí sin afectar los lifetimes. Al igual que las funciones pueden aceptar cualquier tipo cuando la firma especifica un parámetro de tipo genérico, las funciones pueden aceptar referencias con cualquier lifetime al especificar un parámetro de lifetime genérico.

Las anotaciones de lifetimes tienen una sintaxis ligeramente inusual: los nombres de los parámetros de lifetime deben comenzar con una apóstrofe (`'`) y por lo general son todos en minúsculas y muy cortos, como los tipos genéricos. La mayoría de las personas utiliza el nombre `'a` para la primera anotación de lifetime. Colocamos las anotaciones de parámetros de lifetime después del `&` de una referencia, usando un espacio para separar la anotación del tipo de referencia.

Aquí hay algunos ejemplos: una referencia a un `i32` sin parámetro de lifetime, una referencia a un `i32` que tiene un parámetro de lifetime llamado `'a`, y una referencia mutable a un `i32` que también tiene el lifetime `'a`.

```rust
&i32        // una referencia
&'a i32     // una referencia con un lifetime explícito
&'a mut i32 // una referencia mutable con un lifetime explícito
```

Una anotación de lifetime por sí sola no tiene mucho significado porque las anotaciones se destinan a decirle a Rust cómo se relacionan los parámetros de lifetime genéricos de múltiples referencias entre sí. Examinemos cómo se relacionan las anotaciones de lifetime entre sí en el contexto de la función `longest`.
