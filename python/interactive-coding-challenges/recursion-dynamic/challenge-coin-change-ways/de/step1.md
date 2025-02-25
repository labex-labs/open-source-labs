# Münzwechselmöglichkeiten

## Problem

Gegeben eine ganze Zahl n und ein Array von unterschiedlichen Münzen, schreiben Sie eine Funktion, um die Anzahl der Möglichkeiten zu zählen, um für n Wechselgeld zu geben, indem die Münzen im Array verwendet werden. Eine Münze kann beliebig oft verwendet werden, und wir zählen einzigartige Kombinationen.

Beispielsweise, wenn n = 4 und coins = [1, 2], gibt es 3 Möglichkeiten, Wechselgeld zu geben: 1+1+1+1, 1+2+1 und 2+2.

## Anforderungen

Um dieses Problem zu lösen, müssen Sie:

- Eine Funktion schreiben, die zwei Argumente annimmt: eine ganze Zahl n und ein Array von unterschiedlichen Münzen.
- Dynamisches Programmieren verwenden, um die Anzahl der Möglichkeiten zu zählen, um für n Wechselgeld zu geben, indem die Münzen im Array verwendet werden.
- Die Anzahl der einzigartigen Kombinationen zurückgeben.

## Beispiel

Eingabe: n = 4, Münzen = [1, 2]

Ausgabe: 3. 1+1+1+1, 1+2+1, 2+2, wären die Möglichkeiten, Wechselgeld zu geben.
