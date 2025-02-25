# Kopien und Ansichten verstehen

NumPy-Arrays bestehen aus zwei Teilen: dem Datenpuffer und den Metadaten. Der Datenpuffer enthält die tatsächlichen Datenelemente, während die Metadaten Informationen wie Datentyp und Schritte umfassen.

Wenn Sie mit NumPy-Arrays arbeiten, ist es wichtig, den Unterschied zwischen Kopien und Ansichten zu verstehen:

- Eine **Ansicht** ermöglicht es Ihnen, das Array unterschiedlich zuzugreifen, indem Sie bestimmte Metadaten ändern, ohne den Datenpuffer zu verändern. Alle Änderungen, die an einer Ansicht vorgenommen werden, werden im ursprünglichen Array widergespiegelt.

- Eine **Kopie** ist ein neues Array, das sowohl den Datenpuffer als auch die Metadaten dupliziert. Änderungen, die an einer Kopie vorgenommen werden, werden das ursprüngliche Array nicht beeinflussen.
