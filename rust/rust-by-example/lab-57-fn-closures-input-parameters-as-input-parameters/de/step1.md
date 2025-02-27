# Als Eingabeparameter

Während Rust in der Regel die Art der Variablenfassung ohne Typangabe auf dem Laufenden bestimmt, ist diese Mehrdeutigkeit bei der Schreibung von Funktionen nicht erlaubt. Wenn eine Closure als Eingabeparameter verwendet wird, muss der vollständige Typ der Closure mithilfe eines der folgenden `Traits` annotiert werden. Diese werden durch die Art der Verwendung des eingefangenen Werts in der Closure bestimmt. In abnehmender Reihenfolge der Einschränkung sind dies:

- `Fn`: Die Closure verwendet den eingefangenen Wert per Referenz (`&T`)
- `FnMut`: Die Closure verwendet den eingefangenen Wert per mutabler Referenz (`&mut T`)
- `FnOnce`: Die Closure verwendet den eingefangenen Wert per Wert (`T`)

Variablenweise wird der Compiler die Variablen in der am wenigsten restriktiven Weise fassen.

Betrachten Sie beispielsweise einen Parameter, der als `FnOnce` annotiert ist. Dies besagt, dass die Closure den Wert möglicherweise per `&T`, `&mut T` oder `T` fangen kann, aber der Compiler wählt letztendlich basierend auf der Verwendung der eingefangenen Variablen in der Closure.

Dies liegt daran, dass wenn eine Verschiebung möglich ist, auch jede Art von Verweis möglich sein sollte. Beachten Sie, dass die Umkehrung nicht zutrifft. Wenn der Parameter als `Fn` annotiert ist, ist es nicht möglich, Variablen per `&mut T` oder `T` zu fangen. Allerdings ist `&T` möglich.

Im folgenden Beispiel können Sie versuchen, die Verwendung von `Fn`, `FnMut` und `FnOnce` zu tauschen, um zu sehen, was passiert:

```rust
// Eine Funktion, die eine Closure als Argument nimmt und aufruft.
// <F> bedeutet, dass F ein "Generischer Typparameter" ist
fn apply<F>(f: F) where
    // Die Closure nimmt keine Eingabe und gibt nichts zurück.
    F: FnOnce() {
    // ^ TODO: Versuchen Sie, dies in `Fn` oder `FnMut` zu ändern.

    f();
}

// Eine Funktion, die eine Closure nimmt und einen `i32` zurückgibt.
fn apply_to_3<F>(f: F) -> i32 where
    // Die Closure nimmt einen `i32` und gibt einen `i32` zurück.
    F: Fn(i32) -> i32 {

    f(3)
}

fn main() {
    use std::mem;

    let greeting = "hello";
    // Ein nicht kopierbarer Typ.
    // `to_owned` erstellt von einem referenzierten Datum ein eigenes
    let mut farewell = "goodbye".to_owned();

    // Fang 2 Variablen ein: `greeting` per Referenz und
    // `farewell` per Wert.
    let diary = || {
        // `greeting` ist per Referenz: erfordert `Fn`.
        println!("Ich sagte {}.", greeting);

        // Die Mutation zwingt `farewell`, per mutabler
        // Referenz eingefangen zu werden. Jetzt erfordert es `FnMut`.
        farewell.push_str("!!!");
        println!("Dann schrie ich {}.", farewell);
        println!("Jetzt kann ich schlafen. zzzzz");

        // Manuelles Aufrufen von drop zwingt `farewell`,
        // per Wert eingefangen zu werden. Jetzt erfordert es `FnOnce`.
        mem::drop(farewell);
    };

    // Rufe die Funktion auf, die die Closure anwendet.
    apply(diary);

    // `double` erfüllt die Trait-Bedingung von `apply_to_3`
    let double = |x| 2 * x;

    println!("3 verdoppelt: {}", apply_to_3(double));
}
```
