# Temporizador de Contagem Regressiva

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Este código cria um temporizador de contagem regressiva que imprime uma mensagem quando atinge zero. Para implementá-lo, as seguintes etapas são tomadas:

1. Use o hook `useState()` para criar uma variável de estado `time` que armazena o valor do tempo. Inicialize-a a partir das props e desestruture-a em seus componentes.
2. Use o hook `useState()` para criar as variáveis de estado `paused` e `over`, que são usadas para impedir que o temporizador avance se estiver pausado ou se o tempo tiver acabado.
3. Crie um método `tick` que atualiza os valores do tempo com base no valor atual (ou seja, diminuindo o tempo em um segundo).
4. Crie um método `reset` que redefine todas as variáveis de estado para seus estados iniciais.
5. Use o hook `useEffect()` para chamar o método `tick` a cada segundo por meio do uso de `setInterval()` e use `clearInterval()` para limpar quando o componente for desmontado.
6. Use `String.prototype.padStart()` para preencher cada parte do array de tempo com dois caracteres para criar a representação visual do temporizador.

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
      {over && <div>Time's up!</div>}
      <button onClick={() => setPaused(!paused)}>
        {paused ? "Resume" : "Pause"}
      </button>
      <button onClick={reset}>Restart</button>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <CountDown hours={1} minutes={45} />
);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
