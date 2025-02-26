# Introducción

**Objetivos:**

- Aprender sobre generadores administrados

**Archivos creados:** `multitask.py`, `server.py`

Una función generadora o de corrutina nunca puede ejecutarse sin ser impulsada por algún otro código. Por ejemplo, un generador utilizado para iteración no hace nada a menos que se realice una iteración utilizando un bucle `for`. Del mismo modo, una colección de corrutinas no se ejecutará a menos que se invoque de alguna manera su método `send()`.

En aplicaciones avanzadas de generadores, es posible impulsar los generadores de varias maneras inusuales. En este ejercicio, examinamos algunos ejemplos.
