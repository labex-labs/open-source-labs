# Introducción

En este laboratorio (lab), aprenderás sobre la delegación de generadores en Python utilizando la declaración `yield from`. Esta característica, introducida en Python 3.3, simplifica el código que depende de generadores y corutinas.

Los generadores son funciones especiales que pueden pausar y reanudar la ejecución, conservando su estado entre llamadas. La declaración `yield from` ofrece una forma elegante de delegar el control a otro generador, mejorando la legibilidad y mantenibilidad del código.

**Objetivos:**

- Comprender el propósito de la declaración `yield from`
- Aprender cómo usar `yield from` para delegar a otros generadores
- Aplicar este conocimiento para simplificar el código basado en corutinas
- Comprender la conexión con la sintaxis moderna de async/await

**Archivos con los que trabajarás:**

- `cofollow.py` - Contiene funciones de utilidad de corutinas
- `server.py` - Contiene una implementación simple de servidor de red
