# Das Problem verstehen

Bevor wir mit der Erkundung von Metaklassen beginnen, ist es wichtig, das Problem zu verstehen, das wir lösen möchten. In der Programmierung müssen wir oft Strukturen mit bestimmten Typen für ihre Attribute erstellen. In unserer vorherigen Arbeit haben wir ein System für typüberprüfte Strukturen entwickelt. Dieses System ermöglicht es uns, Klassen zu definieren, bei denen jedes Attribut einen bestimmten Typ hat und die den Attributen zugewiesenen Werte gemäß diesem Typ validiert werden.

Hier ist ein Beispiel, wie wir dieses System verwendet haben, um eine `Stock`-Klasse zu erstellen:

```python
from validate import String, PositiveInteger, PositiveFloat
from structure import Structure

class Stock(Structure):
    name = String()
    shares = PositiveInteger()
    price = PositiveFloat()

    @property
    def cost(self):
        return self.shares * self.price

    def sell(self, nshares: PositiveInteger):
        self.shares -= nshares
```

In diesem Code importieren wir zunächst die Validator-Typen (`String`, `PositiveInteger`, `PositiveFloat`) aus dem `validate`-Modul und die `Structure`-Klasse aus dem `structure`-Modul. Dann definieren wir die `Stock`-Klasse, die von `Structure` erbt. Innerhalb der `Stock`-Klasse definieren wir Attribute mit bestimmten Validator-Typen. Beispielsweise muss das `name`-Attribut eine Zeichenkette sein, `shares` muss eine positive Ganzzahl sein und `price` muss eine positive Fließkommazahl sein.

Es gibt jedoch ein Problem mit diesem Ansatz. Wir müssen alle Validator-Typen am Anfang unserer Datei importieren. Wenn wir in einem realen Szenario immer mehr Validator-Typen hinzufügen, können diese Importe sehr lang und schwierig zu verwalten werden. Dies könnte uns dazu verleiten, `from validate import *` zu verwenden, was im Allgemeinen als schlechter Stil angesehen wird, da es Namenskonflikte verursachen und den Code weniger lesbar machen kann.

Um unseren Ausgangspunkt zu verstehen, schauen wir uns die `Structure`-Klasse an. Sie müssen die Datei `structure.py` im Editor öffnen und ihren Inhalt untersuchen. Dies hilft Ihnen zu verstehen, wie die grundlegende Strukturverarbeitung implementiert ist, bevor wir Metaklassen-Funktionalität hinzufügen.

```bash
code structure.py
```

Wenn Sie die Datei öffnen, sehen Sie eine grundlegende Implementierung der `Structure`-Klasse. Diese Klasse ist für die Initialisierung der Attribute verantwortlich, hat aber noch keine Metaklassen-Funktionalität.

Als Nächstes untersuchen wir die Validator-Klassen. Diese Klassen sind in der Datei `validate.py` definiert. Sie haben bereits Descriptor-Funktionalität, was bedeutet, dass sie steuern können, wie Attribute zugegriffen und gesetzt werden. Wir müssen sie jedoch verbessern, um das Importproblem zu lösen, das wir zuvor besprochen haben.

```bash
code validate.py
```

Indem Sie sich diese Validator-Klassen ansehen, verstehen Sie besser, wie der Validierungsprozess funktioniert und welche Änderungen wir vornehmen müssen, um unseren Code zu verbessern.
