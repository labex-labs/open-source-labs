# Eine nicht genutzte Variable, indem man ihren Namen mit einem Unterstrich beginnt

Wenn Sie eine Variable erstellen, aber sie nirgends verwenden, wird Rust normalerweise eine Warnung ausgeben, da eine nicht genutzte Variable ein Fehler sein könnte. Manchmal ist es jedoch nützlich, eine Variable zu erstellen, die man noch nicht verwenden möchte, z.B. wenn man prototypiert oder gerade ein Projekt beginnt. In dieser Situation können Sie Rust mitteilen, dass Sie keine Warnung über die nicht genutzte Variable erhalten möchten, indem Sie den Variablennamen mit einem Unterstrich beginnen. In Listing 18-20 erstellen wir zwei nicht genutzte Variablen, aber wenn wir diesen Code kompilieren, sollten wir nur eine Warnung über eine von ihnen erhalten.

Dateiname: `src/main.rs`

```rust
fn main() {
    let _x = 5;
    let y = 10;
}
```

Listing 18-20: Beginnen eines Variablennamens mit einem Unterstrich, um Warnungen über nicht genutzte Variablen zu vermeiden

Hier erhalten wir eine Warnung darüber, dass die Variable `y` nicht verwendet wird, aber keine Warnung darüber, dass `_x` nicht verwendet wird.

Beachten Sie, dass es einen subtilen Unterschied zwischen der Verwendung von nur `_` und der Verwendung eines Namens, der mit einem Unterstrich beginnt, gibt. Die Syntax `_x` bindet immer noch den Wert an die Variable, während `_` überhaupt nicht bindet. Um einen Fall zu zeigen, in dem diese Unterscheidung wichtig ist, wird Listing 18-21 uns einen Fehler liefern.

Dateiname: `src/main.rs`

```rust
let s = Some(String::from("Hello!"));

if let Some(_s) = s {
    println!("found a string");
}

println!("{:?}", s);
```

Listing 18-21: Eine nicht genutzte Variable, die mit einem Unterstrich beginnt, bindet immer noch den Wert, was möglicherweise die Eigentumsgewalt über den Wert erlangt.

Wir erhalten einen Fehler, da der Wert von `s` immer noch in `_s` bewegt wird, was es uns verhindert, `s` erneut zu verwenden. Verwenden Sie jedoch das Unterstrich-Zeichen allein, umbindet es niemals an den Wert. Listing 18-22 wird ohne Fehler kompiliert, da `s` nicht in `_` bewegt wird.

Dateiname: `src/main.rs`

```rust
let s = Some(String::from("Hello!"));

if let Some(_) = s {
    println!("found a string");
}

println!("{:?}", s);
```

Listing 18-22: Verwenden eines Unterstrich-Zeichens bindet nicht den Wert.

Dieser Code funktioniert einwandfrei, da wir `s` niemals an etwas binden; es wird nicht bewegt.
