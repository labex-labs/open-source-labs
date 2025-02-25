# Trie

## Problem

Ihre Aufgabe ist es, einen Trie mit den folgenden Methoden zu implementieren:

- `find(word)` - gibt `True` zurück, wenn das gegebene Wort im Trie enthalten ist, andernfalls `False`.
- `insert(word)` - fügt das gegebene Wort in den Trie ein.
- `remove(word)` - entfernt das gegebene Wort aus dem Trie.
- `list_words()` - gibt eine Liste aller im Trie enthaltenen Wörter zurück, die mit einem Abschlusszeichen enden.

## Anforderungen

Um diese Herausforderung zu bewältigen, müssen die folgenden Anforderungen erfüllt werden:

- Die Implementierung sollte mit Zeichenketten funktionieren.
- Es wird angenommen, dass die Zeichenketten in ASCII vorliegen.
- Die `find`-Methode sollte nur exakte Wörter mit einem Abschlusszeichen finden.
- Die `list_words`-Methode sollte nur Wörter mit einem Abschlusszeichen zurückgeben.
- Es wird angenommen, dass die Implementierung im Speicher passt.

## Beispielverwendung

Die folgenden Beispiele demonstrieren die Verwendung der Trie-Methoden:

```txt

         root
       /  |  \
      h   a*  m
     / \   \   \
    a   e*  t*  e*
   / \         / \
  s*  t*      n*  t*
             /
            s*

find

* Suchen in einem leeren Trie
* Nicht übereinstimmendes Suchen
* Übereinstimmendes Suchen

insert

* Einfügen in einen leeren Trie
* Einfügen, um ein Blattabschlusszeichen zu erzeugen
* Einfügen, um ein vorhandenes Abschlusszeichen zu erweitern

remove

* Entfernen von mir
* Entfernen von mens
* Entfernen von a
* Entfernen von has

list_words

* Leere Liste auflisten
* Allgemeiner Fall auflisten
```
