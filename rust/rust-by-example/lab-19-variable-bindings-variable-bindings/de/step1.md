# Variable Bindings

Rust bietet Typsicherheit durch statische Typisierung. Variable Bindings können bei der Deklaration mit einem Typ annotiert werden. In den meisten Fällen jedoch kann der Compiler den Typ der Variable aus dem Kontext ableiten, was die Annotationsbelastung erheblich reduziert.

Werte (wie Literale) können an Variablen gebunden werden, indem die `let`-Bindung verwendet wird.

```rust
fn main() {
    let an_integer = 1u32;
    let a_boolean = true;
    let unit = ();

    // Kopiere `an_integer` in `copied_integer`
    let copied_integer = an_integer;

    println!("An integer: {:?}", copied_integer);
    println!("A boolean: {:?}", a_boolean);
    println!("Meet the unit value: {:?}", unit);

    // Der Compiler weist vor, wenn Variable Bindings nicht verwendet werden; diese Warnungen können
    // durch Einfügen eines Unterstrichs am Anfang des Variablennamens unterdrückt werden
    let _unused_variable = 3u32;

    let noisy_unused_variable = 2u32;
    // FIXME ^ Füge einen Unterstrich hinzu, um die Warnung zu unterdrücken
    // Beachten Sie, dass Warnungen möglicherweise nicht im Browser angezeigt werden
}
```
