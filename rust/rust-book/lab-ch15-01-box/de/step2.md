# Verwenden von `Box<T>`{=html} um Daten auf dem Heap zu speichern

Bevor wir uns dem Use Case der Heap-Speicherung für `Box<T>` widmen, besprechen wir die Syntax und die Interaktion mit den Werten, die in einem `Box<T>` gespeichert sind.

Listing 15-1 zeigt, wie man eine Box verwendet, um einen `i32`-Wert auf dem Heap zu speichern.

Dateiname: `src/main.rs`

```rust
fn main() {
    let b = Box::new(5);
    println!("b = {b}");
}
```

Listing 15-1: Speichern eines `i32`-Werts auf dem Heap mit einer Box

Wir definieren die Variable `b` als Wert einer Box, die auf den Wert `5` zeigt, der auf dem Heap zugewiesen ist. Dieses Programm wird `b = 5` ausgeben; in diesem Fall können wir auf die Daten in der Box zugreifen, ähnlich wie wenn diese Daten auf dem Stack wären. Genau wie jeder besitzende Wert wird eine Box, wenn sie außer Gültigkeitsbereich gelangt, wie dies am Ende von `main` für `b` der Fall ist, deallokiert. Die Deallokierung erfolgt sowohl für die Box (gespeichert auf dem Stack) als auch für die von ihr referenzierten Daten (gespeichert auf dem Heap).

Das Speichern eines einzelnen Werts auf dem Heap ist nicht sehr nützlich, daher werden Sie Boxen nicht sehr oft in dieser Weise alleine verwenden. Das Speichern von Werten wie einem einzelnen `i32` auf dem Stack, wo sie standardmäßig gespeichert werden, ist in den meisten Fällen passender. Schauen wir uns einen Fall an, in dem Boxen uns ermöglichen, Typen zu definieren, die wir nicht definieren könnten, wenn wir keine Boxen hätten.
