# Der Arraytyp

Eine andere Möglichkeit, eine Sammlung von mehreren Werten zu haben, ist ein _Array_. Im Gegensatz zu einem Tupel muss jedes Element eines Arrays den gleichen Typ haben. Im Gegensatz zu Arrays in einigen anderen Sprachen haben Arrays in Rust eine feste Länge.

Wir schreiben die Werte in einem Array als komma-getrennte Liste in eckigen Klammern:

Dateiname: `src/main.rs`

```rust
fn main() {
    let a = [1, 2, 3, 4, 5];
}
```

Arrays sind nützlich, wenn Sie möchten, dass Ihre Daten auf dem Stapel und nicht auf dem Heap gespeichert werden (wir werden den Stapel und den Heap im Kapitel 4 genauer besprechen) oder wenn Sie sicherstellen möchten, dass Sie immer eine feste Anzahl von Elementen haben. Ein Array ist jedoch nicht so flexibel wie der Vektor-Typ. Ein _Vektor_ ist eine ähnliche Sammlungstyp, der von der Standardbibliothek bereitgestellt wird und der in der Größe wachsen oder schrumpfen darf. Wenn Sie unsicher sind, ob Sie ein Array oder einen Vektor verwenden sollten, ist es wahrscheinlich ratsam, einen Vektor zu verwenden. Kapitel 8 behandelt Vektoren im Detail.

Arrays sind jedoch nützlicher, wenn Sie wissen, dass die Anzahl der Elemente nicht geändert werden muss. Beispielsweise würden Sie wahrscheinlich bei Verwendung der Monatsnamen in einem Programm ein Array statt eines Vektors verwenden, da Sie wissen, dass es immer 12 Elemente enthalten wird:

```rust
let months = ["January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"];
```

Sie schreiben den Typ eines Arrays mit eckigen Klammern, dem Typ jedes Elements, einem Semikolon und dann der Anzahl der Elemente im Array, wie folgt:

```rust
let a: [i32; 5] = [1, 2, 3, 4, 5];
```

Hier ist `i32` der Typ jedes Elements. Nach dem Semikolon gibt die Zahl `5` an, dass das Array fünf Elemente enthält.

Sie können auch ein Array initialisieren, sodass jedes Element den gleichen Wert enthält, indem Sie den Anfangswert angeben, gefolgt von einem Semikolon und dann der Länge des Arrays in eckigen Klammern, wie hier gezeigt:

```rust
let a = [3; 5];
```

Das Array mit dem Namen `a` wird fünf Elemente enthalten, die alle zunächst auf den Wert `3` gesetzt werden. Dies ist das Gleiche wie `let a = [3, 3, 3, 3, 3];`, aber in einer kürzeren Schreibweise.
