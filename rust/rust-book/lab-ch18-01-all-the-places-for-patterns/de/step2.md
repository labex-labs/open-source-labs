# match-Arme

Wie in Kapitel 6 besprochen, verwenden wir Muster in den Armen von `match`-Ausdrücken. Formal sind `match`-Ausdrücke definiert als das Schlüsselwort `match`, einen Wert, auf den gematcht werden soll, und einen oder mehrere match-Arme, die aus einem Muster und einem Ausdruck bestehen, der ausgeführt werden soll, wenn der Wert dem Muster des Arms entspricht, wie folgt:

    match WERT {
        MUSTER => AUSDRUCK,
        MUSTER => AUSDRUCK,
        MUSTER => AUSDRUCK,
    }

Beispielsweise ist hier der `match`-Ausdruck aus Listing 6-5, der auf einen `Option<i32>`-Wert in der Variable `x` gematcht wird:

    match x {
        None => None,
        Some(i) => Some(i + 1),
    }

Die Muster in diesem `match`-Ausdruck sind die `None` und `Some(i)` links von jedem Pfeil.

Eine Anforderung für `match`-Ausdrücke ist, dass sie _ausführlich_ sein müssen, in dem Sinne, dass alle Möglichkeiten für den Wert im `match`-Ausdruck berücksichtigt werden müssen. Ein Weg, um sicherzustellen, dass Sie jede Möglichkeit abgedeckt haben, ist, einen Fallback-Muster für den letzten Arm zu haben: Beispielsweise kann ein Variablennamen, der jedem Wert entspricht, niemals fehlschlagen und deckt somit jeden verbleibenden Fall ab.

Das besondere Muster `_` wird mit allem übereinstimmen, bindet jedoch niemals an eine Variable, weshalb es oft im letzten match-Arm verwendet wird. Das `_`-Muster kann nützlich sein, wenn Sie beispielsweise alle Werte ignorieren möchten, die nicht angegeben sind. Wir werden das `_`-Muster im Abschnitt "Ignorieren von Werten in einem Muster" im Detail behandeln.
