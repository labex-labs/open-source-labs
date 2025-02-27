# Déballez les options avec `?`

Vous pouvez déballer les `Option` en utilisant des instructions `match`, mais il est souvent plus facile d'utiliser l'opérateur `?`. Si `x` est une `Option`, alors l'évaluation de `x?` retournera la valeur sous-jacente si `x` est `Some`, sinon elle terminera la fonction en cours d'exécution et retournera `None`.

```rust
fn next_birthday(current_age: Option<u8>) -> Option<String> {
    // Si `current_age` est `None`, cela retourne `None`.
    // Si `current_age` est `Some`, l'`u8` interne est assigné à `next_age`
    let next_age: u8 = current_age? + 1;
    Some(format!("Next year I will be {}", next_age))
}
```

Vous pouvez chaîner plusieurs `?` pour rendre votre code beaucoup plus lisible.

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

    // Obtient le code d'aire du numéro de téléphone du travail de la personne, s'il existe.
    fn work_phone_area_code(&self) -> Option<u8> {
        // Cela nécessiterait de nombreuses instructions `match` imbriquées sans l'opérateur `?`.
        // Cela nécessiterait beaucoup plus de code - essayez de l'écrire vous-même et voyez lequel
        // est plus facile.
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
