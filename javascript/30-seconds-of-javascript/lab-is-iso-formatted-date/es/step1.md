# Comprender el formato de fecha ISO y los objetos Date de JavaScript

Antes de comenzar a codificar, entendamos qué es el formato de fecha ISO 8601 y cómo JavaScript maneja las fechas.

## El formato de fecha ISO 8601

El formato ISO 8601 es un estándar internacional para representar fechas y horas. El formato ISO extendido simplificado tiene el siguiente aspecto:

```
YYYY-MM-DDTHH:mm:ss.sssZ
```

Donde:

- `YYYY` representa el año (cuatro dígitos)
- `MM` representa el mes (dos dígitos)
- `DD` representa el día (dos dígitos)
- `T` es un carácter literal que separa la fecha y la hora
- `HH` representa las horas (dos dígitos)
- `mm` representa los minutos (dos dígitos)
- `ss` representa los segundos (dos dígitos)
- `sss` representa los milisegundos (tres dígitos)
- `Z` indica la zona horaria UTC (hora Zulu)

Por ejemplo, `2023-05-12T14:30:15.123Z` representa el 12 de mayo de 2023, a las 2:30:15.123 PM UTC.

## El objeto Date de JavaScript

JavaScript proporciona un objeto `Date` incorporado para trabajar con fechas y horas. Cuando creas un nuevo objeto `Date`, puedes pasarle una cadena en formato ISO:

```javascript
const date = new Date("2023-05-12T14:30:15.123Z");
```

Abriremos la terminal y practicaremos el trabajo con objetos Date:

1. Abre la Terminal haciendo clic en el menú Terminal en la parte superior del WebIDE
2. Escribe `node` y presiona Enter para iniciar la shell interactiva de Node.js
3. Crea un nuevo objeto Date para la hora actual:

```javascript
const now = new Date();
console.log(now);
```

![node-prompt](../assets/screenshot-20250306-odDaT5Rp@2x.png)

4. Convierte este objeto Date en una cadena ISO:

```javascript
const isoString = now.toISOString();
console.log(isoString);
```

Deberías ver una salida similar a:

```
2023-05-12T14:30:15.123Z
```

5. Crea una fecha a partir de una cadena ISO:

```javascript
const dateFromIso = new Date("2023-05-12T14:30:15.123Z");
console.log(dateFromIso);
```

![node-prompt](../assets/screenshot-20250306-dbkCLkf7@2x.png)

Esto demuestra cómo JavaScript puede analizar y crear objetos Date a partir de cadenas en formato ISO.
