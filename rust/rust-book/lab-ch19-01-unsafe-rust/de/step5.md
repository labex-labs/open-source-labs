# Erstellen einer sicheren Abstraktion über unsafe Code

Das bloße Vorhandensein von unsafe Code in einer Funktion bedeutet noch lange nicht, dass wir die gesamte Funktion als unsafe markieren müssen. Tatsächlich ist das Einhüllen von unsafe Code in eine sichere Funktion eine häufige Abstraktion. Als Beispiel betrachten wir die `split_at_mut`-Funktion aus der Standardbibliothek, die ein gewisses unsafe Code benötigt. Wir werden untersuchen, wie wir sie implementieren könnten. Diese sichere Methode wird für mutable Slices definiert: Sie nimmt einen Slice und teilt ihn an der als Argument angegebenen Indexposition in zwei Teile auf. Listing 19-4 zeigt, wie man `split_at_mut` verwendet.

```rust
let mut v = vec![1, 2, 3, 4, 5, 6];

let r = &mut v[..];

let (a, b) = r.split_at_mut(3);

assert_eq!(a, &mut [1, 2, 3]);
assert_eq!(b, &mut [4, 5, 6]);
```

Listing 19-4: Verwenden der sicheren `split_at_mut`-Funktion

Wir können diese Funktion nicht nur mit safe Rust implementieren. Ein Versuch könnte wie in Listing 19-5 aussehen, was jedoch nicht kompilieren wird. Um die Darstellung einfacher zu halten, implementieren wir `split_at_mut` als Funktion statt als Methode und nur für Slices von `i32`-Werten statt für einen generischen Typ `T`.

```rust
fn split_at_mut(
    values: &mut [i32],
    mid: usize,
) -> (&mut [i32], &mut [i32]) {
    let len = values.len();

    assert!(mid <= len);

    (&mut values[..mid], &mut values[mid..])
}
```

Listing 19-5: Ein versuchter Versuch zur Implementierung von `split_at_mut` mit nur safe Rust

Diese Funktion bestimmt zunächst die Gesamtlänge des Slices. Anschließend wird überprüft, ob der als Parameter angegebene Index innerhalb des Slices liegt, indem überprüft wird, ob er kleiner oder gleich der Länge ist. Die Prüfung bedeutet, dass die Funktion im Falle eines Indexes, der größer als die Länge ist, um das Teilen des Slices, vor dem Versuch, diesen Index zu verwenden, abstürzt.

Anschließend geben wir zwei mutable Slices in einem Tuple zurück: Einer vom Anfang des ursprünglichen Slices bis zum `mid`-Index und ein anderer von `mid` bis zum Ende des Slices.

Wenn wir den Code in Listing 19-5 versuchen, zu kompilieren, erhalten wir einen Fehler:

```bash
error[E0499]: cannot borrow `*values` as mutable more than once at a time
 --> src/main.rs:9:31
  |
2 |     values: &mut [i32],
  |             - let's call the lifetime of this reference `'1`
...
9 |     (&mut values[..mid], &mut values[mid..])
  |     --------------------------^^^^^^--------
  |     |     |                   |
  |     |     |                   second mutable borrow occurs here
  |     |     first mutable borrow occurs here
  |     returning this value requires that `*values` is borrowed for `'1`
```

Der Borrow-Checker von Rust kann nicht verstehen, dass wir verschiedene Teile des Slices borrowen; er weiß nur, dass wir von demselben Slice zweimal borrowen. Das Borrowen von verschiedenen Teilen eines Slices ist grundsätzlich in Ordnung, da die beiden Slices nicht überlappen, aber Rust ist nicht intelligent genug, um das zu wissen. Wenn wir wissen, dass der Code in Ordnung ist, aber Rust es nicht, ist es an der Zeit, unsafe Code zu verwenden.

Listing 19-6 zeigt, wie man einen `unsafe`-Block, einen rohen Zeiger und einige Aufrufe von unsicheren Funktionen verwendet, um die Implementierung von `split_at_mut` zu machen.

```rust
use std::slice;

