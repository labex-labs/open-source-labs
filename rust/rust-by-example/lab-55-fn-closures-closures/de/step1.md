# Closures

Closures sind Funktionen, die die umgebende Umgebung erfassen können. Beispielsweise eine Closure, die die Variable `x` erfassen würde:

```rust
|val| val + x
```

Die Syntax und die Funktionen von Closures machen sie sehr praktisch für das sofortige Verwenden. Ein Closure aufzurufen ist genauso wie eine Funktion aufzurufen. Allerdings können sowohl die Eingabe- als auch die Rückgabetypen _inferiert_ werden, und die Namen der Eingabevariablen _müssen_ angegeben werden.

Weitere Eigenschaften von Closures umfassen:

- Verwendung von `||` anstelle von `()` um die Eingabevariablen.
- optionale Körperabgrenzung (`{}`) für einen einzelnen Ausdruck (sonst obligatorisch).
- die Fähigkeit, die Variablen der äußeren Umgebung zu erfassen.

```rust
fn main() {
    let outer_var = 42;

    // Eine normale Funktion kann nicht auf Variablen in der umgebenden Umgebung verweisen
    //fn function(i: i32) -> i32 { i + outer_var }
    // TODO: Entkommentieren Sie die obige Zeile und sehen Sie sich den Compilerfehler an. Der Compiler
    // schlägt vor, dass wir stattdessen eine Closure definieren.

    // Closures sind anonym. Hier binden wir sie an Referenzen
    // Die Annotation ist identisch zur Funktionsannotation, aber optional
    // ebenso wie die `{}` um den Körper. Diese namenlosen Funktionen
    // werden an passend benannten Variablen zugewiesen.
    let closure_annotated = |i: i32| -> i32 { i + outer_var };
    let closure_inferred  = |i     |          i + outer_var  ;

    // Rufen Sie die Closures auf.
    println!("closure_annotated: {}", closure_annotated(1));
    println!("closure_inferred: {}", closure_inferred(1));
    // Sobald der Typ eines Closures inferiert wurde, kann er nicht erneut mit einem anderen Typ inferiert werden.
    //println!("cannot reuse closure_inferred with another type: {}", closure_inferred(42i64));
    // TODO: Entkommentieren Sie die obige Zeile und sehen Sie sich den Compilerfehler an.

    // Eine Closure, die keine Argumente nimmt und einen `i32` zurückgibt.
    // Der Rückgabetyp wird inferiert.
    let one = || 1;
    println!("closure returning one: {}", one());

}
```
