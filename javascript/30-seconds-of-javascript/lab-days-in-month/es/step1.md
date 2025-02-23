# Función de JavaScript para Obtener el Número de Días en un Mes

Para encontrar el número de días en un mes específico de un año dado usando JavaScript, siga estos pasos:

1. Abra la Terminal/SSH y escriba `node` para comenzar a practicar la codificación.
2. Cree una función llamada `daysInMonth` que tome dos parámetros: `year` (año) y `month` (mes).
3. Dentro de la función `daysInMonth`, use el constructor `Date` para crear un objeto de fecha a partir del `year` y `month` dados.
4. Establezca el parámetro de días en `0` para obtener el último día del mes anterior, ya que los meses están indexados a partir de cero.
5. Use `Date.prototype.getDate()` para devolver el número de días en el `month` dado.
6. Devuelva el número de días desde la función `daysInMonth`.

Aquí está el código de JavaScript para la función `daysInMonth`:

```js
const daysInMonth = (year, month) => new Date(year, month, 0).getDate();
```

Puede usar la función `daysInMonth` para obtener el número de días en cualquier mes de cualquier año, como se muestra en estos ejemplos:

```js
daysInMonth(2020, 12); // 31
daysInMonth(2024, 2); // 29
```
