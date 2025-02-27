# Definieren einer Enumeration

Während Structs dir eine Möglichkeit geben, zusammengehörige Felder und Daten zu gruppieren, wie ein `Rectangle` mit seiner `width` und `height`, geben Enums dir eine Möglichkeit, auszudrücken, dass ein Wert einer möglichen Menge von Werten angehört. Beispielsweise möchten wir sagen, dass `Rectangle` eine der möglichen Formen ist, die auch `Circle` und `Triangle` umfasst. Um dies zu tun, erlaubt Rust uns, diese Möglichkeiten als Enum zu kodieren.

Schauen wir uns eine Situation an, die wir in Code ausdrücken möchten, und sehen, warum Enums in diesem Fall nützlich und passender als Structs sind. Nehmen wir an, dass wir mit IP-Adressen arbeiten müssen. Derzeit werden zwei Hauptstandards für IP-Adressen verwendet: Version vier und Version sechs. Da diese die einzigen Möglichkeiten für eine IP-Adresse sind, die unser Programm begegnen wird, können wir alle möglichen Varianten _enumerieren_, was der Enumeration ihren Namen gibt.

Jede IP-Adresse kann entweder eine Version-vier- oder eine Version-sechs-Adresse sein, aber nicht gleichzeitig beides. Diese Eigenschaft von IP-Adressen macht die Enum-Datenstruktur geeignet, da ein Enum-Wert nur eine seiner Varianten sein kann. Sowohl Version-vier- als auch Version-sechs-Adressen sind immer noch im Grunde IP-Adressen, sodass sie als derselbe Typ behandelt werden sollten, wenn der Code Situationen behandelt, die für jede Art von IP-Adresse gelten.

Wir können diesen Begriff im Code ausdrücken, indem wir eine `IpAddrKind`-Enumeration definieren und die möglichen Arten auflisten, die eine IP-Adresse haben kann, `V4` und `V6`. Dies sind die Varianten der Enum:

```rust
enum IpAddrKind {
    V4,
    V6,
}
```

`IpAddrKind` ist jetzt ein benutzerdefinierter Datentyp, den wir in anderen Teilen unseres Codes verwenden können.