fn split_at_mut(
    values: &mut [i32],
    mid: usize,
) -> (&mut [i32], &mut [i32]) {
  1 let len = values.len();
  2 let ptr = values.as_mut_ptr();

  3 assert!(mid <= len);

  4 unsafe {
        (
          5 slice::from_raw_parts_mut(ptr, mid),
          6 slice::from_raw_parts_mut(ptr.add(mid), len - mid),
        )
    }
}
```

Listing 19-6: Verwenden von unsafe Code in der Implementierung der `split_at_mut`-Funktion

Denken wir uns aus "Der Slice-Typ" zurück, dass ein Slice ein Zeiger auf einige Daten und die Länge des Slices ist. Wir verwenden die `len`-Methode, um die Länge eines Slices zu erhalten \[1\] und die `as_mut_ptr`-Methode, um auf den rohen Zeiger eines Slices zuzugreifen \[2\]. Im Falle eines mutable Slices von `i32`-Werten gibt `as_mut_ptr` einen rohen Zeiger vom Typ `*mut i32` zurück, den wir in der Variable `ptr` gespeichert haben.

Wir behalten die Prüfung bei, dass der `mid`-Index innerhalb des Slices liegt \[3\]. Dann kommen wir zu dem unsafe Code \[4\]: Die `slice::from_raw_parts_mut`-Funktion nimmt einen rohen Zeiger und eine Länge und erstellt daraus einen Slice. Wir verwenden sie, um einen Slice zu erstellen, der bei `ptr` beginnt und `mid` Elemente lang ist \[5\]. Anschließend rufen wir die `add`-Methode auf `ptr` mit `mid` als Argument auf, um einen rohen Zeiger zu erhalten, der bei `mid` beginnt, und erstellen einen Slice mit diesem Zeiger und der verbleibenden Anzahl von Elementen nach `mid` als Länge \[6\].

Die Funktion `slice::from_raw_parts_mut` ist unsafe, weil sie einen rohen Zeiger nimmt und davon ausgehen muss, dass dieser Zeiger gültig ist. Die `add`-Methode auf rohen Zeigern ist ebenfalls unsafe, weil sie davon ausgehen muss, dass die Offsetposition ebenfalls ein gültiger Zeiger ist. Daher mussten wir einen `unsafe`-Block um unsere Aufrufe von `slice::from_raw_parts_mut` und `add` setzen, um sie aufrufen zu können. Indem wir den Code betrachten und die Prüfung hinzufügen, dass `mid` kleiner oder gleich `len` sein muss, können wir feststellen, dass alle rohen Zeiger, die innerhalb des `unsafe`-Blocks verwendet werden, gültige Zeiger auf Daten innerhalb des Slices sein werden. Dies ist eine akzeptable und angemessene Verwendung von `unsafe`.

Beachte, dass wir die resultierende `split_at_mut`-Funktion nicht als `unsafe` markieren müssen und wir diese Funktion aus safe Rust aufrufen können. Wir haben eine sichere Abstraktion für den unsafe Code mit einer Implementierung der Funktion erstellt, die unsafe Code auf sichere Weise verwendet, weil sie nur gültige Zeiger aus den Daten erstellt, auf die diese Funktion zugreift.

Im Gegensatz dazu würde die Verwendung von `slice::from_raw_parts_mut` in Listing 19-7 wahrscheinlich abstürzen, wenn der Slice verwendet wird. Dieser Code nimmt eine beliebige Speicheradresse und erstellt einen Slice, der 10.000 Elemente lang ist.

```rust
use std::slice;

let address = 0x01234usize;
let r = address as *mut i32;

let values: &[i32] = unsafe {
    slice::from_raw_parts_mut(r, 10000)
};
```

Listing 19-7: Erstellen eines Slices aus einer beliebigen Speicheradresse

Wir besitzen nicht den Speicher an dieser beliebigen Adresse, und es ist keine Garantie, dass der Slice, den dieser Code erstellt, gültige `i32`-Werte enthält. Das Versuchen, `values` als einen gültigen Slice zu verwenden, führt zu undefiniertem Verhalten.
