# `From` e `Into`

Los tratos [`From`](#from) y [`Into`](#into) están inherentemente vinculados, y esto es en realidad parte de su implementación. Si es posible convertir el tipo A a partir del tipo B, entonces es fácil de creer que deberíamos poder convertir el tipo B al tipo A.

## `From`

El trato [`From`](#from) permite que un tipo defina cómo crear sí mismo a partir de otro tipo, proporcionando así un mecanismo muy simple para convertir entre varios tipos. Hay numerosas implementaciones de este trato en la biblioteca estándar para la conversión de tipos primitivos y comunes.

Por ejemplo, podemos convertir fácilmente un `str` en un `String`

```rust
let my_str = "hello";
let my_string = String::from(my_str);
```

Podemos hacer lo mismo para definir una conversión para nuestro propio tipo.

```rust
use std::convert::From;

#[derive(Debug)]
struct Number {
    value: i32,
}

impl From<i32> for Number {
    fn from(item: i32) -> Self {
        Number { value: item }
    }
}

fn main() {
    let num = Number::from(30);
    println!("My number is {:?}", num);
}
```

## `Into`

El trato [`Into`](#into) es simplemente el recíproco del trato `From`. Es decir, si ha implementado el trato `From` para su tipo, `Into` lo llamará cuando sea necesario.

Usar el trato `Into` generalmente requerirá especificar el tipo al que se desea convertir, ya que el compilador no puede determinarlo en la mayoría de los casos. Sin embargo, este es un pequeño inconveniente teniendo en cuenta que obtenemos la funcionalidad gratis.

```rust
use std::convert::Into;

#[derive(Debug)]
struct Number {
    value: i32,
}

impl Into<Number> for i32 {
    fn into(self) -> Number {
        Number { value: self }
    }
}

fn main() {
    let int = 5;
    // Intenta quitar la anotación de tipo
    let num: Number = int.into();
    println!("My number is {:?}", num);
}
```
