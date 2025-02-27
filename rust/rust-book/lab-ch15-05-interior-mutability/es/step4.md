# Un Caso de Uso para la Mutabilidad Interior: Objetos de Simulación

A veces, durante las pruebas, un programador usará un tipo en lugar de otro tipo, con el fin de observar un comportamiento particular y afirmar que está implementado correctamente. Este tipo de marcador de posición se llama _doble de prueba_. Piénsalo en el sentido de un doble de actuación en el cine, donde una persona entra y sustituye a un actor para hacer una escena particularmente complicada. Los dobles de prueba sustituyen a otros tipos cuando estamos ejecutando pruebas. Los _objetos de simulación_ son tipos específicos de dobles de prueba que registran lo que sucede durante una prueba para que puedas afirmar que se llevaron a cabo las acciones correctas.

Rust no tiene objetos en el mismo sentido que otros lenguajes y no tiene la funcionalidad de objetos de simulación integrada en la biblioteca estándar como lo hacen algunos otros lenguajes. Sin embargo, definitivamente puedes crear una estructura que servirá para los mismos fines que un objeto de simulación.

Aquí está el escenario que probaremos: crearemos una biblioteca que sigue un valor en relación con un valor máximo y envía mensajes según qué tan cerca del valor máximo está el valor actual. Esta biblioteca podría usarse, por ejemplo, para controlar la cuota de un usuario para el número de llamadas API que se le permite hacer.

Nuestra biblioteca solo proporcionará la funcionalidad de controlar qué tan cerca del máximo está un valor y cuáles deben ser los mensajes en cada momento. Las aplicaciones que usen nuestra biblioteca se esperará que proporcionen el mecanismo para enviar los mensajes: la aplicación podría poner un mensaje en la aplicación, enviar un correo electrónico, enviar un mensaje de texto o hacer algo más. La biblioteca no necesita saber ese detalle. Todo lo que necesita es algo que implemente un trato que proporcionaremos llamado `Messenger`. La Lista 15-20 muestra el código de la biblioteca.

Nombre de archivo: `src/lib.rs`

```rust
pub trait Messenger {
  1 fn send(&self, msg: &str);
}

pub struct LimitTracker<'a, T: Messenger> {
    messenger: &'a T,
    value: usize,
    max: usize,
}

impl<'a, T> LimitTracker<'a, T>
where
    T: Messenger,
{
    pub fn new(
        messenger: &'a T,
        max: usize
    ) -> LimitTracker<'a, T> {
        LimitTracker {
            messenger,
            value: 0,
            max,
        }
    }

  2 pub fn set_value(&mut self, value: usize) {
        self.value = value;

        let percentage_of_max =
            self.value as f64 / self.max as f64;

        if percentage_of_max >= 1.0 {
            self.messenger
             .send("Error: You are over your quota!");
        } else if percentage_of_max >= 0.9 {
            self.messenger
             .send("Urgent: You're at 90% of your quota!");
        } else if percentage_of_max >= 0.75 {
            self.messenger
             .send("Warning: You're at 75% of your quota!");
        }
    }
}
```

Lista 15-20: Una biblioteca para controlar qué tan cerca está un valor de un valor máximo y advertir cuando el valor está en ciertos niveles

Una parte importante de este código es que el trato `Messenger` tiene un método llamado `send` que toma una referencia inmutable a `self` y el texto del mensaje \[1\]. Este trato es la interfaz que nuestro objeto de simulación necesita implementar para que se pueda usar el objeto de simulación de la misma manera que un objeto real. La otra parte importante es que queremos probar el comportamiento del método `set_value` en el `LimitTracker` \[2\]. Podemos cambiar lo que pasamos para el parámetro `value`, pero `set_value` no devuelve nada para lo que podamos hacer afirmaciones. Queremos poder decir que si creamos un `LimitTracker` con algo que implemente el trato `Messenger` y un valor particular para `max`, cuando pasamos diferentes números para `value` se le dice al mensajero que envíe los mensajes adecuados.

Necesitamos un objeto de simulación que, en lugar de enviar un correo electrónico o un mensaje de texto cuando llamamos a `send`, solo registrará los mensajes que se le dicen que envíe. Podemos crear una nueva instancia del objeto de simulación, crear un `LimitTracker` que use el objeto de simulación, llamar al método `set_value` en `LimitTracker` y luego comprobar que el objeto de simulación tenga los mensajes que esperamos. La Lista 15-21 muestra un intento de implementar un objeto de simulación para hacer exactamente eso, pero el verificador de préstamos no lo permitirá.

