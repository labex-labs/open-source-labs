# Ermöglichen von rekursiven Typen mit Boxen

Ein Wert eines _rekursiven Typs_ kann einen anderen Wert desselben Typs als Teil seiner selbst enthalten. Rekursive Typen stellen ein Problem dar, da Rust zur Compile-Zeit wissen muss, wie viel Speicher ein Typ einnimmt. Da die Verschachtelung von Werten rekursiver Typen theoretisch endlos fortfahren könnte, kann Rust nicht wissen, wie viel Speicher der Wert benötigt. Da Boxen eine bekannte Größe haben, können wir rekursive Typen aktivieren, indem wir eine Box in die rekursive Typdefinition einfügen.

Als Beispiel für einen rekursiven Typ wollen wir die _Cons-Liste_ untersuchen. Dies ist ein Datentyp, der in funktionalen Programmiersprachen häufig vorkommt. Der von uns zu definierende Cons-Liste-Typ ist bis auf die Rekursion einfach; daher werden die Konzepte im Beispiel, mit dem wir arbeiten, jederzeit nützlich sein, wenn Sie in komplexere Situationen mit rekursiven Typen geraten.
