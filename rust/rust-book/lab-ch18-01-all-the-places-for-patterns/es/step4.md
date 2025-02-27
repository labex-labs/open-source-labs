# Bucles Condicionales `while let`

Similar en construcción a `if let`, el bucle condicional `while let` permite que un bucle `while` se ejecute mientras un patrón siga coincidiendo. En el Listado 18-2, codificamos un bucle `while let` que utiliza un vector como una pila y muestra los valores del vector en el orden inverso al en que se insertaron.

Nombre del archivo: `src/main.rs`

```rust
let mut stack = Vec::new();

stack.push(1);
stack.push(2);
stack.push(3);

while let Some(top) = stack.pop() {
    println!("{top}");
}
```

Listado 18-2: Usando un bucle `while let` para imprimir valores mientras `stack.pop()` devuelva `Some`

Este ejemplo imprime `3`, `2` y luego `1`. El método `pop` saca el último elemento del vector y devuelve `Some(value)`. Si el vector está vacío, `pop` devuelve `None`. El bucle `while` continúa ejecutando el código en su bloque mientras `pop` devuelva `Some`. Cuando `pop` devuelve `None`, el bucle se detiene. Podemos usar `while let` para sacar cada elemento de nuestra pila.
