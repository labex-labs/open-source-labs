# Variablenbereich

Jetzt, nachdem wir die grundlegende Rust-Syntax hinter uns haben, werden wir in den Beispielen nicht mehr den gesamten `fn main() {`-Code angeben. Wenn du mitmachst, musst du daher die folgenden Beispiele manuell in eine `main`-Funktion einfügen. Dadurch werden unsere Beispiele etwas kürzer und wir können uns auf die tatsächlichen Details konzentrieren, anstatt auf Boilerplate-Code.

Als erstes Beispiel für Besitz betrachten wir den _Bereich_ von Variablen. Ein Bereich ist der Bereich innerhalb eines Programms, für den ein Element gültig ist. Nehmen wir die folgende Variable:

```rust
let s = "hello";
```

Die Variable `s` bezieht sich auf einen String-Literal, wobei der Wert des Strings in den Text unseres Programms hartenkodiert ist. Die Variable ist von dem Zeitpunkt an gültig, zu dem sie deklariert wird, bis zum Ende des aktuellen _Bereichs_. Listing 4-1 zeigt ein Programm mit Kommentaren, die angeben, wo die Variable `s` gültig wäre.

    {                      // s ist hier nicht gültig, da sie noch nicht deklariert ist
        let s = "hello";   // s ist ab diesem Zeitpunkt gültig

        // mache etwas mit s
    }                      // dieser Bereich ist jetzt vorbei, und s ist nicht mehr gültig

Listing 4-1: Eine Variable und der Bereich, in dem sie gültig ist

Mit anderen Worten, es gibt zwei wichtige Zeitpunkte hier:

- Wenn `s` in den _Bereich_ kommt, ist sie gültig.
- Sie bleibt gültig, bis sie außerhalb des _Bereichs_ fällt.

An diesem Punkt ist die Beziehung zwischen Bereichen und der Gültigkeit von Variablen ähnlich wie in anderen Programmiersprachen. Jetzt bauen wir auf diesem Verständnis auf, indem wir den `String`-Typ einführen.
