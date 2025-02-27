# Bytes, Skalarwerte und Grapheme-Clustern! Oh mein!

Ein weiterer Aspekt von UTF-8 ist, dass es tatsächlich drei relevante Wege gibt, Strings aus der Sicht von Rust zu betrachten: als Bytes, Skalarwerte und Grapheme-Clustern (das Ähnlichste zu dem, was wir _Buchstaben_ nennen würden).

Wenn wir das hindi Wort "नमस्ते" in der Devanagari-Schrift betrachten, wird es als Vektor von `u8`-Werten gespeichert, der so aussieht:

```rust
[224, 164, 168, 224, 164, 174, 224, 164, 184, 224, 165, 141, 224,
164, 164, 224, 165, 135]
```

Das sind 18 Bytes und so speichern Computer letztendlich diese Daten. Wenn wir sie als Unicode-Skalarwerte betrachten, was der `char`-Typ von Rust ist, sehen diese Bytes so aus:

```rust
['न', 'म', 'स', '्', 'त', 'े']
```

Es gibt hier sechs `char`-Werte, aber der vierte und der sechste sind keine Buchstaben: Sie sind Diakritika, die alleine keinen Sinn ergeben. Schließlich, wenn wir sie als Grapheme-Clustern betrachten, erhalten wir das, was eine Person die vier Buchstaben nennen würde, die das hindi Wort bilden:

```rust
["न", "म", "स्", "ते"]
```

Rust bietet verschiedene Möglichkeiten, die ursprünglichen Stringdaten, die Computer speichern, zu interpretieren, sodass jedes Programm die Interpretation wählen kann, die es benötigt, unabhängig davon, welche menschliche Sprache die Daten in sind.

Ein letzter Grund, warum Rust uns nicht erlaubt, in einen `String` einzusteigen, um ein Zeichen zu erhalten, ist, dass Indexoperationen immer in konstanter Zeit (O(1)) erfolgen sollten. Dies ist jedoch nicht möglich, um die Leistung eines `Strings` zu gewährleisten, da Rust die Inhalte von Anfang bis zum Index durchlaufen müsste, um zu bestimmen, wie viele gültige Zeichen vorhanden sind.