Nombre de archivo: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;

  1 struct MockMessenger {
      2 sent_messages: Vec<String>,
    }

    impl MockMessenger {
      3 fn new() -> MockMessenger {
            MockMessenger {
                sent_messages: vec![],
            }
        }
    }

  4 impl Messenger for MockMessenger {
        fn send(&self, message: &str) {
          5 self.sent_messages.push(String::from(message));
        }
    }

    #[test]
  6 fn it_sends_an_over_75_percent_warning_message() {
        let mock_messenger = MockMessenger::new();
        let mut limit_tracker = LimitTracker::new(
            &mock_messenger,
            100
        );

        limit_tracker.set_value(80);

        assert_eq!(mock_messenger.sent_messages.len(), 1);
    }
}
```

Lista 15-21: Un intento de implementar un `MockMessenger` que no está permitido por el verificador de préstamos

Este código de prueba define una estructura `MockMessenger` \[1\] que tiene un campo `sent_messages` con un `Vec` de valores `String` \[2\] para registrar los mensajes que se le dicen que envíe. También definimos una función asociada `new` \[3\] para facilitar la creación de nuevos valores de `MockMessenger` que empiecen con una lista vacía de mensajes. Luego implementamos el trato `Messenger` para `MockMessenger` \[4\] para que podamos dar un `MockMessenger` a un `LimitTracker`. En la definición del método `send` \[5\], tomamos el mensaje pasado como parámetro y lo almacenamos en la lista `sent_messages` de `MockMessenger`.

En la prueba, estamos probando lo que sucede cuando se le dice a `LimitTracker` que establezca `value` en algo que es más del 75 por ciento del valor `max` \[6\]. Primero creamos un nuevo `MockMessenger`, que comenzará con una lista vacía de mensajes. Luego creamos un nuevo `LimitTracker` y le damos una referencia al nuevo `MockMessenger` y un valor `max` de `100`. Llamamos al método `set_value` en el `LimitTracker` con un valor de `80`, que es más del 75 por ciento de 100. Luego afirmamos que la lista de mensajes que está registrando `MockMessenger` ahora debería tener un mensaje en ella.

Sin embargo, hay un problema con esta prueba, como se muestra aquí:

```bash
error[E0596]: no se puede prestar `self.sent_messages` como mutable, ya que está detrás de una
`&` referencia
  --> src/lib.rs:58:13
   |
2  |     fn send(&self, msg: &str);
   |             ----- ayuda: considere cambiar eso a ser una referencia mutable:
`&mut self`
...
58 |             self.sent_messages.push(String::from(message));
   |             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ `self` es una
`&` referencia, por lo que los datos a los que se refiere no se pueden prestar como mutable
```

No podemos modificar el `MockMessenger` para registrar los mensajes porque el método `send` toma una referencia inmutable a `self`. Tampoco podemos tomar la sugerencia del texto del error para usar `&mut self` en su lugar porque entonces la firma de `send` no coincidiría con la firma en la definición del trato `Messenger` (siéntase libre de probarlo y ver qué mensaje de error obtiene).

Esta es una situación en la que la mutabilidad interior puede ayudar! Almacenaremos los `sent_messages` dentro de un `RefCell<T>`, y luego el método `send` será capaz de modificar `sent_messages` para almacenar los mensajes que hemos visto. La Lista 15-22 muestra cómo se ve eso.

Nombre de archivo: `src/lib.rs`

```rust
#[cfg(test)]
mod tests {
    use super::*;
    use std::cell::RefCell;

    struct MockMessenger {
      1 sent_messages: RefCell<Vec<String>>,
    }

    impl MockMessenger {
        fn new() -> MockMessenger {
            MockMessenger {
              2 sent_messages: RefCell::new(vec![]),
            }
        }
    }

    impl Messenger for MockMessenger {
        fn send(&self, message: &str) {
            self.sent_messages
              3.borrow_mut()
               .push(String::from(message));
        }
    }

    #[test]
    fn it_sends_an_over_75_percent_warning_message() {
        --snip--

        assert_eq!(
          4 mock_messenger.sent_messages.borrow().len(),
            1
        );
    }
}
```

Lista 15-22: Usando `RefCell<T>` para mutar un valor interno mientras el valor externo se considera inmutable

El campo `sent_messages` ahora es del tipo `RefCell<Vec<String>>` \[1\] en lugar de `Vec<String>`. En la función `new`, creamos una nueva instancia de `RefCell<Vec<String>>` alrededor del vector vacío \[2\].

Para la implementación del método `send`, el primer parámetro sigue siendo una préstamo inmutable de `self`, lo que coincide con la definición del trato. Llamamos a `borrow_mut` en el `RefCell<Vec<String>>` en `self.sent_messages` \[3\] para obtener una referencia mutable al valor dentro del `RefCell<Vec<String>>`, que es el vector. Luego podemos llamar a `push` en la referencia mutable al vector para registrar los mensajes enviados durante la prueba.

El último cambio que tenemos que hacer es en la afirmación: para ver cuántos elementos hay en el vector interno, llamamos a `borrow` en el `RefCell<Vec<String>>` para obtener una referencia inmutable al vector \[4\].

Ahora que has visto cómo usar `RefCell<T>`, profundicemos en cómo funciona!
