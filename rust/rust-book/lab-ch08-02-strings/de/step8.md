# Interne Darstellung

Ein `String` ist eine Umhüllung über ein `Vec<u8>`. Schauen wir uns einige unserer korrekt codierten UTF-8-Beispielstrings aus Listing 8-14 an. Zunächst diesen:

```rust
let hello = String::from("Hola");
```

In diesem Fall wird `len` `4` sein, was bedeutet, dass der Vektor, der den String `"Hola"` speichert, 4 Bytes lang ist. Jeder dieser Buchstaben nimmt ein Byte bei der UTF-8-Codierung ein. Die folgende Zeile mag Sie jedoch überraschen (achten Sie darauf, dass dieser String mit dem großen kyrillischen Buchstaben _Ze_, nicht der arabischen Zahl 3 beginnt):

```rust
let hello = String::from("Здравствуйте");
```

Wenn Sie gefragt würden, wie lang der String ist, würden Sie vielleicht 12 sagen. Tatsächlich ist Rust's Antwort 24: das ist die Anzahl der Bytes, die es braucht, um "Здравствуйте" in UTF-8 zu codieren, weil jeder Unicode-Skalarwert in diesem String 2 Bytes Speicherplatz nimmt. Daher wird ein Index in die Bytes des Strings nicht immer mit einem gültigen Unicode-Skalarwert korrelieren. Um dies zu demonstrieren, betrachten Sie diesen ungültigen Rust-Code:

```rust
let hello = "Здравствуйте";
let answer = &hello[0];
```

Sie wissen bereits, dass `answer` nicht `З`, der erste Buchstabe, sein wird. Wenn in UTF-8 codiert, ist der erste Byte von `З` `208` und das zweite `151`, so dass es so aussehen würde, dass `answer` tatsächlich `208` sein sollte, aber `208` ist kein gültiges Zeichen für sich allein. Das Zurückgeben von `208` ist wahrscheinlich nicht das, was ein Benutzer möchte, wenn er den ersten Buchstaben dieses Strings fragt; jedoch ist das die einzige Daten, die Rust an Byteindex 0 hat. Benutzer möchten im Allgemeinen nicht den Bytewert zurückgegeben bekommen, auch wenn der String nur lateinische Buchstaben enthält: Wenn `&"hello"[0]` gültiger Code wäre, der den Bytewert zurückgibt, würde er `104` zurückgeben, nicht `h`.

Die Antwort ist daher, dass Rust diesen Code überhaupt nicht compiliert, um unerwartete Werte zurückzugeben und Bugs zu vermeiden, die möglicherweise nicht sofort entdeckt werden, und um Missverständnisse im frühen Entwicklungsprozess zu vermeiden.
