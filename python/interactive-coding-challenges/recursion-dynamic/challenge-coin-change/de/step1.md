# Münzwechsel

## Problem

Gegeben eine Menge von Münzen unterschiedlicher Denominationen und ein Gesamtbetrag von n Geldbeträgen, bestimmen Sie die Gesamtzahl der einzigartigen Möglichkeiten, um n Cent zu wechseln. Die bereitgestellten Münzen haben Denominationen von weniger als n Cent.

## Anforderungen

Um dieses Problem zu lösen, müssen die folgenden Anforderungen erfüllt sein:

- Die Münzen müssen genau n Cent erreichen.
- Es kann angenommen werden, dass es unendlich viele Münzen gibt, um n Cent zu bilden.
- Die Kombination(en) von Münzen, die das Minimum darstellen, müssen nicht gemeldet werden.
- Die Münzdenominationen werden nicht in aufsteigender Reihenfolge angegeben.
- Die Lösung muss in den Arbeitsspeicher passen.

## Beispielverwendung

Die folgenden Beispiele veranschaulichen die Verwendung des Münzwechselproblems:

- Münzen: None oder n: None -> Ausnahme
- Münzen: [] oder n: 0 -> 0
- Münzen: [1, 2, 3], n: 5 -> 5
