# Anexando a una cadena con push_str y push

Podemos hacer crecer una `String` usando el método `push_str` para anexar una porción de cadena, como se muestra en la Lista 8-15.

```rust
let mut s = String::from("foo");
s.push_str("bar");
```

Lista 8-15: Anexando una porción de cadena a una `String` usando el método `push_str`

Después de estas dos líneas, `s` contendrá `foobar`. El método `push_str` toma una porción de cadena porque no necesariamente queremos tomar posesión del parámetro. Por ejemplo, en el código de la Lista 8-16, queremos poder usar `s2` después de anexar su contenido a `s1`.

```rust
let mut s1 = String::from("foo");
let s2 = "bar";
s1.push_str(s2);
println!("s2 is {s2}");
```

Lista 8-16: Usando una porción de cadena después de anexar su contenido a una `String`

Si el método `push_str` tomara posesión de `s2`, no podríamos imprimir su valor en la última línea. Sin embargo, este código funciona como esperamos.

El método `push` toma un solo carácter como parámetro y lo agrega a la `String`. La Lista 8-17 agrega la letra _l_ a una `String` usando el método `push`.

```rust
let mut s = String::from("lo");
s.push('l');
```

Lista 8-17: Agregando un carácter a un valor de `String` usando `push`

Como resultado, `s` contendrá `lol`.
