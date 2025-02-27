# Sacando los Valores Capturados de los Closures y los Tratamientos Fn

Una vez que un closure ha capturado una referencia o la propiedad de un valor del entorno donde se define el closure (por lo tanto, afectando lo que, si hay algo, se mueve _hacia dentro_ del closure), el código en el cuerpo del closure define lo que pasa con las referencias o valores cuando se evalúa el closure más tarde (por lo tanto, afectando lo que, si hay algo, se mueve _hacia fuera_ del closure).

El cuerpo de un closure puede hacer cualquiera de lo siguiente: mover un valor capturado fuera del closure, mutar el valor capturado, ni mover ni mutar el valor o no capturar nada del entorno para comenzar.

La forma en que un closure captura y maneja valores del entorno afecta a los tratamientos que implementa el closure, y los tratamientos son la forma en que funciones y structs pueden especificar qué tipos de closures pueden usar. Los closures implementarán automáticamente uno, dos o los tres de estos tratamientos `Fn`, de manera aditiva, dependiendo de cómo el cuerpo del closure maneja los valores:

- `FnOnce` se aplica a closures que se pueden llamar una vez. Todos los closures implementan al menos este tratamiento porque todos los closures se pueden llamar. Un closure que mueve valores capturados fuera de su cuerpo solo implementará `FnOnce` y ninguno de los otros tratamientos `Fn` porque solo se puede llamar una vez.
- `FnMut` se aplica a closures que no mueven valores capturados fuera de su cuerpo, pero que pueden mutar los valores capturados. Estos closures se pueden llamar más de una vez.
- `Fn` se aplica a closures que no mueven valores capturados fuera de su cuerpo y que no mutan valores capturados, así como a closures que no capturan nada de su entorno. Estos closures se pueden llamar más de una vez sin mutar su entorno, lo que es importante en casos como llamar a un closure múltiples veces de manera concurrente.

Veamos la definición del método `unwrap_or_else` en `Option<T>` que usamos en la Lista 13-1:

```rust
impl<T> Option<T> {
    pub fn unwrap_or_else<F>(self, f: F) -> T
    where
        F: FnOnce() -> T
    {
        match self {
            Some(x) => x,
            None => f(),
        }
    }
}
```

Recuerda que `T` es el tipo genérico que representa el tipo del valor en la variante `Some` de un `Option`. Ese tipo `T` también es el tipo de retorno de la función `unwrap_or_else`: el código que llama a `unwrap_or_else` en un `Option<String>`, por ejemplo, obtendrá un `String`.

A continuación, observa que la función `unwrap_or_else` tiene el parámetro de tipo genérico adicional `F`. El tipo `F` es el tipo del parámetro llamado `f`, que es el closure que proporcionamos cuando llamamos a `unwrap_or_else`.

La restricción de tratamiento especificada en el tipo genérico `F` es `FnOnce() -> T`, lo que significa que `F` debe poder ser llamado una vez, no tomar argumentos y devolver un `T`. Usar `FnOnce` en la restricción de tratamiento expresa la limitación de que `unwrap_or_else` solo llamará a `f` una vez, como máximo. En el cuerpo de `unwrap_or_else`, podemos ver que si el `Option` es `Some`, `f` no se llamará. Si el `Option` es `None`, `f` se llamará una vez. Debido a que todos los closures implementan `FnOnce`, `unwrap_or_else` acepta la mayor variedad de closures y es tan flexible como puede ser.

> Nota: Las funciones también pueden implementar los tres tratamientos `Fn`. Si lo que queremos hacer no requiere capturar un valor del entorno, podemos usar el nombre de una función en lugar de un closure donde necesitamos algo que implemente uno de los tratamientos `Fn`. Por ejemplo, en un valor `Option<Vec<T>>`, podríamos llamar a `unwrap_or_else(Vec::new)` para obtener un nuevo vector vacío si el valor es `None`.

Ahora veamos el método estándar de la biblioteca `sort_by_key`, definido en slices, para ver cómo difiere de `unwrap_or_else` y por qué `sort_by_key` usa `FnMut` en lugar de `FnOnce` para la restricción de tratamiento. El closure recibe un argumento en forma de una referencia al elemento actual en el slice que se está considerando y devuelve un valor de tipo `K` que se puede ordenar. Esta función es útil cuando quieres ordenar un slice por un atributo particular de cada elemento. En la Lista 13-7, tenemos una lista de instancias de `Rectangle` y usamos `sort_by_key` para ordenarlas por su atributo `width` de menor a mayor.

