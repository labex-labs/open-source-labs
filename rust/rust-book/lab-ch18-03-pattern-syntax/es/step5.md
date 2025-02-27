# Coincidencia de rangos de valores con..=

La sintaxis `..=` nos permite coincidir con un rango de valores inclusivo. En el siguiente código, cuando un patrón coincide con cualquiera de los valores dentro del rango dado, ese brazo se ejecutará:

Nombre de archivo: `src/main.rs`

```rust
let x = 5;

match x {
    1..=5 => println!("uno a cinco"),
    _ => println!("algo más"),
}
```

Si `x` es `1`, `2`, `3`, `4` o `5`, el primer brazo coincidirá. Esta sintaxis es más conveniente para múltiples valores de coincidencia que usar el operador `|` para expresar la misma idea; si tuviéramos que usar `|`, tendríamos que especificar `1 | 2 | 3 | 4 | 5`. Especificar un rango es mucho más corto, especialmente si queremos coincidir, digamos, cualquier número entre 1 y 1.000!

El compilador comprueba que el rango no esté vacío en tiempo de compilación, y como los únicos tipos para los que Rust puede decir si un rango está vacío o no son `char` y valores numéricos, los rangos solo se permiten con valores numéricos o `char`.

Aquí hay un ejemplo que usa rangos de valores de `char`:

Nombre de archivo: `src/main.rs`

```rust
let x = 'c';

match x {
    'a'..='j' => println!("letra ASCII temprana"),
    'k'..='z' => println!("letra ASCII tardía"),
    _ => println!("algo más"),
}
```

Rust puede decir que `'c'` está dentro del rango del primer patrón e imprime `letra ASCII temprana`.
