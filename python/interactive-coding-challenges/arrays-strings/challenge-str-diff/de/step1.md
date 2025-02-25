# Str Diff

## Problem

Gegeben zwei Zeichenketten müssen wir das einzige unterschiedliche Zeichen zwischen ihnen finden. Die Zeichenketten werden als ASCII und in Kleinbuchstaben angenommen. Wir können nicht davon ausgehen, dass die Eingaben gültig sind, daher müssen wir auf None prüfen. Wenn die Eingaben gültig sind, können wir davon ausgehen, dass es zwischen den beiden Zeichenketten nur ein einziges unterschiedliches Zeichen gibt. Wir müssen auch sicherstellen, dass die Lösung im Speicher passt.

## Anforderungen

Um dieses Problem zu lösen, müssen wir die folgenden Anforderungen berücksichtigen:

- Die Zeichenketten sind ASCII.
- Die Zeichenketten sind in Kleinbuchstaben.
- Wir müssen auf None-Eingaben prüfen.
- Es gibt zwischen den beiden Zeichenketten nur ein einziges unterschiedliches Zeichen.
- Die Lösung sollte im Speicher passen.

## Beispielverwendung

Hier sind einige Beispiele, wie die Funktion verwendet werden kann:

- None-Eingabe -> TypeError
- 'ab', 'aab' -> 'a'
- 'aab', 'ab' -> 'a'
- 'abcd', 'abcde' -> 'e'
- 'aaabbcdd', 'abdbacade' -> 'e'
