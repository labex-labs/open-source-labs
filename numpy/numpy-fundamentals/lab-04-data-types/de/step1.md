# Das Verständnis von Datentypen

NumPy unterstützt eine Vielzahl von numerischen Typen, die eng mit denen in der C-Programmiersprache verbunden sind. Hier sind einige der am häufigsten verwendeten Datentypen in NumPy:

- `numpy.bool_`: Boolescher Wert (True oder False), gespeichert als Byte
- `numpy.byte`: Geteiltes Vorzeichen (plattformabhängig definiert)
- `numpy.ubyte`: Vorzeichenlose Ganzzahl (plattformabhängig definiert)
- `numpy.short`: Kurz (plattformabhängig definiert)
- `numpy.ushort`: Vorzeichenlose Kurzzahl (plattformabhängig definiert)
- `numpy.intc`: Ganzzahl (plattformabhängig definiert)
- `numpy.uintc`: Vorzeichenlose Ganzzahl (plattformabhängig definiert)
- `numpy.int_`: Lang (plattformabhängig definiert)
- `numpy.uint`: Vorzeichenlose lange Ganzzahl (plattformabhängig definiert)
- `numpy.longlong`: Lang lang (plattformabhängig definiert)
- `numpy.ulonglong`: Vorzeichenlose lange lange Ganzzahl (plattformabhängig definiert)
- `numpy.half` / `numpy.float16`: Halbgenauigkeit Gleitkommazahl
- `numpy.single`: Einfachgenauigkeit Gleitkommazahl (plattformabhängig definiert)
- `numpy.double`: Doppelte Genauigkeit Gleitkommazahl (plattformabhängig definiert)
- `numpy.longdouble`: Erweiterte Genauigkeit Gleitkommazahl (plattformabhängig definiert)
- `numpy.csingle`: Komplexe Zahl, dargestellt durch zwei Einfachgenauigkeits-Gleitkommazahlen
- `numpy.cdouble`: Komplexe Zahl, dargestellt durch zwei Doppelte Genauigkeits-Gleitkommazahlen
- `numpy.clongdouble`: Komplexe Zahl, dargestellt durch zwei Erweiterte Genauigkeits-Gleitkommazahlen

Diese Datentypen haben plattformabhängige Definitionen, aber NumPy bietet auch feste Größen-Aliasnamen für die Bequemlichkeit.
