# React usePrevious Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para armazenar o estado ou as props anteriores, você pode criar um hook customizado. Aqui estão os passos:

1.  Defina um hook customizado que recebe um argumento `value`.
2.  Use o hook `useRef()` para criar uma `ref` para o `value`.
3.  Use o hook `useEffect()` para lembrar o último `value`.
4.  Retorne o valor `ref.current`.

```jsx
const usePrevious = (value) => {
  const ref = React.useRef();
  React.useEffect(() => {
    ref.current = value;
  });
  return ref.current;
};
```

Aqui está um exemplo de como usar o hook `usePrevious`:

```jsx
const Counter = () => {
  const [value, setValue] = React.useState(0);
  const lastValue = usePrevious(value);

  return (
    <div>
      <p>
        Current: {value} - Previous: {lastValue}
      </p>
      <button onClick={() => setValue(value + 1)}>Increment</button>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

O componente `Counter` exibe os valores atual e anterior de `value`. Quando o botão `Increment` é clicado, `value` é atualizado e o valor anterior é armazenado usando o hook `usePrevious`.

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
