# N pares de paréntesis

## Problema

El problema consiste en encontrar todas las combinaciones válidas de n-pares de paréntesis. Una combinación válida es aquella en la que cada paréntesis de apertura tiene un paréntesis de cierre correspondiente y los pares de paréntesis están correctamente anidados. Por ejemplo, las siguientes son combinaciones válidas de 3-pares de paréntesis:

- ((()))
- (()())
- (())()
- ()(())
- ()()()

Las siguientes no son combinaciones válidas de 3-pares de paréntesis:

- )()(
- ((()
- ))((
- ()()()

## Requisitos

Para resolver este problema, debemos responder a las siguientes preguntas:

- ¿La entrada es un entero que representa el número de pares?
  - Sí, la entrada es un entero que representa el número de pares.
- ¿Podemos asumir que las entradas son válidas?
  - No, no podemos asumir que las entradas son válidas.
- ¿La salida es una lista de combinaciones válidas?
  - Sí, la salida es una lista de combinaciones válidas.
- ¿La salida debe tener duplicados?
  - No, la salida no debe tener duplicados.
- ¿Podemos asumir que esto cabe en memoria?
  - Sí, podemos asumir que esto cabe en memoria.

## Uso de ejemplo

Los siguientes son usos de ejemplo de la función:

- Ninguno -> Excepción
- Negativo -> Excepción
- 0 -> []
- 1 -> ['()']
- 2 -> ['(())', '()()']
- 3 -> ['((()))', '(()())', '(())()', '()(())', '()()()']
