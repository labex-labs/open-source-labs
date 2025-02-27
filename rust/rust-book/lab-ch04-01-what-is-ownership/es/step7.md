# Variables y datos interactuando con Clone

Si _queremos_ copiar en profundidad los datos del montón del `String`, no solo los datos de la pila, podemos usar un método común llamado `clone`. Discutiremos la sintaxis de los métodos en el Capítulo 5, pero debido a que los métodos son una característica común en muchos lenguajes de programación, es probable que los hayas visto antes.

Aquí hay un ejemplo de cómo funciona el método `clone`:

```rust
let s1 = String::from("hello");
let s2 = s1.clone();

println!("s1 = {s1}, s2 = {s2}");
```

Esto funciona perfectamente y produce explícitamente el comportamiento mostrado en la Figura 4-3, donde los datos del montón _se copian_.

Cuando ves una llamada a `clone`, sabes que se está ejecutando algún código arbitrario y que ese código puede ser costoso. Es un indicador visual de que algo diferente está sucediendo.
