# Verwendung von Mutexen, um Zugang zu Daten zu ermöglichen, nur von einem Thread zur selben Zeit

_Mutex_ ist die Abkürzung für _mutual exclusion_ (gegenseitige Ausschließung), da ein Mutex nur einem Thread erlaubt, zu einem bestimmten Zeitpunkt auf einige Daten zuzugreifen. Um auf die Daten in einem Mutex zuzugreifen, muss ein Thread zunächst signalisieren, dass er den Zugang wünscht, indem er den Lock (Sperre) des Mutexes anfordert. Der Lock ist eine Datenstruktur, die Teil des Mutexes ist und verfolgt, wer derzeit ausschließlich auf die Daten zugreifen kann. Daher wird der Mutex als _bewachend_ die Daten beschrieben, die er über das Sperrsystem hält.

Mutexe haben einen Ruf, schwierig zu verwenden, weil man zwei Regeln beachten muss:

1.  Man muss versuchen, den Lock zu erwerben, bevor man die Daten verwendet.
2.  Wenn man mit den Daten fertig ist, die der Mutex bewacht, muss man die Daten entsperren, damit andere Threads den Lock erwerben können.

Als realitätsnahes Beispiel für einen Mutex kann man sich eine Podiumsrunde auf einer Konferenz vorstellen, bei der es nur ein Mikrofon gibt. Bevor ein Podiumsredner sprechen kann, muss er fragen oder signalisieren, dass er das Mikrofon verwenden möchte. Wenn er das Mikrofon erhält, kann er so lange sprechen, wie er möchte, und gibt dann das Mikrofon an den nächsten Podiumsredner weiter, der sprechen möchte. Wenn ein Podiumsredner vergisst, das Mikrofon abzugeben, wenn er damit fertig ist, kann niemand else sprechen. Wenn die Verwaltung des geteilten Mikrofons fehlschlägt, funktioniert die Podiumsrunde nicht wie geplant!

Die Verwaltung von Mutexen kann extrem schwierig sein, um richtig zu erledigen, weshalb so viele Leute von Kanälen begeistert sind. Dank des Rust-Typsystems und der Eigentumsregeln kann man jedoch nicht falsch sperren und entsperren.
