# Berechnen der Größe eines nicht-rekursiven Typs

Denken Sie sich das `Message`-Enum aus Listing 6-2 zurück, das wir im Kapitel 6 bei der Diskussion von Enum-Definitionen definiert haben:

```rust
enum Message {
    Quit,
    Move { x: i32, y: i32 },
    Write(String),
    ChangeColor(i32, i32, i32),
}
```

Um zu bestimmen, wie viel Speicher für einen `Message`-Wert zuzuweisen ist, geht Rust durch jede der Varianten, um zu sehen, welche Variante den meisten Speicher benötigt. Rust erkennt, dass `Message::Quit` keinen Speicher benötigt, `Message::Move` genug Speicher für zwei `i32`-Werte benötigt und so weiter. Da nur eine Variante verwendet werden wird, ist der größte Speicher, den ein `Message`-Wert benötigen wird, der Speicher, den es braucht, um die größte seiner Varianten zu speichern.

Vergleichen Sie dies mit dem, was passiert, wenn Rust versucht, zu bestimmen, wie viel Speicher ein rekursiver Typ wie das `List`-Enum in Listing 15-2 benötigt. Der Compiler beginnt mit der Betrachtung der `Cons`-Variante, die einen Wert vom Typ `i32` und einen Wert vom Typ `List` enthält. Daher benötigt `Cons` eine Speichergröße, die der Größe eines `i32` plus der Größe eines `List` entspricht. Um herauszufinden, wie viel Speicher der `List`-Typ benötigt, betrachtet der Compiler die Varianten, beginnend mit der `Cons`-Variante. Die `Cons`-Variante enthält einen Wert vom Typ `i32` und einen Wert vom Typ `List`, und dieser Prozess geht endlos weiter, wie in Abbildung 15-1 gezeigt.

Abbildung 15-1: Eine unendliche `List` bestehend aus unendlichen `Cons`-Varianten
