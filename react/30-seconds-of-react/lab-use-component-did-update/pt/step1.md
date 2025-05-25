# Hook useComponentDidUpdate do React

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Este código fornece um hook personalizado chamado `useComponentDidUpdate` que executa uma função `callback` fornecida sempre que um componente é atualizado. Aqui estão as etapas que o hook segue:

1.  Crie uma variável `mounted` usando o hook `useRef()`. Esta variável rastreia se o componente foi montado ou não.
2.  Use o hook `useEffect()` para definir o valor de `mounted` como `true` na primeira vez que o hook é executado.
3.  Em execuções subsequentes do hook, execute a função `callback` fornecida somente se o componente já tiver sido montado.
4.  Se um segundo argumento `condition` for fornecido, o hook só será executado se alguma de suas dependências mudar.
5.  Este hook se comporta como o método de ciclo de vida `componentDidUpdate()` dos componentes de classe.

Aqui está o código:

```jsx
const useComponentDidUpdate = (callback, condition) => {
  const isMounted = React.useRef(false);
  React.useEffect(() => {
    if (isMounted.current) {
      callback();
    } else {
      isMounted.current = true;
    }
  }, condition);
};

const App = () => {
  const [value, setValue] = React.useState(0);
  const [otherValue, setOtherValue] = React.useState(1);

  useComponentDidUpdate(() => {
    console.log(`Current value is ${value}.`);
  }, [value]);

  return (
    <>
      <p>
        Value: {value}, other value: {otherValue}
      </p>
      <button onClick={() => setValue(value + 1)}>Increment value</button>
      <button onClick={() => setOtherValue(otherValue + 1)}>
        Increment other value
      </button>
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<App />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
