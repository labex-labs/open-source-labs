# Verlassen von Schleifen

Einer der Anwendungen einer `loop`-Schleife besteht darin, eine Operation wiederholt auszuführen, bis sie erfolgreich ist. Wenn die Operation jedoch einen Wert zurückgibt, musst du ihn möglicherweise an den Rest des Codes weitergeben: platziere ihn nach dem `break`, und er wird von dem `loop`-Ausdruck zurückgegeben.

```rust
fn main() {
    let mut counter = 0;

    let result = loop {
        counter += 1;

        if counter == 10 {
            break counter * 2;
        }
    };

    assert_eq!(result, 20);
}
```
