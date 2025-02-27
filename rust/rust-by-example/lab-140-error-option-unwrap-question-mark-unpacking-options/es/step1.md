# Desempaquetar opciones con `?`

Puedes desempaquetar `Option` utilizando declaraciones `match`, pero a menudo es más fácil utilizar el operador `?`. Si `x` es una `Option`, entonces evaluar `x?` devolverá el valor subyacente si `x` es `Some`, de lo contrario, terminará la función que se esté ejecutando y devolverá `None`.

```rust
fn next_birthday(current_age: Option<u8>) -> Option<String> {
    // Si `current_age` es `None`, esto devuelve `None`.
    // Si `current_age` es `Some`, el `u8` interno se asigna a `next_age`
    let next_age: u8 = current_age? + 1;
    Some(format!("Next year I will be {}", next_age))
}
```

Puedes encadenar muchos `?` juntos para hacer que tu código sea mucho más legible.

```rust
struct Person {
    job: Option<Job>,
}

#[derive(Clone, Copy)]
struct Job {
    phone_number: Option<PhoneNumber>,
}

#[derive(Clone, Copy)]
struct PhoneNumber {
    area_code: Option<u8>,
    number: u32,
}

impl Person {

    // Obtiene el código de área del número de teléfono del trabajo de la persona, si existe.
    fn work_phone_area_code(&self) -> Option<u8> {
        // Esto requeriría muchas declaraciones `match` anidadas sin el operador `?`.
        // Tomaría mucho más código - intenta escribirlo tú mismo y ver cuál
        // es más fácil.
        self.job?.phone_number?.area_code
    }
}

fn main() {
    let p = Person {
        job: Some(Job {
            phone_number: Some(PhoneNumber {
                area_code: Some(61),
                number: 439222222,
            }),
        }),
    };

    assert_eq!(p.work_phone_area_code(), Some(61));
}
```
