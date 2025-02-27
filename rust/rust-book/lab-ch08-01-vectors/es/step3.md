# Actualizar un vector

Para crear un vector y luego agregar elementos a él, podemos usar el método `push`, como se muestra en la Lista 8-3.

```rust
let mut v = Vec::new();

v.push(5);
v.push(6);
v.push(7);
v.push(8);
```

Lista 8-3: Usar el método `push` para agregar valores a un vector

Como con cualquier variable, si queremos poder cambiar su valor, necesitamos hacerla mutable usando la palabra clave `mut`, como se discutió en el Capítulo 3. Los números que ponemos dentro son todos del tipo `i32`, y Rust infiere esto a partir de los datos, por lo que no necesitamos la anotación `Vec<i32>`.
