# Calculando el tamaño de un tipo no recursivo

Recuerde el enumerado `Message` que definimos en la Lista 6-2 cuando discutimos las definiciones de enumerados en el Capítulo 6:

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}
```

Para determinar cuánto espacio asignar para un valor de `Message`, Rust examina cada una de las variantes para ver cuál necesita más espacio. Rust ve que `Message::Quit` no necesita ningún espacio, `Message::Move` necesita suficiente espacio para almacenar dos valores de `i32`, y así sucesivamente. Debido a que solo se usará una variante, el mayor espacio que un valor de `Message` necesitará es el espacio que ocuparía almacenar la más grande de sus variantes.

Contraste esto con lo que sucede cuando Rust intenta determinar cuánto espacio necesita un tipo recursivo como el enumerado `List` en la Lista 15-2. El compilador comienza examinando la variante `Cons`, que contiene un valor de tipo `i32` y un valor de tipo `List`. Por lo tanto, `Cons` necesita una cantidad de espacio igual al tamaño de un `i32` más el tamaño de un `List`. Para determinar cuánta memoria necesita el tipo `List`, el compilador examina las variantes, comenzando por la variante `Cons`. La variante `Cons` contiene un valor de tipo `i32` y un valor de tipo `List`, y este proceso continúa indefinidamente, como se muestra en la Figura 15-1.

Figura 15-1: Una `List` infinita compuesta por variantes `Cons` infinitas
