# Lesen von Attributen mit Vererbung

Logisch gesehen verläuft der Prozess zum Finden eines Attributs wie folgt. Zunächst wird im lokalen `__dict__` nachgeschaut. Wenn es nicht gefunden wird, wird im `__dict__` der Klasse gesucht. Wenn es in der Klasse nicht gefunden wird, wird in den Basisklassen über `__bases__` gesucht. Es gibt jedoch einige subtilere Aspekte, die im Folgenden besprochen werden.
