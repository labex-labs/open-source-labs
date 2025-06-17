# Ganzzahltypen (Integer Types)

Eine _Ganzzahl_ (integer) ist eine Zahl ohne einen Bruchteil. Wir haben einen Ganzzahltyp in Kapitel 2 verwendet, den Typ `u32`. Diese Typdeklaration gibt an, dass der Wert, dem sie zugeordnet ist, eine vorzeichenlose Ganzzahl (signed integer types) sein soll (vorzeichenbehaftete Ganzzahltypen beginnen mit `i` anstelle von `u`), die 32 Bit Speicherplatz beansprucht. Tabelle 3-1 zeigt die integrierten Ganzzahltypen in Rust. Wir können jede dieser Varianten verwenden, um den Typ eines Ganzzahlwerts zu deklarieren.

Tabelle 3-1: Ganzzahltypen in Rust

Länge Vorzeichenbehaftet (Signed) Vorzeichenlos (Unsigned)

---

8-Bit `i8` `u8`
16-Bit `i16` `u16`
32-Bit `i32` `u32`
64-Bit `i64` `u64`
128-Bit `i128` `u128`
arch `isize` `usize`

Jede Variante kann entweder vorzeichenbehaftet (signed) oder vorzeichenlos (unsigned) sein und hat eine explizite Größe. _Vorzeichenbehaftet_ (signed) und _vorzeichenlos_ (unsigned) beziehen sich darauf, ob die Zahl negativ sein kann – mit anderen Worten, ob die Zahl ein Vorzeichen haben muss (vorzeichenbehaftet) oder ob sie nur positiv sein wird und daher ohne Vorzeichen dargestellt werden kann (vorzeichenlos). Es ist wie das Schreiben von Zahlen auf Papier: Wenn das Vorzeichen wichtig ist, wird eine Zahl mit einem Plus- oder Minuszeichen angezeigt; wenn jedoch davon ausgegangen werden kann, dass die Zahl positiv ist, wird sie ohne Vorzeichen angezeigt. Vorzeichenbehaftete Zahlen werden mit der Zweierkomplementdarstellung (two's complement representation) gespeichert.

Jede vorzeichenbehaftete Variante kann Zahlen von -(2^(n-1)) bis 2^(n-1) - 1 einschließlich speichern, wobei _n_ die Anzahl der Bits ist, die diese Variante verwendet. Ein `i8` kann also Zahlen von -(2^7) bis 2^7 - 1 speichern, was -128 bis 127 entspricht. Vorzeichenlose Varianten können Zahlen von 0 bis 2^n - 1 speichern, also kann ein `u8` Zahlen von 0 bis 2^8 - 1 speichern, was 0 bis 255 entspricht.

Zusätzlich hängen die Typen `isize` und `usize` von der Architektur des Computers ab, auf dem Ihr Programm ausgeführt wird, was in der Tabelle als "arch" bezeichnet wird: 64 Bit, wenn Sie sich auf einer 64-Bit-Architektur befinden, und 32 Bit, wenn Sie sich auf einer 32-Bit-Architektur befinden.

Sie können Ganzzahlliterale in jeder der in Tabelle 3-2 gezeigten Formen schreiben. Beachten Sie, dass Zahlenliterale, die mehrere numerische Typen sein können, ein Typsuffix wie `57u8` zulassen, um den Typ zu bezeichnen. Zahlenliterale können auch `_` als visuelles Trennzeichen verwenden, um die Zahl leichter lesbar zu machen, z. B. `1_000`, was denselben Wert hat, als ob Sie `1000` angegeben hätten.

Tabelle 3-2: Ganzzahlliterale in Rust

Zahlenliterale Beispiel

---

Dezimal `98_222`
Hexadezimal `0xff`
Oktal `0o77`
Binär `0b1111_0000`
Byte (nur `u8`) `b'A'`

Wie wissen Sie also, welchen Ganzzahltyp Sie verwenden sollen? Wenn Sie sich unsicher sind, sind die Standardeinstellungen von Rust im Allgemeinen ein guter Ausgangspunkt: Ganzzahltypen werden standardmäßig auf `i32` gesetzt. Die primäre Situation, in der Sie `isize` oder `usize` verwenden würden, ist beim Indizieren einer Art von Sammlung.

> **Ganzzahlüberlauf (Integer Overflow)**
>
> Angenommen, Sie haben eine Variable vom Typ `u8`, die Werte zwischen 0 und 255 aufnehmen kann. Wenn Sie versuchen, die Variable auf einen Wert außerhalb dieses Bereichs zu ändern, z. B. 256, tritt ein _Ganzzahlüberlauf_ (integer overflow) auf, der zu einem von zwei Verhaltensweisen führen kann. Wenn Sie im Debug-Modus kompilieren, enthält Rust Überlaufprüfungen für Ganzzahlen, die dazu führen, dass Ihr Programm zur Laufzeit _panickt_ (panic), wenn dieses Verhalten auftritt. Rust verwendet den Begriff _panicking_ (panicking), wenn ein Programm mit einem Fehler beendet wird; wir werden Panics in "Unrecoverable Errors with panic!" ausführlicher besprechen.
>
> Wenn Sie im Release-Modus mit dem Flag `--release` kompilieren, enthält Rust _keine_ Überlaufprüfungen für Ganzzahlen, die Panics verursachen. Stattdessen führt Rust, wenn ein Überlauf auftritt, eine _Zweierkomplement-Umwicklung_ (two's complement wrapping) durch. Kurz gesagt, Werte, die größer sind als der Maximalwert, den der Typ aufnehmen kann, "wickeln sich" auf das Minimum der Werte, die der Typ aufnehmen kann. Im Fall eines `u8` wird der Wert 256 zu 0, der Wert 257 zu 1 usw. Das Programm wird nicht panicken, aber die Variable hat einen Wert, der wahrscheinlich nicht dem entspricht, was Sie erwartet haben. Sich auf das Wrapping-Verhalten des Ganzzahlüberlaufs zu verlassen, gilt als Fehler.
>
> Um die Möglichkeit eines Überlaufs explizit zu behandeln, können Sie diese Familien von Methoden verwenden, die von der Standardbibliothek für primitive numerische Typen bereitgestellt werden:
>
> - Umwickeln in allen Modi mit den `wrapping_*`-Methoden, wie z. B. `wrapping_add`.
> - Den Wert `None` zurückgeben, wenn ein Überlauf mit den `checked_*`-Methoden auftritt.
> - Den Wert und einen booleschen Wert zurückgeben, der angibt, ob ein Überlauf mit den `overflowing_*`-Methoden aufgetreten ist.
> - Mit den `saturating_*`-Methoden auf die Minimal- oder Maximalwerte des Werts sättigen.
