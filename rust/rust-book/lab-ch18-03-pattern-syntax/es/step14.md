# Una variable no utilizada comenzando su nombre con \_

Si creas una variable pero no la usas en ningún lugar, Rust generalmente emitirá una advertencia porque una variable no utilizada podría ser un error. Sin embargo, a veces es útil poder crear una variable que aún no utilizarás, como cuando estás haciendo un prototipo o simplemente comenzando un proyecto. En esta situación, puedes decirle a Rust que no te advierta sobre la variable no utilizada comenzando el nombre de la variable con un guion bajo. En la Lista 18-20, creamos dos variables no utilizadas, pero cuando compilamos este código, solo deberíamos recibir una advertencia sobre una de ellas.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let _x = 5;
    let y = 10;
}
```

Lista 18-20: Comenzar el nombre de una variable con un guion bajo para evitar advertencias de variables no utilizadas

Aquí, recibimos una advertencia sobre no utilizar la variable `y`, pero no recibimos una advertencia sobre no utilizar `_x`.

Tenga en cuenta que hay una diferencia sutil entre usar solo `_` y usar un nombre que comienza con un guion bajo. La sintaxis `_x` todavía enlaza el valor a la variable, mientras que `_` no enlaza en absoluto. Para mostrar un caso en el que esta distinción importa, la Lista 18-21 nos proporcionará un error.

Nombre de archivo: `src/main.rs`

```rust
let s = Some(String::from("Hello!"));

if let Some(_s) = s {
    println!("encontró una cadena");
}

println!("{:?}", s);
```

Lista 18-21: Una variable no utilizada que comienza con un guion bajo todavía enlaza el valor, lo que podría tomar posesión del valor.

Recibiremos un error porque el valor `s` todavía se moverá a `_s`, lo que nos impide usar `s` nuevamente. Sin embargo, usar el guion bajo por sí solo nunca se enlaza al valor. La Lista 18-22 se compilará sin errores porque `s` no se mueve a `_`.

Nombre de archivo: `src/main.rs`

```rust
let s = Some(String::from("Hello!"));

if let Some(_) = s {
    println!("encontró una cadena");
}

println!("{:?}", s);
```

Lista 18-22: Usar un guion bajo no enlaza el valor.

Este código funciona perfectamente porque nunca enlazamos `s` a nada; no se mueve.
