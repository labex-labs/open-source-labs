# Entpacken von Optionen mit `?`

Sie können `Option`s mithilfe von `match`-Anweisungen entpacken, aber es ist oft einfacher, den `?`-Operator zu verwenden. Wenn `x` eine `Option` ist, dann wird die Auswertung von `x?` den zugrunde liegenden Wert zurückgeben, wenn `x` `Some` ist, andernfalls wird die Funktion, die ausgeführt wird, abgebrochen und `None` zurückgegeben.

```rust
fn next_birthday(current_age: Option<u8>) -> Option<String> {
    // Wenn `current_age` `None` ist, wird `None` zurückgegeben.
    // Wenn `current_age` `Some` ist, wird der innere `u8` an `next_age` zugewiesen
    let next_age: u8 = current_age? + 1;
    Some(format!("Next year I will be {}", next_age))
}
```

Sie können mehrere `?` hintereinander verketten, um Ihren Code viel lesbarer zu machen.

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

    // Holt die Vorwahl der Telefonnummer des Jobs der Person, wenn vorhanden.
    fn work_phone_area_code(&self) -> Option<u8> {
        // Ohne den `?`-Operator bräuchten hier viele geschachtelte `match`-Anweisungen.
        // Es würde viel mehr Code benötigen - versuchen Sie es selbst zu schreiben und sehen Sie,
        // welche Variante einfacher ist.
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
