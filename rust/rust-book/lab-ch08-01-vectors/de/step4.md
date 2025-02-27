# Lesen von Elementen von Vektoren

Es gibt zwei Möglichkeiten, auf einen in einem Vektor gespeicherten Wert zu verweisen: über die Indizierung oder mithilfe der `get`-Methode. In den folgenden Beispielen haben wir die Typen der von diesen Funktionen zurückgegebenen Werte annotiert, um zusätzliche Klarheit zu schaffen.

Listing 8-4 zeigt beide Methoden, um auf einen Wert in einem Vektor zuzugreifen, mit der Indizierungssyntax und der `get`-Methode.

```rust
let v = vec![1, 2, 3, 4, 5];

1 let third: &i32 = &v[2];
println!("The third element is {third}");

2 let third: Option<&i32> = v.get(2);
match third  {
    Some(third) => println!("The third element is {third}"),
    None => println!("There is no third element."),
}
```

Listing 8-4: Verwenden der Indizierungssyntax und der `get`-Methode, um auf ein Element in einem Vektor zuzugreifen

Beachten Sie einige Details hier. Wir verwenden den Indexwert `2`, um das dritte Element zu erhalten \[1\], weil Vektoren von der Null beginnend nummeriert sind. Mit `&` und `[]` erhalten wir eine Referenz auf das Element mit dem Indexwert. Wenn wir die `get`-Methode mit dem als Argument übergebenen Index verwenden \[2\], erhalten wir ein `Option<&T>`, das wir mit `match` verwenden können.

Rust bietet diese zwei Möglichkeiten, um auf ein Element zu verweisen, damit Sie wählen können, wie das Programm reagiert, wenn Sie versuchen, einen Indexwert außerhalb des Bereichs der vorhandenen Elemente zu verwenden. Als Beispiel sehen wir uns an, was passiert, wenn wir einen Vektor mit fünf Elementen haben und dann versuchen, mit jeder Technik auf ein Element am Index 100 zuzugreifen, wie in Listing 8-5 gezeigt.

```rust
let v = vec![1, 2, 3, 4, 5];

let does_not_exist = &v[100];
let does_not_exist = v.get(100);
```

Listing 8-5: Versuchen, auf das Element am Index 100 in einem Vektor mit fünf Elementen zuzugreifen

Wenn wir diesen Code ausführen, wird die erste `[]`-Methode dazu führen, dass das Programm abstürzt, weil sie auf ein nicht existierendes Element verweist. Diese Methode eignet sich am besten, wenn Sie möchten, dass Ihr Programm abstürzt, wenn versucht wird, auf ein Element hinterhalb des Endes des Vektors zuzugreifen.

Wenn der `get`-Methode ein Index übergeben wird, der außerhalb des Vektors liegt, gibt sie `None` zurück, ohne zu abstürzen. Sie würden diese Methode verwenden, wenn es unter normalen Umständen gelegentlich möglich ist, auf ein Element außerhalb des Bereichs des Vektors zuzugreifen. Ihr Code wird dann Logik haben, um entweder `Some(&element)` oder `None` zu verarbeiten, wie im Kapitel 6 besprochen. Beispielsweise könnte der Index von einer Person eingegeben werden. Wenn sie versehentlich eine zu große Zahl eingeben und das Programm einen `None`-Wert erhält, können Sie der Benutzer mitteilen, wie viele Elemente sich derzeit im Vektor befinden, und ihnen eine weitere Möglichkeit geben, einen gültigen Wert einzugeben. Das wäre nutzerfreundlicher als das Abstürzen des Programms aufgrund eines Tippfehlers!

Wenn das Programm eine gültige Referenz hat, überwacht der Entleihensprüfer die Besitz- und Entleihregeln (beschrieben im Kapitel 4), um sicherzustellen, dass diese Referenz und alle anderen Referenzen auf den Inhalt des Vektors gültig bleiben. Erinnern Sie sich an die Regel, die besagt, dass Sie in einem gleichen Gültigkeitsbereich keine änderbare und nicht änderbare Referenz haben können. Diese Regel gilt in Listing 8-6, wo wir eine nicht änderbare Referenz auf das erste Element in einem Vektor halten und versuchen, ein Element am Ende hinzuzufügen. Dieses Programm wird nicht funktionieren, wenn wir auch später im Funktionskörper versuchen, auf jenes Element zu verweisen.

```rust
let mut v = vec![1, 2, 3, 4, 5];

let first = &v[0];

v.push(6);

println!("The first element is: {first}");
```

Listing 8-6: Versuchen, ein Element zu einem Vektor hinzuzufügen, während eine Referenz auf ein Element gehalten wird

Das Kompilieren dieses Codes führt zu diesem Fehler:

```bash
error[E0502]: cannot borrow `v` as mutable because it is also borrowed as
immutable
 --> src/main.rs:6:5
  |
4 |     let first = &v[0];
  |                  - immutable borrow occurs here
5 |
6 |     v.push(6);
  |     ^^^^^^^^^ mutable borrow occurs here
7 |
8 |     println!("The first element is: {first}");
  |                                      ----- immutable borrow later used here
```

Der Code in Listing 8-6 mag so aussehen, als sollte er funktionieren: Warum sollte eine Referenz auf das erste Element auf Änderungen am Ende des Vektors achten? Dieser Fehler liegt an der Art, wie Vektoren funktionieren: Da Vektoren die Werte nebeneinander im Speicher ablegen, kann das Hinzufügen eines neuen Elements am Ende des Vektors möglicherweise erforderlich machen, neues Speicher zuzuweisen und die alten Elemente in den neuen Speicherbereich zu kopieren, wenn nicht genug Platz vorhanden ist, um alle Elemente nebeneinander an der aktuellen Speicherposition des Vektors zu platzieren. In diesem Fall würde die Referenz auf das erste Element auf deallokierten Speicher verweisen. Die Entleihregeln verhindern, dass Programme in diese Situation geraten.

> Hinweis: Für weitere Informationen über die Implementierungsdetails des `Vec<T>`-Typs siehe "The Rustonomicon" unter *https://doc.rust-lang.org/nomicon/vec/vec.html*.
