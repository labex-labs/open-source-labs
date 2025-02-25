# Menge von Stapeln

## Problem

Implementiere eine SetOfStacks-Klasse, die eine Liste von Stapeln umschließt, wobei jeder Stapel durch eine Kapazität begrenzt ist. Die Klasse sollte die folgenden Funktionalitäten haben:

- Füge ein Element auf den obersten Stapel der letzten Stapel in der Liste hinzu. Wenn der letzte Stapel voll ist, erstelle einen neuen Stapel und füge das Element dem neuen Stapel hinzu.
- Entferne das oberste Element vom letzten Stapel in der Liste. Wenn der letzte Stapel leer ist, entferne es aus der Liste und entferne das oberste Element vom neuen letzten Stapel in der Liste. Wenn die Liste leer ist, gib None zurück.
- Entferne ein Element von einem bestimmten Stapel in der Liste. Wenn der Stapel leer ist, entferne es aus der Liste. Wenn die Liste leer ist, gib None zurück.

## Anforderungen

Die SetOfStacks-Klasse sollte die folgenden Anforderungen erfüllen:

- Die Klasse sollte eine vorhandene Stapelklasse verwenden.
- Alle Stapel in der Liste sollten durch die gleiche Kapazität begrenzt sein.
- Wenn ein Stapel voll wird, sollte automatisch ein neuer Stapel erstellt werden, um zusätzliche Elemente zu speichern.
- Wenn ein Stapel leer wird, sollte er aus der Liste entfernt werden.
- Wenn wir auf einem leeren Stapel pop ausführen, sollte die Methode None zurückgeben.
- Die Implementierung sollte im Speicher passen.

## Beispielverwendung

Die SetOfStacks-Klasse kann in folgenden Szenarien verwendet werden:

- Push und pop auf einem leeren Stapel.
- Push und pop auf einem nicht-leeren Stapel.
- Push auf einen Stapel mit Kapazität, um einen neuen zu erstellen.
- Pop auf einem Stapel, um ihn zu zerstören.
