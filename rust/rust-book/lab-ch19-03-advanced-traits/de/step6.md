# Verwendung des Newtype-Patterns, um externe Traits zu implementieren

In "Implementing a Trait on a Type" haben wir die Orphan-Regel erwähnt, die besagt, dass wir nur dann ein Trait auf einem Typ implementieren dürfen, wenn entweder das Trait oder der Typ oder beide unserem Kasten lokal sind. Es ist möglich, diese Einschränkung umgehen zu können, indem wir das _Newtype-Pattern_ verwenden, bei dem es darum geht, einen neuen Typ in einer Tuple-Struktur zu erstellen. (Wir haben Tuple-Strukturen in "Using Tuple Structs Without Named Fields to Create Different Types" behandelt.) Die Tuple-Struktur wird ein Feld haben und eine dünne Umhüllung des Typs sein, für den wir ein Trait implementieren möchten. Dann ist der Umhüllungstyp unserem Kasten lokal, und wir können das Trait auf der Umhüllung implementieren. _Newtype_ ist ein Begriff, der aus der Haskell-Programmiersprache stammt. Es entsteht keine Laufzeitleistungseinbuße bei der Verwendung dieses Musters, und der Umhüllungstyp wird zur Compile-Zeit weggelassen.

Als Beispiel sagen wir, dass wir `Display` auf `Vec<T>` implementieren möchten, was uns die Orphan-Regel direkt verwehrt, da das `Display`-Trait und der `Vec<T>`-Typ außerhalb unseres Kastens definiert sind. Wir können eine `Wrapper`-Struktur erstellen, die eine Instanz von `Vec<T>` enthält; dann können wir `Display` auf `Wrapper` implementieren und den `Vec<T>`-Wert verwenden, wie in Listing 19-23 gezeigt.

Dateiname: `src/main.rs`

```rust
use std::fmt;

struct Wrapper(Vec<String>);

impl fmt::Display for Wrapper {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "[{}]", self.0.join(", "))
    }
}

fn main() {
    let w = Wrapper(vec![
        String::from("hello"),
        String::from("world"),
    ]);
    println!("w = {w}");
}
```

Listing 19-23: Erstellen eines `Wrapper`-Typs um `Vec<String>`, um `Display` zu implementieren

Die Implementierung von `Display` verwendet `self.0`, um auf das innere `Vec<T>` zuzugreifen, da `Wrapper` eine Tuple-Struktur ist und `Vec<T>` das Element an Index 0 in der Tuple ist. Dann können wir die Funktionalität des `Display`-Typs auf `Wrapper` verwenden.

Der Nachteil der Verwendung dieser Technik ist, dass `Wrapper` ein neuer Typ ist, sodass er nicht die Methoden des Werts hat, den er enthält. Wir müssten alle Methoden von `Vec<T>` direkt auf `Wrapper` implementieren, sodass die Methoden an `self.0` delegieren, was uns ermöglichen würde, `Wrapper` genauso wie ein `Vec<T>` zu behandeln. Wenn wir wollten, dass der neue Typ alle Methoden des inneren Typs hat, wäre die Implementierung des `Deref`-Traits auf `Wrapper`, um den inneren Typ zurückzugeben, eine Lösung (wir haben die Implementierung des `Deref`-Traits in "Treating Smart Pointers Like Regular References with Deref" diskutiert). Wenn wir nicht wollten, dass der `Wrapper`-Typ alle Methoden des inneren Typs hat - beispielsweise, um das Verhalten des `Wrapper`-Typs einzuschränken - müssten wir nur die Methoden implementieren, die wir tatsächlich möchten, manuell.

Dieses Newtype-Pattern ist auch nützlich, auch wenn es um Traits nicht geht. Lassen Sie uns den Fokus wechseln und einige fortgeschrittene Wege betrachten, um mit dem Typsystem von Rust zu interagieren.
