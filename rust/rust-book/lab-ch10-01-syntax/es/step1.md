# Eliminación de duplicados mediante extracción de una función

Los genéricos nos permiten reemplazar tipos específicos con un marcador de posición que representa múltiples tipos para eliminar la duplicación de código. Antes de adentrarnos en la sintaxis de los genéricos, primero veamos cómo eliminar la duplicación de una manera que no involucre tipos genéricos mediante la extracción de una función que reemplaza valores específicos con un marcador de posición que representa múltiples valores. Luego aplicaremos la misma técnica para extraer una función genérica. Al ver cómo reconocer el código duplicado que se puede extraer en una función, comenzarás a reconocer el código duplicado que puede utilizar genéricos.

Comenzaremos con el programa corto de la Lista 10-1 que encuentra el número más grande en una lista.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
  1 let number_list = vec![34, 50, 25, 100, 65];

  2 let mut largest = &number_list[0];

  3 for number in &number_list {
      4 if number > largest {
          5 largest = number;
        }
    }

    println!("El número más grande es {largest}");
}
```

Lista 10-1: Encontrando el número más grande en una lista de números

Almacenamos una lista de enteros en la variable `number_list` \[1\] y colocamos una referencia al primer número de la lista en una variable llamada `largest` \[2\]. Luego iteramos a través de todos los números de la lista \[3\], y si el número actual es mayor que el número almacenado en `largest` \[4\], reemplazamos la referencia en esa variable \[5\]. Sin embargo, si el número actual es menor o igual al número más grande visto hasta ahora, la variable no cambia y el código pasa al siguiente número de la lista. Después de considerar todos los números de la lista, `largest` debería referirse al número más grande, que en este caso es 100.

Ahora nos han encomendado la tarea de encontrar el número más grande en dos listas diferentes de números. Para hacer eso, podemos elegir duplicar el código de la Lista 10-1 y usar la misma lógica en dos lugares diferentes del programa, como se muestra en la Lista 10-2.

Nombre de archivo: `src/main.rs`

```rust
fn main() {
    let number_list = vec![34, 50, 25, 100, 65];

    let mut largest = &number_list[0];

    for number in &number_list {
        if number > largest {
            largest = number;
        }
    }

    println!("El número más grande es {largest}");

    let number_list = vec![102, 34, 6000, 89, 54, 2, 43, 8];

    let mut largest = &number_list[0];

    for number in &number_list {
        if number > largest {
            largest = number;
        }
    }

    println!("El número más grande es {largest}");
}
```

Lista 10-2: Código para encontrar el número más grande en _dos_ listas de números

Aunque este código funciona, duplicar el código es tedioso y propenso a errores. También tenemos que recordar actualizar el código en múltiples lugares cuando queremos cambiarlo.

Para eliminar esta duplicación, crearemos una abstracción definiendo una función que opere en cualquier lista de enteros pasada como parámetro. Esta solución hace que nuestro código sea más claro y nos permite expresar el concepto de encontrar el número más grande en una lista de manera abstracta.

En la Lista 10-3, extraemos el código que encuentra el número más grande en una función llamada `largest`. Luego llamamos a la función para encontrar el número más grande en las dos listas de la Lista 10-2. También podríamos usar la función en cualquier otra lista de valores de `i32` que podamos tener en el futuro.

Nombre de archivo: `src/main.rs`

```rust
fn largest(list: &[i32]) -> &i32 {
    let mut largest = &list[0];

    for item in list {
        if item > largest {
            largest = item;
        }
    }

    largest
}

fn main() {
    let number_list = vec![34, 50, 25, 100, 65];

    let result = largest(&number_list);
    println!("El número más grande es {result}");

    let number_list = vec![102, 34, 6000, 89, 54, 2, 43, 8];

    let result = largest(&number_list);
    println!("El número más grande es {result}");
}
```

Lista 10-3: Código abstraído para encontrar el número más grande en dos listas

La función `largest` tiene un parámetro llamado `list`, que representa cualquier fragmento concreto de valores de `i32` que podamos pasar a la función. Como resultado, cuando llamamos a la función, el código se ejecuta en los valores específicos que pasamos.

En resumen, estos son los pasos que dimos para cambiar el código de la Lista 10-2 a la Lista 10-3:

1.  Identificar el código duplicado.
2.  Extraer el código duplicado al cuerpo de la función y especificar las entradas y los valores de retorno de ese código en la firma de la función.
3.  Actualizar las dos instancias de código duplicado para llamar a la función en lugar de eso.

A continuación, usaremos estos mismos pasos con genéricos para reducir la duplicación de código. De la misma manera que el cuerpo de la función puede operar en una `list` abstracta en lugar de valores específicos, los genéricos permiten que el código opere en tipos abstractos.

Por ejemplo, digamos que tuviéramos dos funciones: una que encuentra el elemento más grande en un fragmento de valores de `i32` y otra que encuentra el elemento más grande en un fragmento de valores de `char`. ¿Cómo eliminaremos esa duplicación? Vamos a averiguarlo!
