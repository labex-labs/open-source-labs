# Devolviendo Valores desde los Bucles

Una de las usos de un `loop` es reintentar una operación que sabes que puede fallar, como comprobar si un hilo ha terminado su trabajo. También es posible que necesites pasar el resultado de esa operación fuera del bucle al resto de tu código. Para hacer esto, puedes agregar el valor que quieres devolver después de la expresión `break` que usas para detener el bucle; ese valor se devolverá fuera del bucle para que puedas usarlo, como se muestra aquí:

```rust
fn main() {
    let mut counter = 0;

    let result = loop {
        counter += 1;

        if counter == 10 {
            break counter * 2;
        }
    };

    println!("The result is {result}");
}
```

Antes del bucle, declaramos una variable llamada `counter` y la inicializamos a `0`. Luego declaramos una variable llamada `result` para almacenar el valor devuelto por el bucle. En cada iteración del bucle, sumamos `1` a la variable `counter`, y luego comprobamos si `counter` es igual a `10`. Cuando lo es, usamos la palabra clave `break` con el valor `counter * 2`. Después del bucle, usamos un punto y coma para terminar la declaración que asigna el valor a `result`. Finalmente, imprimimos el valor en `result`, que en este caso es `20`.
