# React useEffectOnce Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

O código abaixo implementa uma função `useEffectOnce(callback, when)` que executa um `callback` apenas uma vez quando uma condição `when` se torna verdadeira.

Para implementar esta função:

- Crie uma variável `hasRunOnce` usando o hook `useRef()` para rastrear o status de execução do efeito.
- Use o hook `useEffect()` que é executado apenas quando a condição `when` muda.
- Dentro do hook `useEffect()`, verifique se `when` é `true` e se o efeito não foi executado antes. Se ambos forem `true`, execute `callback` e defina `hasRunOnce` como `true`.

```jsx
const useEffectOnce = (callback, when) => {
  const hasRunOnce = React.useRef(false);
  React.useEffect(() => {
    if (when && !hasRunOnce.current) {
      callback();
      hasRunOnce.current = true;
    }
  }, [when]);
};
```

Aqui está um exemplo de uso de `useEffectOnce()`:

```jsx
const App = () => {
  const [clicked, setClicked] = React.useState(false);
  useEffectOnce(() => {
    console.log("mounted");
  }, clicked);
  return <button onClick={() => setClicked(true)}>Click me</button>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

No exemplo, `useEffectOnce()` é usado para registrar "mounted" no console quando o botão é clicado pela primeira vez. O hook `useEffectOnce()` recebe dois argumentos: o `callback` a ser executado e a condição `when` a ser verificada. A condição `when` é definida para o estado `clicked`, então o `callback` é executado apenas quando `clicked` é `true` pela primeira vez.

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
