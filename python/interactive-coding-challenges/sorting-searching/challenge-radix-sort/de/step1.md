#基数排序

## Problem

Implementieren Sie den基数排序-Algorithmus, um eine Liste von ganzen Zahlen zu sortieren. Der Algorithmus sortiert die ganzen Zahlen, indem er ihre Ziffern von der am wenigsten signifikanten Ziffer bis zur am meisten signifikanten Ziffer vergleicht. Der Algorithmus sortiert zunächst die ganzen Zahlen basierend auf der am wenigsten signifikanten Ziffer, dann auf der zweitam wenigsten signifikanten Ziffer usw., bis die am meisten signifikanten Ziffer sortiert ist.

## Anforderungen

Um den基数排序-Implementieren Sie die folgenden Anforderungen müssen erfüllt sein:

- Die Eingabe muss eine Liste von ganzen Zahlen sein.
- Prüfen Sie auf None anstelle eines Arrays.
- Nehmen Sie an, dass die Arrayelemente ganze Zahlen sind.
- Die Ziffern müssen im Zehnersystem sein.
- Der Algorithmus muss mit beliebig vielen Ziffern umgehen können.
- Der Algorithmus muss in den Arbeitsspeicher passen.

## Beispielverwendung

Die folgenden sind Beispiele dafür, wie der基数排序-Algorithmus verwendet werden kann:

- None -> Exception
- [] -> []
- [128, 256, 164, 8, 2, 148, 212, 242, 244] -> [2, 8, 128, 148, 164, 212, 242, 244, 256]
