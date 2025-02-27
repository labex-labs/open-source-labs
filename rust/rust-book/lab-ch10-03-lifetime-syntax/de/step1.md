# Validating References with Lifetimes

Lebenszeiten sind eine weitere Art von Generics, die wir bereits verwendet haben. Anstatt sicherzustellen, dass ein Typ das Verhalten hat, das wir wollen, gewährleisten Lebenszeiten, dass Referenzen so lange gültig sind, wie wir sie benötigen.

Ein Detail, das wir in "References and Borrowing" nicht besprochen haben, ist, dass jede Referenz in Rust eine _Lebenszeit_ hat, die der Bereich ist, für den diese Referenz gültig ist. Die meiste Zeit sind Lebenszeiten implizit und werden inferiert, genauso wie die meiste Zeit Typen inferiert werden. Wir müssen nur dann Typen annotieren, wenn mehrere Typen möglich sind. Auf ähnliche Weise müssen wir Lebenszeiten annotieren, wenn die Lebenszeiten von Referenzen auf einige verschiedene Weise zusammenhängen können. Rust erfordert, dass wir die Beziehungen mit generischen Lebenszeitparametern annotieren, um sicherzustellen, dass die tatsächlich verwendeten Referenzen zur Laufzeit definitiv gültig sein werden.

Das Annotieren von Lebenszeiten ist sogar kein Begriff, den die meisten anderen Programmiersprachen haben, daher wird dies unvertraut vorkommen. Obwohl wir in diesem Kapitel die Lebenszeiten nicht vollständig behandeln werden, werden wir die gängigen Arten besprechen, wie du die Lebenszeitssyntax antreffen könntest, damit du mit dem Konzept vertraut wirst.
