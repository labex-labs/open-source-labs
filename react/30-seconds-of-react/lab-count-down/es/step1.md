# Temporizador倒计时器

> En la máquina virtual ya se han proporcionado `index.html` y `script.js`. En general, solo es necesario agregar código a `script.js` y `style.css`.

Este código crea un temporizador倒计时器 que imprime un mensaje cuando llega a cero. Para implementarlo, se siguen los siguientes pasos:

1. Utilice el hook `useState()` para crear una variable de estado `time` que almacene el valor del tiempo. Inicialícela a partir de las propiedades y desestructúrela en sus componentes.
2. Utilice el hook `useState()` para crear las variables de estado `paused` y `over`, que se utilizan para evitar que el temporizador marque si está en pausa o se agotó el tiempo.
3. Cree un método `tick` que actualice los valores del tiempo en función del valor actual (es decir, disminuyendo el tiempo en un segundo).
4. Cree un método `reset` que restablezca todas las variables de estado a sus estados iniciales.
5. Utilice el hook `useEffect()` para llamar al método `tick` cada segundo a través de `setInterval()` y use `clearInterval()` para limpiar cuando el componente se desmonta.
6. Utilice `String.prototype.padStart()` para rellenar cada parte del arreglo de tiempo con dos caracteres para crear la representación visual del temporizador.

```jsx
const CountDown = ({ hours = 0, minutes = 0, seconds = 0 }) => {
  const [paused, setPaused] = React.useState(false);
  const [over, setOver] = React.useState(false);
  const [[h, m, s], setTime] = React.useState([hours, minutes, seconds]);

  const tick = () => {
    if (paused || over) return;
    if (h === 0 && m === 0 && s === 0) setOver(true);
    else if (m === 0 && s === 0) setTime([h - 1, 59, 59]);
    else if (s == 0) setTime([h, m - 1, 59]);
    else setTime([h, m, s - 1]);
  };

  const reset = () => {
    setTime([parseInt(hours), parseInt(minutes), parseInt(seconds)]);
    setPaused(false);
    setOver(false);
  };

  React.useEffect(() => {
    const timerID = setInterval(tick, 1000);
    return () => clearInterval(timerID);
  });

  return (
    <div>
      <p>
        {`${h.toString().padStart(2, "0")}:${m.toString().padStart(2, "0")}:${s
          .toString()
          .padStart(2, "0")}`}
      </p>
      {over && <div>Se acabó el tiempo!</div>}
      <button onClick={() => setPaused(!paused)}>
        {paused ? "Reanudar" : "Pausar"}
      </button>
      <button onClick={reset}>Reiniciar</button>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <CountDown hours={1} minutes={45} />
);
```

Haga clic en 'Go Live' en la esquina inferior derecha para ejecutar el servicio web en el puerto 8080. Luego, puede actualizar la pestaña **Web 8080** para previsualizar la página web.
