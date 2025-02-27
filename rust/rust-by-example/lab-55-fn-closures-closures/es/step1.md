# Closures

Los closures son funciones que pueden capturar el entorno circundante. Por ejemplo, un closure que captura la variable `x`:

```rust
|val| val + x
```

La sintaxis y las capacidades de los closures los hacen muy convenientes para su uso inmediato. Llamar a un closure es exactamente como llamar a una función. Sin embargo, tanto los tipos de entrada como de retorno _pueden_ ser inferidos y los nombres de las variables de entrada _deben_ ser especificados.

Otras características de los closures incluyen:

- usar `||` en lugar de `()` alrededor de las variables de entrada.
- delimitación opcional del cuerpo (`{}`) para una sola expresión (obligatoria en caso contrario).
- la capacidad de capturar las variables del entorno externo.

```rust
fn main() {
    let outer_var = 42;

    // Una función regular no puede hacer referencia a variables en el entorno circundante
    //fn function(i: i32) -> i32 { i + outer_var }
    // TODO: descomentar la línea anterior y ver el error del compilador. El compilador
    // sugiere que definamos un closure en lugar.

    // Los closures son anónimos, aquí los estamos enlazando a referencias
    // La anotación es idéntica a la anotación de función pero es opcional
    // al igual que las `{}` que envuelven el cuerpo. Estas funciones sin nombre
    // se asignan a variables con nombres adecuados.
    let closure_annotated = |i: i32| -> i32 { i + outer_var };
    let closure_inferred  = |i     |          i + outer_var  ;

    // Llama a los closures.
    println!("closure_annotated: {}", closure_annotated(1));
    println!("closure_inferred: {}", closure_inferred(1));
    // Una vez que el tipo de un closure ha sido inferido, no se puede inferir de nuevo con otro tipo.
    //println!("cannot reuse closure_inferred with another type: {}", closure_inferred(42i64));
    // TODO: descomentar la línea anterior y ver el error del compilador.

    // Un closure que no toma argumentos y devuelve un `i32`.
    // El tipo de retorno es inferido.
    let one = || 1;
    println!("closure returning one: {}", one());

}
```
