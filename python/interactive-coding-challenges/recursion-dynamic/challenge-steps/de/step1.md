# Python Challenge: Steps

## Problem

Stellen Sie sich vor, dass Sie am Boden einer Treppe mit n Stufen stehen. Sie können jeweils einen, zwei oder drei Stufen hochsteigen. Das Problem besteht darin, herauszufinden, auf wie viele mögliche Weise man die n-te Stufe erreichen kann.

Beispielsweise, wenn es 3 Stufen gibt, können Sie die Treppe auf die folgenden Weise hochsteigen:

- 1-1-1
- 1-2
- 2-1
- 3

Es gibt somit 4 mögliche Wege, um die 3. Stufe zu erreichen.

## Anforderungen

Um dieses Problem zu lösen, müssen wir die folgenden Anforderungen beachten:

- Wenn n == 0, sollte das Ergebnis 1 sein. Es gibt jedoch verschiedene Herangehensweisen an dieses Problem, die diskutiert werden können.
- Wir dürfen nicht annehmen, dass die Eingaben gültig sind.
- Wir können annehmen, dass das Problem in den Speicher passt.

## Beispielverwendung

Hier sind einige Beispiele dafür, wie dieses Problem mit Python gelöst werden kann:

- Keine oder negative Eingabe -> Exception
- n == 0 -> 1
- n == 1 -> 1
- n == 2 -> 2
- n == 3 -> 4
- n == 4 -> 7
- n == 10 -> 274
