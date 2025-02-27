# Ein ganzes Element mit `_`

Wir haben das Unterstrich-Zeichen als Platzhalter-Muster verwendet, das jedem Wert entspricht, aber nicht an diesen gebunden wird. Dies ist besonders nützlich als letzter Arm in einem `match`-Ausdruck, aber wir können es auch in jedem Muster verwenden, einschließlich Funktionsparameter, wie in Listing 18-17 gezeigt.

Dateiname: `src/main.rs`

```rust
fn foo(_: i32, y: i32) {
    println!("Dieser Code verwendet nur den y-Parameter: {y}");
}

fn main() {
    foo(3, 4);
}
```

Listing 18-17: Verwendung von `_` in einer Funktionssignatur

Dieser Code ignoriert vollständig den Wert `3`, der als erster Argument übergeben wird, und gibt `Dieser Code verwendet nur den y-Parameter: 4` aus.

In den meisten Fällen, wenn Sie einen bestimmten Funktionsparameter nicht mehr benötigen, würden Sie die Signatur ändern, sodass der nicht verwendete Parameter nicht mehr enthalten ist. Das Ignorieren eines Funktionsparameters kann besonders nützlich sein, wenn Sie beispielsweise ein Merkmal implementieren und dabei eine bestimmte Typsignatur benötigen, aber der Funktionskörper in Ihrer Implementierung einen der Parameter nicht benötigt. Dadurch vermeiden Sie eine Compiler-Warnung über nicht verwendete Funktionsparameter, die Sie erhalten würden, wenn Sie stattdessen einen Namen verwenden würden.
