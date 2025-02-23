# Conversión de grados a radianes

Para convertir un ángulo de grados a radianes, sigue estos pasos:

1. Abre la Terminal/SSH.
2. Escribe `node` para comenzar a codificar.
3. Utiliza la fórmula de conversión de grados a radianes junto con `Math.PI`.
4. Aplica la fórmula al ángulo en grados para obtener el ángulo en radianes.

Aquí está la fórmula en JavaScript:

```js
const degreesToRads = (deg) => (deg * Math.PI) / 180.0;
```

Por ejemplo, si quieres convertir 90 grados a radianes, puedes usar la función `degreesToRads` de la siguiente manera:

```js
degreesToRads(90.0); // ~1.5708
```
