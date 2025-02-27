# Konditionale if let-Ausdrücke

Im Kapitel 6 haben wir diskutiert, wie man `if let`-Ausdrücke hauptsächlich als eine kürzere Schreibweise für das Äquivalent eines `match` verwendet, das nur einen Fall abdeckt. Optionalerweise kann `if let` einen entsprechenden `else` enthalten, der Code enthält, der ausgeführt wird, wenn das Muster in `if let` nicht übereinstimmt.

Listing 18-1 zeigt, dass es auch möglich ist, `if let`, `else if` und `else if let`-Ausdrücke zu kombinieren. Dadurch haben wir mehr Flexibilität als bei einem `match`-Ausdruck, bei dem wir nur einen Wert angeben können, der mit den Mustern verglichen werden soll. Außerdem erfordert Rust nicht, dass die Bedingungen in einer Reihe von `if let`, `else if` und `else if let`-Armen miteinander in Beziehung stehen.

Der Code in Listing 18-1 bestimmt, welche Farbe für den Hintergrund verwendet werden soll, basierend auf einer Reihe von Prüfungen für mehrere Bedingungen. Für dieses Beispiel haben wir Variablen mit hartcodierten Werten erstellt, die ein reales Programm möglicherweise von der Benutzereingabe erhält.

Dateiname: `src/main.rs`

```rust
fn main() {
    let favorite_color: Option<&str> = None;
    let is_tuesday = false;
    let age: Result<u8, _> = "34".parse();

  1 if let Some(color) = favorite_color {
      2 println!(
            "Using your favorite, {color}, as the background"
        );
  3 } else if is_tuesday {
      4 println!("Tuesday is green day!");
  5 } else if let Ok(age) = age {
      6 if age > 30 {
          7 println!("Using purple as the background color");
        } else {
          8 println!("Using orange as the background color");
        }
  9 } else {
     10 println!("Using blue as the background color");
    }
}
```

Listing 18-1: Kombinieren von `if let`, `else if`, `else if let` und `else`

Wenn der Benutzer eine Lieblingsfarbe angibt \[1\], wird diese Farbe als Hintergrund verwendet \[2\]. Wenn keine Lieblingsfarbe angegeben ist und heute Dienstag ist \[3\], ist die Hintergrundfarbe grün \[4\]. Andernfalls, wenn der Benutzer sein Alter als Zeichenfolge angibt und wir es erfolgreich als Zahl analysieren können \[5\], ist die Farbe entweder lila \[7\] oder orange \[8\], je nachdem, was der Wert der Zahl ist \[6\]. Wenn keine dieser Bedingungen zutrifft \[9\], ist die Hintergrundfarbe blau \[10\].

Diese bedingte Struktur ermöglicht es uns, komplexe Anforderungen zu unterstützen. Mit den hier verwendeten hartcodierten Werten wird dieses Beispiel `Using purple as the background color` ausgeben.

Sie können sehen, dass `if let` auch in der gleichen Weise wie `match`-Arme shadowed Variablen einführen kann: Die Zeile `if let Ok(age) = age` \[5\] führt eine neue shadowed `age`-Variable ein, die den Wert innerhalb der `Ok`-Variante enthält. Dies bedeutet, dass wir die Bedingung `if age > 30` \[6\] innerhalb dieses Blocks platzieren müssen: Wir können diese beiden Bedingungen nicht zu `if let Ok(age) = age && age > 30` kombinieren. Die shadowed `age`, mit der wir mit 30 vergleichen möchten, ist erst gültig, wenn der neue Gültigkeitsbereich mit der geschweiften Klammer beginnt.

Der Nachteil von `if let`-Ausdrücken ist, dass der Compiler nicht auf Vollständigkeit überprüft, während dies bei `match`-Ausdrücken der Fall ist. Wenn wir den letzten `else`-Block \[9\] weglassen und somit einige Fälle unbehandelt lassen, wird uns der Compiler nicht auf den möglichen Logikfehler hinweisen.
