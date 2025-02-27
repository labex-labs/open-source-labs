# `TryFrom` und `TryInto`

Ähnlich wie `From` und `Into` sind \[`TryFrom`\] und \[`TryInto`\] generische Traits zur Konvertierung zwischen Typen. Im Gegensatz zu `From`/`Into` werden die `TryFrom`/`TryInto`-Traits für fehlerbehaftete Konvertierungen verwendet und geben daher \[`Result`\]s zurück.

```rust
use std::convert::TryFrom;
use std::convert::TryInto;

#[derive(Debug, PartialEq)]
struct EvenNumber(i32);

impl TryFrom<i32> for EvenNumber {
    type Error = ();

    fn try_from(value: i32) -> Result<Self, Self::Error> {
        if value % 2 == 0 {
            Ok(EvenNumber(value))
        } else {
            Err(())
        }
    }
}

fn main() {
    // TryFrom

    assert_eq!(EvenNumber::try_from(8), Ok(EvenNumber(8)));
    assert_eq!(EvenNumber::try_from(5), Err(()));

    // TryInto

    let result: Result<EvenNumber, ()> = 8i32.try_into();
    assert_eq!(result, Ok(EvenNumber(8)));
    let result: Result<EvenNumber, ()> = 5i32.try_into();
    assert_eq!(result, Err(()));
}
```
