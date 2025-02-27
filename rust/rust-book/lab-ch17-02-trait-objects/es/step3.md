# Implementando el Trato

Ahora agregaremos algunos tipos que implementen el trato `Draw`. Proporcionaremos el tipo `Button`. Una vez más, implementar en realidad una biblioteca GUI está fuera del alcance de este libro, por lo que el método `draw` no tendrá ninguna implementación útil en su cuerpo. Para imaginar cómo podría ser la implementación, un struct `Button` podría tener campos para `width`, `height` y `label`, como se muestra en la Lista 17-7.

Nombre de archivo: `src/lib.rs`

```rust
pub struct Button {
    pub width: u32,
    pub height: u32,
    pub label: String,
}

impl Draw for Button {
    fn draw(&self) {
        // código para realmente dibujar un botón
    }
}
```

Lista 17-7: Un struct `Button` que implementa el trato `Draw`

Los campos `width`, `height` y `label` en `Button` difirán de los campos en otros componentes; por ejemplo, un tipo `TextField` podría tener esos mismos campos más un campo `placeholder`. Cada uno de los tipos que queremos dibujar en la pantalla implementará el trato `Draw` pero usará código diferente en el método `draw` para definir cómo dibujar ese tipo particular, como lo tiene `Button` aquí (sin el código GUI real, como se mencionó). El tipo `Button`, por ejemplo, podría tener un bloque `impl` adicional que contenga métodos relacionados con lo que sucede cuando un usuario hace clic en el botón. Este tipo de métodos no se aplicará a tipos como `TextField`.

Si alguien que usa nuestra biblioteca decide implementar un struct `SelectBox` que tiene campos `width`, `height` y `options`, también implementarán el trato `Draw` en el tipo `SelectBox`, como se muestra en la Lista 17-8.

Nombre de archivo: `src/main.rs`

```rust
use gui::Draw;

struct SelectBox {
    width: u32,
    height: u32,
    options: Vec<String>,
}

impl Draw for SelectBox {
    fn draw(&self) {
        // código para realmente dibujar una caja de selección
    }
}
```

Lista 17-8: Otro crat que usa `gui` e implementa el trato `Draw` en un struct `SelectBox`

El usuario de nuestra biblioteca ahora puede escribir su función `main` para crear una instancia de `Screen`. A la instancia de `Screen`, pueden agregar una `SelectBox` y un `Button` poniendo cada uno en un `Box<T>` para convertirse en un objeto de trato. Luego pueden llamar al método `run` en la instancia de `Screen`, que llamará a `draw` en cada uno de los componentes. La Lista 17-9 muestra esta implementación.

Nombre de archivo: `src/main.rs`

```rust
use gui::{Button, Screen};

fn main() {
    let screen = Screen {
        components: vec![
            Box::new(SelectBox {
                width: 75,
                height: 10,
                options: vec![
                    String::from("Yes"),
                    String::from("Maybe"),
                    String::from("No"),
                ],
            }),
            Box::new(Button {
                width: 50,
                height: 10,
                label: String::from("OK"),
            }),
        ],
    };

    screen.run();
}
```

Lista 17-9: Usando objetos de trato para almacenar valores de diferentes tipos que implementan el mismo trato

Cuando escribimos la biblioteca, no sabíamos que alguien podría agregar el tipo `SelectBox`, pero la implementación de `Screen` fue capaz de operar en el nuevo tipo y dibujarlo porque `SelectBox` implementa el trato `Draw`, lo que significa que implementa el método `draw`.

Este concepto, de preocuparse solo por los mensajes a los que responde un valor en lugar del tipo concreto del valor, es similar al concepto de _duck typing_ en los lenguajes de tipado dinámico: si camina como un pato y cuac como un pato, entonces debe ser un pato! En la implementación de `run` en `Screen` en la Lista 17-5, `run` no necesita saber cuál es el tipo concreto de cada componente. No verifica si un componente es una instancia de un `Button` o un `SelectBox`, simplemente llama al método `draw` en el componente. Al especificar `Box<dyn Draw>` como el tipo de los valores en el vector `components`, hemos definido `Screen` para necesitar valores en los que podemos llamar al método `draw`.

La ventaja de usar objetos de trato y el sistema de tipos de Rust para escribir código similar al código que usa duck typing es que nunca tenemos que verificar si un valor implementa un método particular en tiempo de ejecución o preocuparnos por obtener errores si un valor no implementa un método pero lo llamamos de todos modos. Rust no compilará nuestro código si los valores no implementan los tratados que necesitan los objetos de trato.

Por ejemplo, la Lista 17-10 muestra lo que sucede si intentamos crear un `Screen` con una `String` como componente.

Nombre de archivo: `src/main.rs`

```rust
use gui::Screen;

fn main() {
    let screen = Screen {
        components: vec![Box::new(String::from("Hi"))],
    };

    screen.run();
}
```

Lista 17-10: Intentando usar un tipo que no implementa el trato del objeto de trato

Obtendremos este error porque `String` no implementa el trato `Draw`:

```bash
error[E0277]: the trait bound `String: Draw` is not satisfied
 --> src/main.rs:5:26
  |
5 |         components: vec![Box::new(String::from("Hi"))],
  |                          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^ the trait `Draw` is
not implemented for `String`
  |
  = note: required for the cast to the object type `dyn Draw`
```

Este error nos avisa de que ya sea que estemos pasando algo a `Screen` que no queríamos pasar y por lo tanto deberíamos pasar un tipo diferente, o que deberíamos implementar `Draw` en `String` para que `Screen` sea capaz de llamar a `draw` en ella.
