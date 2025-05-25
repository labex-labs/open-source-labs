# React useDebounce Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para debouncer um determinado valor, você pode criar um custom hook que recebe um `value` e um `delay`. Use o hook `useState()` para armazenar o valor debounced e o hook `useEffect()` para atualizar o valor debounced toda vez que `value` é atualizado. Para atrasar a invocação do setter da variável de estado anterior por `delay` ms, use `setTimeout()`. Para limpar ao desmontar o componente, use `clearTimeout()`. Isso é particularmente útil ao lidar com a entrada do usuário.

Aqui está um exemplo de implementação do hook `useDebounce()`:

```jsx
const useDebounce = (value, delay) => {
  const [debouncedValue, setDebouncedValue] = React.useState(value);

  React.useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);

    return () => {
      clearTimeout(handler);
    };
  }, [value, delay]);

  return debouncedValue;
};
```

Você pode usar o hook `useDebounce()` em um componente assim:

```jsx
const Counter = () => {
  const [value, setValue] = React.useState(0);
  const lastValue = useDebounce(value, 500);

  return (
    <div>
      <p>
        Current: {value} - Debounced: {lastValue}
      </p>
      <button onClick={() => setValue(value + 1)}>Increment</button>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
