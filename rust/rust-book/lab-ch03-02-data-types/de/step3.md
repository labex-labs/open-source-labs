# Ganzzahlige Datentypen

Eine _Ganzzahl_ ist eine Zahl ohne Bruchanteil. Wir haben in Kapitel 2 einen ganzzahligen Datentyp verwendet, nämlich den `u32`-Typ. Diese Typdeklaration gibt an, dass der ihr zugeordnete Wert ein vorzeichenloses Ganzzahl (vorzeichenbehaftete Ganzzahltypen beginnen mit `i` anstelle von `u`) sein soll, der 32 Bits Speicherplatz einnimmt. Tabelle 3-1 zeigt die in Rust integrierten ganzzahligen Datentypen. Wir können jede dieser Varianten verwenden, um den Typ eines ganzzahligen Werts zu deklarieren.

Tabelle 3-1: Ganzzahlige Datentypen in Rust

Länge Vorzeichenbehaftet Vorzeichenlos

---

8 Bit `i8` `u8`
16 Bit `i16` `u16`
32 Bit `i32` `u32`
64 Bit `i64` `u64`
128 Bit `i128` `u128`
Architektur `isize` `usize`

Jede Variante kann entweder vorzeichenbehaftet oder vorzeichenlos sein und hat eine explizite Größe. _Vorzeichenbehaftet_ und _vorzeichenlos_ beziehen sich darauf, ob es möglich ist, dass die Zahl negativ ist – mit anderen Worten, ob die Zahl ein Vorzeichen haben muss (vorzeichenbehaftet) oder ob sie nur positiv sein kann und daher ohne Vorzeichen dargestellt werden kann (vorzeichenlos). Es ist wie das Schreiben von Zahlen auf Papier: Wenn das Vorzeichen wichtig ist, wird eine Zahl mit einem Plus- oder Minuszeichen dargestellt; wenn es jedoch sicher ist, anzunehmen, dass die Zahl positiv ist, wird sie ohne Vorzeichen dargestellt. Vorzeichenbehaftete Zahlen werden mit der Zweierkomplement-Darstellung gespeichert.

Jede vorzeichenbehaftete Variante kann Zahlen von -(2`<sup>`{=html}n - 1`</sup>`{=html}) bis 2`<sup>`{=html}n - 1`</sup>`{=html} einschließlich speichern, wobei _n_ die Anzahl der Bits ist, die diese Variante verwendet. Ein `i8` kann daher Zahlen von -(2`<sup>`{=html}7`</sup>`{=html}) bis 2`<sup>`{=html}7`</sup>`{=html} - 1 speichern, was -128 bis 127 entspricht. Vorzeichenlose Varianten können Zahlen von 0 bis 2`<sup>`{=html}n`</sup>`{=html} - 1 speichern, so kann ein `u8` Zahlen von 0 bis 2`<sup>`{=html}8`</sup>`{=html} - 1 speichern, was 0 bis 255 entspricht.

Zusätzlich hängen die Typen `isize` und `usize` von der Architektur des Computers ab, auf dem Ihr Programm ausgeführt wird, was in der Tabelle als "Architektur" bezeichnet wird: 64 Bits, wenn Sie auf einer 64-Bit-Architektur sind, und 32 Bits, wenn Sie auf einer 32-Bit-Architektur sind.

Sie können ganzzahlige Literale in jeder der in Tabelle 3-2 gezeigten Formen schreiben. Beachten Sie, dass Zahlennliterale, die mehrere numerische Typen zulassen, einen Typzusatz wie `57u8` zulassen, um den Typ anzugeben. Zahlennliterale können auch `_` als visuelle Trennung verwenden, um die Zahl leichter lesbar zu machen, wie `1_000`, das denselben Wert wie `1000` haben wird.

Tabelle 3-2: Ganzzahlige Literale in Rust

Zahlennliterale Beispiel

---

Dezimal `98_222`
Hexadezimal `0xff`
Oktal `0o77`
Binär `0b1111_0000`
Byte (`nur u8`) `b'A'`

Wie wissen Sie also, welchen ganzzahligen Typ Sie verwenden sollen? Wenn Sie unsicher sind, sind die Standardwerte von Rust im Allgemeinen gute Ausgangspunkte: Ganzzahltypen haben standardmäßig den Typ `i32`. Die Hauptsituation, in der Sie `isize` oder `usize` verwenden würden, besteht darin, wenn Sie eine Art von Sammlung indizieren.

> **Ganzzahlüberlauf**
>
> Stellen Sie sich vor, dass Sie eine Variable vom Typ `u8` haben, die Werte zwischen 0 und 255 speichern kann. Wenn Sie versuchen, die Variable auf einen Wert außerhalb dieses Bereichs, wie 256, zu ändern, tritt ein _Ganzzahlüberlauf_ auf, was zu einem von zwei Verhaltensweisen führen kann. Wenn Sie im Debugmodus kompilieren, enthält Rust Überlaufprüfungen für Ganzzahlen, die dazu führen, dass Ihr Programm zur Laufzeit _abstürzt_, wenn dieser Fehler auftritt. Rust verwendet den Begriff _abstürzen_, wenn ein Programm mit einem Fehler beendet wird; wir werden Abstürze im weiteren Verlauf in "Unwiderholbare Fehler mit panic!" genauer besprechen.
>
> Wenn Sie im Releasemodus mit der Option `--release` kompilieren, enthält Rust keine Überlaufprüfungen für Ganzzahlen, die zu Abstürzen führen. Stattdessen führt Rust bei einem Überlauf eine _Zweierkomplementumkehrung_ durch. Kurz gesagt werden Werte, die größer als der maximale Wert sind, den der Typ aufnehmen kann, auf den minimalen Wert, den der Typ aufnehmen kann, "zurückgewickelt". Im Falle eines `u8` wird der Wert 256 zu 0, der Wert 257 zu 1 usw. Das Programm wird nicht abstürzen, aber die Variable wird einen Wert haben, der wahrscheinlich nicht dem entspricht, was Sie erwartet haben. Das Verlassen auf das Umkehrverhalten des Ganzzahlüberlaufs wird als Fehler angesehen.
>
> Um die Möglichkeit eines Überlaufs explizit zu behandeln, können Sie die folgenden Methodenfamilien der Standardbibliothek für primitive numerische Typen verwenden:
>
> - Wenden Sie die `wrapping_*`-Methoden wie `wrapping_add` in allen Modi an.
> - Geben Sie den Wert `None` zurück, wenn es bei der Verwendung der `checked_*`-Methoden zu einem Überlauf kommt.
> - Geben Sie den Wert und einen booleschen Wert zurück, der angibt, ob es zu einem Überlauf kam, bei Verwendung der `overflowing_*`-Methoden.
> - Sättigen Sie den Wert an seinem minimalen oder maximalen Wert mit den `saturating_*`-Methoden.
