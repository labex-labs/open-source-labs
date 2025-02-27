# Iterar sobre los valores en un vector

Para acceder a cada elemento en un vector uno por uno, iteraríamos a través de todos los elementos en lugar de usar índices para acceder a uno a la vez. La Lista 8-7 muestra cómo usar un bucle `for` para obtener referencias inmutables a cada elemento en un vector de valores de tipo `i32` y mostrarlos.

```rust
let v = vec![100, 32, 57];
for i in &v {
    println!("{i}");
}
```

Lista 8-7: Mostrar cada elemento en un vector iterando sobre los elementos usando un bucle `for`

También podemos iterar sobre referencias mutables a cada elemento en un vector mutable para poder hacer cambios a todos los elementos. El bucle `for` en la Lista 8-8 sumará `50` a cada elemento.

```rust
let mut v = vec![100, 32, 57];
for i in &mut v {
    *i += 50;
}
```

Lista 8-8: Iterar sobre referencias mutables a elementos en un vector

Para cambiar el valor al que se refiere la referencia mutable, tenemos que usar el operador de desreferencia `*` para acceder al valor en `i` antes de poder usar el operador `+=`. Hablaremos más sobre el operador de desreferencia en "Siguiendo el puntero hacia el valor".

Iterar sobre un vector, ya sea inmutable o mutable, es seguro debido a las reglas del verificador de préstamos. Si intentáramos insertar o eliminar elementos en los cuerpos de los bucles `for` en las Listas 8-7 y 8-8, obtendríamos un error del compilador similar al que obtuvimos con el código en la Lista 8-6. La referencia al vector que mantiene el bucle `for` impide la modificación simultánea del vector completo.
