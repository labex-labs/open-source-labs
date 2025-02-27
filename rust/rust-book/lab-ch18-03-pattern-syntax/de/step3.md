# Benannte Variablen abgleichen

Benannte Variablen sind unwiderlegbare Muster, die jedem Wert entsprechen, und wir haben sie in diesem Buch bereits vielfach verwendet. Es gibt jedoch eine Komplikation, wenn du benannte Variablen in `match`-Ausdrücken verwendest. Da `match` einen neuen Gültigkeitsbereich startet, werden Variablen, die als Teil eines Musters innerhalb des `match`-Ausdrucks deklariert werden, die Variablen mit demselben Namen außerhalb des `match`-Konstrukts verdrängen, wie dies bei allen Variablen der Fall ist. In Listing 18-11 deklarieren wir eine Variable namens `x` mit dem Wert `Some(5)` und eine Variable `y` mit dem Wert `10`. Anschließend erstellen wir einen `match`-Ausdruck für den Wert `x`. Schau dir die Muster in den `match`-Armen und die `println!` am Ende an und versuche, herauszufinden, was der Code ausgeben wird, bevor du diesen Code ausführst oder weiter liest.

Dateiname: `src/main.rs`

```rust
fn main() {
  1 let x = Some(5);
  2 let y = 10;

    match x {
      3 Some(50) => println!("Krieg 50"),
      4 Some(y) => println!("Übereinstimmung, y = {y}"),
      5 _ => println!("Standardfall, x = {:?}", x),
    }

  6 println!("am Ende: x = {:?}, y = {y}", x);
}
```

Listing 18-11: Ein `match`-Ausdruck mit einem Arm, der eine verdrängte Variable `y` einführt

Schauen wir uns an, was passiert, wenn der `match`-Ausdruck ausgeführt wird. Das Muster im ersten `match`-Arm \[3\] stimmt nicht mit dem definierten Wert von `x` \[1\] überein, also wird der Code fortgesetzt.

Das Muster im zweiten `match`-Arm \[4\] führt eine neue Variable namens `y` ein, die jedem Wert innerhalb eines `Some`-Werts entsprechen wird. Da wir uns in einem neuen Gültigkeitsbereich innerhalb des `match`-Ausdrucks befinden, handelt es sich um eine neue `y`-Variable, nicht um die `y`, die wir am Anfang mit dem Wert `10` deklariert haben \[2\]. Diese neue `y`-Bindung wird jedem Wert innerhalb eines `Some` entsprechen, was wir in `x` haben. Daher bindet diese neue `y` an den inneren Wert des `Some` in `x`. Dieser Wert ist `5`, sodass der Ausdruck für diesen Arm ausgeführt wird und `Übereinstimmung, y = 5` ausgibt.

Wenn `x` ein `None`-Wert anstelle von `Some(5)` gewesen wäre, wären die Muster in den ersten beiden Armen nicht übereinstimmend, sodass der Wert dem Unterstrich \[5\] entsprechen würde. Wir haben die `x`-Variable im Muster des Unterstrich-Arms nicht eingeführt, sodass die `x` im Ausdruck immer noch die äußere `x` ist, die nicht verdrängt wurde. In diesem hypothetischen Fall würde der `match` `Standardfall, x = None` ausgeben.

Wenn der `match`-Ausdruck abgeschlossen ist, endet auch sein Gültigkeitsbereich, und damit auch der Gültigkeitsbereich der inneren `y`. Die letzte `println!` \[6\] liefert `am Ende: x = Some(5), y = 10`.

Um einen `match`-Ausdruck zu erstellen, der die Werte der äußeren `x` und `y` vergleicht, anstatt eine verdrängte Variable zu introduzieren, müssten wir stattdessen einen `match`-Guard-Zusatzbedingung verwenden. Wir werden in "Zusätzliche Bedingungen mit `match`-Guards" über `match`-Guards sprechen.
