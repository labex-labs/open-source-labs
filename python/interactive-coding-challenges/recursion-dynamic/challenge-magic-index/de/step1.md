# Magischer Index

## Problem

Gegeben ein sortiertes Array von ganzen Zahlen mit möglicherweise doppelten Werten, schreiben Sie eine Python-Funktion, um den magischen Index, sofern vorhanden, im Array zu finden. Wenn es mehrere magische Werte gibt, geben Sie den linkensten zurück. Wenn es keinen magischen Index gibt, geben Sie -1 zurück.

## Anforderungen

Um das Problem zu lösen, müssen die folgenden Anforderungen erfüllt sein:

- Das Array ist sortiert.
- Die Elemente im Array dürfen nicht unterschiedlich sein.
- Negative Werte sind im Array erlaubt.
- Wenn es keinen magischen Index gibt, geben Sie -1 zurück.

## Beispielverwendung

Die folgenden Beispiele veranschaulichen die Verwendung der Funktion:

- Keine Eingabe -> -1
- Leeres Array -> -1

```txt
a[i]  -4 -2  2  6  6  6  6 10
  i    0  1  2  3  4  5  6  7
```

Ergebnis: 2

```txt
a[i]  -4 -2  1  6  6  6  6 10
  i    0  1  2  3  4  5  6  7
```

Ergebnis: 6

```txt
a[i]  -4 -2  1  6  6  6  7 10
  i    0  1  2  3  4  5  6  7
```

Ergebnis: -1
