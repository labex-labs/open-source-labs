# Einzigartige Zeichen

## Problemstellung

Gegeben einen String, ist die Aufgabe, zu bestimmen, ob er ausschließlich einzigartige Zeichen enthält. Mit anderen Worten, es sollten keine wiederholten Zeichen im String vorhanden sein. Beispielsweise hat der String "hello" nicht ausschließlich einzigartige Zeichen, da der Buchstabe "l" zweimal vorkommt. Andererseits hat der String "world" ausschließlich einzigartige Zeichen, da jeder Buchstabe nur einmal vorkommt.

## Anforderungen

Um dieses Problem zu lösen, müssen die folgenden Anforderungen erfüllt sein:

- Der String wird als ASCII angenommen.
  - Unicode-Strings können je nach verwendeter Sprache besondere Behandlung erfordern.
- Die Groß-/Kleinschreibung wird als sensibel angenommen.
- Zusätzliche Datenstrukturen können verwendet werden.
- Es wird angenommen, dass der String in den Arbeitsspeicher passt.

## Beispielverwendung

Die folgenden Beispiele zeigen, wie die Funktion verhalten sollte:

- None -> False
- '' -> True
- 'foo' -> False
- 'bar' -> True
