# Allgemeine Broadcast-Regeln

NumPy vergleicht die Formen zweier Arrays elementweise, um zu bestimmen, ob sie für das Broadcasting kompatibel sind. Die folgenden Regeln gelten:

1. Zwei Dimensionen sind kompatibel, wenn sie in der Größe gleich sind.
2. Zwei Dimensionen sind kompatibel, wenn eine von ihnen eine Größe von 1 hat.

Wenn diese Bedingungen nicht erfüllt sind, wird ein `ValueError` ausgelöst, was darauf hinweist, dass die Arrays inkongruente Formen haben.
