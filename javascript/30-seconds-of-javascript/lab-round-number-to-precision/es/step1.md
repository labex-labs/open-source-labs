# Así es como se redondea un número a una precisión dada en JavaScript:

```
const round = (n, decimals = 0) =>
  Number(`${Math.round(`${n}e${decimals}`)}e-${decimals}`);
```

- Utiliza `Math.round()` y los literales de plantilla para redondear el número al número especificado de dígitos.
- Si quieres redondear a un entero, omite el segundo argumento, `decimals`.
- Para comenzar a practicar la codificación, abre la Terminal/SSH y escribe `node`.
- Por ejemplo, `round(1.005, 2)` devolverá `1.01`.
