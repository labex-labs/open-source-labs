# Juego de la Serpiente

Para comenzar, abre el editor. Puedes ver los siguientes archivos desde tu editor.

```txt
├── public
├── src
│   ├── components
│   │   ├── Food.js
│   │   └── Snake.js
│   ├── App.css
│   ├── App.js
│   ├── index.css
│   └── index.js
├── package-lock.json
└── package.json
```

## Requisitos

- Para instalar las dependencias del proyecto, utiliza el siguiente comando:

  ```bash
  npm i
  ```

- Por favor, completa este desafío en el archivo `src/App.js`.
- La función `randomFoodPosition` está definida para generar una posición aleatoria para el ítem de comida en el tablero de juego.
- Dentro de la función App, hay varias variables de estado definidas utilizando el hook useState:
  - `snake` representa el estado actual de la serpiente.
  - `lastDirection` representa la última dirección en la que se movió la serpiente.
  - `foodPosition` representa la posición actual del ítem de comida.
  - `isStarted` determina si el juego ha comenzado.
  - `gameOver` indica si el juego ha terminado.
  - `playgroundRef` es una referencia al elemento del tablero de juego.

## Ejemplo

Una vez que hayas completado el código, ejecútalo con el siguiente comando:

```bash
npm start
```

El resultado final es el siguiente:

![Snake game final result](../assets/finished.gif)
