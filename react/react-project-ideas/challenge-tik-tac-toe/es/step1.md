# Tres en raya

Para comenzar, abre el editor. Puedes ver los siguientes archivos desde tu editor.

```txt
├── public
├── src
│   ├── components
│   │   ├── common
│   │   │   └── Utils.js
│   │   ├── Tablero.js
│   │   ├── Juego.js
│   │   └── Cuadrado.js
│   ├── App.css
│   ├── App.js
│   ├── App.test.js
│   ├── index.css
│   ├── index.js
│   ├── logo.svg
│   ├── reportWebVitals.js
│   └── setupTests.js
├── package-lock.json
└── package.json
```

## Requisitos

- Para instalar las dependencias del proyecto, utiliza el siguiente comando:

  ```bash
  npm i
  ```

- Por favor, completa este desafío en el archivo `src/components/Juego.js`.
- Utiliza el hook `useState` para definir tres variables de estado: tablero, turnoX y ganador.
  - `tablero` representa el estado del tablero de juego. Se inicializa como un array de 9 elementos, donde cada elemento se establece inicialmente en null.
  - `turnoX` es una bandera booleana que indica si es el turno actual de X.
  - `ganador` almacena el resultado de la función `calcularGanador`, que determina al ganador basado en el estado actual del tablero.
- La función `manejarClic` se llama cuando se hace clic en un cuadrado del tablero de juego.
  - Crea una copia del estado actual del tablero utilizando el operador de propagación (`[...tablero]`) y la asigna a tmpTablero.
  - Si ya hay un ganador (ganador es verdadero) o el cuadrado clicado ya está marcado (`tmpTablero[i]` es verdadero), la función devuelve sin hacer ningún cambio.
  - De lo contrario, actualiza el valor del cuadrado clicado en `tmpTablero` a "X" o "O" según el valor de `turnoX`.
  - Luego, el `tmpTablero` actualizado se establece como el nuevo valor para el estado del tablero utilizando `setTablero`, y `turnoX` se invierte utilizando `setTurnoX`.

## Ejemplo

Una vez que hayas terminado el código, ejecútalo con el siguiente comando:

```bash
npm start
```

El resultado final es el siguiente:

![Demo del juego Tres en raya](../assets/terminado.gif)
