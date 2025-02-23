# Función para convertir números en sufijo ordinal

Para convertir un número en un sufijo ordinal, utiliza la función `toOrdinalSuffix`.

- Abre la Terminal/SSH y escribe `node` para comenzar a practicar la codificación.
- La función toma un número como entrada y lo devuelve como una cadena con el sufijo correcto del indicador ordinal.
- Utiliza el operador módulo (`%`) para encontrar los valores de los dígitos de unidades y decenas.
- Encuentra qué patrón de dígitos ordinales coincide.
- Si el dígito se encuentra en el patrón de los adolescentes, utiliza el ordinal de los adolescentes.

```js
const toOrdinalSuffix = (num) => {
  const int = parseInt(num),
    digits = [int % 10, int % 100],
    ordinals = ["st", "nd", "rd", "th"],
    oPattern = [1, 2, 3, 4],
    tPattern = [11, 12, 13, 14, 15, 16, 17, 18, 19];
  return oPattern.includes(digits[0]) && !tPattern.includes(digits[1])
    ? int + ordinals[digits[0] - 1]
    : int + ordinals[3];
};
```

A continuación, se muestra un ejemplo de uso de la función `toOrdinalSuffix`:

```js
toOrdinalSuffix("123"); // '123rd'
```
