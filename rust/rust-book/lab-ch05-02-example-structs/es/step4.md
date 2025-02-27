# Agregando Funcionalidad Útil con Rasgos Derivados

Sería útil poder imprimir una instancia de `Rectangle` mientras estamos depurando nuestro programa y ver los valores de todos sus campos. La Lista 5-11 intenta usar la macro `println!` como lo hemos hecho en capítulos anteriores. Sin embargo, esto no funcionará.

Nombre del archivo: `src/main.rs`

```rust
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!("rect1 es {}", rect1);
}
```

Lista 5-11: Intentando imprimir una instancia de `Rectangle`

Cuando compilamos este código, obtenemos un error con este mensaje principal:

```bash
error[E0277]: `Rectangle` no implementa `std::fmt::Display`
```

La macro `println!` puede hacer muchos tipos de formateo, y por defecto, las llaves curvas le dicen a `println!` que use un formateo conocido como `Display`: salida destinada para el consumo directo del usuario final. Los tipos primitivos que hemos visto hasta ahora implementan `Display` por defecto porque solo hay una forma en que querríamos mostrar un `1` u otro tipo primitivo a un usuario. Pero con las estructuras, la forma en que `println!` debería formatear la salida es menos clara porque hay más posibilidades de visualización: ¿Quieres comas o no? ¿Quieres imprimir las llaves curvas? ¿Deben mostrarse todos los campos? Debido a esta ambigüedad, Rust no intenta adivinar lo que queremos, y las estructuras no tienen una implementación proporcionada de `Display` para usar con `println!` y el marcador de posición `{}`.

Si seguimos leyendo los errores, encontraremos esta nota útil:

    = ayuda: el rasgo `std::fmt::Display` no está implementado para `Rectangle`
    = nota: en las cadenas de formato, es posible que puedas usar `{:?}` (o {:#?} para
    formato bonito) en su lugar

¡Intentémoslo! La llamada a la macro `println!` ahora se verá como `println!("rect1 es {:?}", rect1);`. Colocar el especificador `:?` dentro de las llaves curvas le dice a `println!` que queremos usar un formato de salida llamado `Debug`. El rasgo `Debug` nos permite imprimir nuestra estructura de una manera que sea útil para los desarrolladores para que podamos ver su valor mientras estamos depurando nuestro código.

Compile el código con este cambio. ¡Ay! Todavía obtenemos un error:

```bash
error[E0277]: `Rectangle` no implementa `Debug`
```

Pero una vez más, el compilador nos da una nota útil:

```rust
= ayuda: el rasgo `Debug` no está implementado para `Rectangle`
= nota: agregue `#[derive(Debug)]` o implemente manualmente `Debug`
```

Rust _sí_ incluye la funcionalidad para imprimir información de depuración, pero tenemos que optar explícitamente para que esa funcionalidad esté disponible para nuestra estructura. Para hacer eso, agregamos el atributo externo `#[derive(Debug)]` justo antes de la definición de la estructura, como se muestra en la Lista 5-12.

Nombre del archivo: `src/main.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let rect1 = Rectangle {
        width: 30,
        height: 50,
    };

    println!("rect1 es {:?}", rect1);
}
```

Lista 5-12: Agregando el atributo para derivar el rasgo `Debug` e imprimiendo la instancia de `Rectangle` usando el formateo de depuración

Ahora, cuando ejecutamos el programa, no obtendremos ningún error y veremos la siguiente salida:

```rust
rect1 es Rectangle { width: 30, height: 50 }
```

¡Genial! No es la salida más bonita, pero muestra los valores de todos los campos para esta instancia, lo que definitivamente ayudaría durante la depuración. Cuando tenemos estructuras más grandes, es útil tener una salida un poco más fácil de leer; en esos casos, podemos usar `{:#?}` en lugar de `{:?}` en la cadena de `println!`. En este ejemplo, usar el estilo `{:#?}` producirá la siguiente salida:

    rect1 es Rectangle {
        width: 30,
        height: 50,
    }

Otra forma de imprimir un valor usando el formato `Debug` es usar la macro `dbg!`, que toma posesión de una expresión (al contrario de `println!`, que toma una referencia), imprime el archivo y el número de línea donde se produce la llamada a la macro `dbg!` en su código junto con el valor resultante de esa expresión y devuelve la posesión del valor.

> Nota: Llamar a la macro `dbg!` imprime en el flujo de consola de error estándar (`stderr`), al contrario de `println!`, que imprime en el flujo de consola de salida estándar (`stdout`). Hablaremos más sobre `stderr` y `stdout` en "Escribiendo Mensajes de Error en el Error Estándar en lugar de la Salida Estándar".

Aquí hay un ejemplo donde estamos interesados en el valor que se asigna al campo `width`, así como en el valor de la estructura completa en `rect1`:

Nombre del archivo: `src/main.rs`

```rust
#[derive(Debug)]
struct Rectangle {
    width: u32,
    height: u32,
}

fn main() {
    let scale = 2;
    let rect1 = Rectangle {
      1 width: dbg!(30 * scale),
        height: 50,
    };

  2 dbg!(&rect1);
}
```

Podemos poner `dbg!` alrededor de la expresión `30 * scale` \[1\] y, debido a que `dbg!` devuelve la posesión del valor de la expresión, el campo `width` tendrá el mismo valor que si no tuviéramos la llamada a `dbg!` allí. No queremos que `dbg!` tome posesión de `rect1`, por lo que usamos una referencia a `rect1` en la siguiente llamada \[2\]. Aquí está cómo se ve la salida de este ejemplo:

    [src/main.rs:10] 30 * scale = 60
    [src/main.rs:14] &rect1 = Rectangle {
        width: 60,
        height: 50,
    }

Podemos ver que la primera parte de la salida proviene de \[1\] donde estamos depurando la expresión `30 * scale` y su valor resultante es `60` (el formateo `Debug` implementado para enteros es imprimir solo su valor). La llamada a `dbg!` en \[2\] imprime el valor de `&rect1`, que es la estructura `Rectangle`. Esta salida utiliza el formateo `Debug` bonito del tipo `Rectangle`. La macro `dbg!` puede ser muy útil cuando intentas entender lo que está haciendo tu código.

Además del rasgo `Debug`, Rust ha proporcionado una serie de rasgos para que los usemos con el atributo `derive` que pueden agregar un comportamiento útil a nuestros tipos personalizados. Esos rasgos y sus comportamientos se enumeran en el Apéndice C. Cubriremos cómo implementar estos rasgos con un comportamiento personalizado, así como cómo crear tus propios rasgos en el Capítulo 10. También hay muchos atributos diferentes a `derive`; para obtener más información, consulte la sección "Atributos" de la Referencia de Rust en *https://doc.rust-lang.org/reference/attributes.html*.

Nuestra función `area` es muy específica: solo calcula el área de rectángulos. Sería útil vincular este comportamiento más estrechamente a nuestra estructura `Rectangle` porque no funcionará con ningún otro tipo. Veamos cómo podemos continuar refactorizando este código convirtiendo la función `area` en un _método_ `area` definido en nuestro tipo `Rectangle`.