Nombre de archivo: `src/main.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let mut list = [
        Rectangle { width: 10, height: 1 },
        Rectangle { width: 3, height: 5 },
        Rectangle { width: 7, height: 12 },
    ];

    list.sort_by_key(|r| r.width);
    println!("{:#?}", list);
}
```

Lista 13-7: Usando `sort_by_key` para ordenar rectángulos por ancho

Este código imprime:

    [
        Rectangle {
            width: 3,
            height: 5,
        },
        Rectangle {
            width: 7,
            height: 12,
        },
        Rectangle {
            width: 10,
            height: 1,
        },
    ]

La razón por la que `sort_by_key` está definido para tomar un closure `FnMut` es que lo llama múltiples veces: una vez para cada elemento en el slice. El closure `|r| r.width` no captura, muta ni mueve nada de su entorno, por lo que cumple con los requisitos de la restricción de tratamiento.

En contraste, la Lista 13-8 muestra un ejemplo de un closure que implementa solo el tratamiento `FnOnce`, porque mueve un valor fuera del entorno. El compilador no nos permitirá usar este closure con `sort_by_key`.

Nombre de archivo: `src/main.rs`

```rust
--snip--

fn main() {
    let mut list = [
        Rectangle { width: 10, height: 1 },
        Rectangle { width: 3, height: 5 },
        Rectangle { width: 7, height: 12 },
    ];

    let mut sort_operations = vec![];
    let value = String::from("by key called");

    list.sort_by_key(|r| {
        sort_operations.push(value);
        r.width
    });
    println!("{:#?}", list);
}
```

Lista 13-8: Intentando usar un closure `FnOnce` con `sort_by_key`

Este es un ejemplo forzado y complicado (que no funciona) para tratar de contar el número de veces que `sort_by_key` se llama cuando se ordena `list`. Este código intenta hacer este recuento empujando `value` (una `String` del entorno del closure) al vector `sort_operations`. El closure captura `value` y luego mueve `value` fuera del closure transferiendo la propiedad de `value` al vector `sort_operations`. Este closure se puede llamar una vez; intentar llamarlo una segunda vez no funcionaría porque `value` ya no estaría en el entorno para ser empujado nuevamente a `sort_operations`! Por lo tanto, este closure solo implementa `FnOnce`. Cuando intentamos compilar este código, obtenemos este error de que `value` no se puede mover fuera del closure porque el closure debe implementar `FnMut`:

```bash
error[E0507]: cannot move out of `value`, a captured variable in an `FnMut`
closure
  --> src/main.rs:18:30
   |
15 |       let value = String::from("by key called");
   |           ----- captured outer variable
16 |
17 |       list.sort_by_key(|r| {
   |  ______________________-
18 | |         sort_operations.push(value);
   | |                              ^^^^^ move occurs because `value` has
type `String`, which does not implement the `Copy` trait
19 | |         r.width
20 | |     });
   | |_____- captured by this `FnMut` closure
```

El error apunta a la línea en el cuerpo del closure que mueve `value` fuera del entorno. Para solucionar esto, necesitamos cambiar el cuerpo del closure para que no mueva valores fuera del entorno. Mantener un contador en el entorno e incrementar su valor en el cuerpo del closure es una forma más directa de contar el número de veces que se llama a `sort_by_key`. El closure en la Lista 13-9 funciona con `sort_by_key` porque solo está capturando una referencia mutable al contador `num_sort_operations` y por lo tanto se puede llamar más de una vez.

Nombre de archivo: `src/main.rs`

```rust
--snip--

fn main() {
    --snip--

    let mut num_sort_operations = 0;
    list.sort_by_key(|r| {
        num_sort_operations += 1;
        r.width
    });
    println!(
        "{:#?}, sorted in {num_sort_operations} operations",
        list
    );
}
```

Lista 13-9: Usar un closure `FnMut` con `sort_by_key` está permitido.

Los tratamientos `Fn` son importantes cuando se definen o se usan funciones o tipos que utilizan closures. En la siguiente sección, discutiremos iteradores. Muchos métodos de iterador toman argumentos de closure, ¡así que mantenga estos detalles de closure en mente a medida que continuamos!
