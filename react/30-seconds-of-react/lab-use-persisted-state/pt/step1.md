# Hook React usePersistedState

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Este hook retorna um valor com estado que é persistido no `localStorage`, juntamente com uma função que pode ser usada para atualizá-lo. Para usá-lo, siga estes passos:

1. Use o hook `useState()` para inicializar o `value` para `defaultValue`.
2. Use o hook `useRef()` para criar uma ref que irá conter o `name` do valor em `Window.localStorage`.
3. Use 3 instâncias do hook `useEffect()` para inicialização, mudança de `value` e mudança de `name`, respectivamente.
4. Quando o componente é montado pela primeira vez, use `Storage.getItem()` para atualizar o `value` se houver um valor armazenado, ou `Storage.setItem()` para persistir o valor atual.
5. Quando o `value` é atualizado, use `Storage.setItem()` para armazenar o novo valor.
6. Quando o `name` é atualizado, use `Storage.setItem()` para criar a nova chave, atualizar o `nameRef` e use `Storage.removeItem()` para remover a chave anterior de `Window.localStorage`.
7. Observe que o hook é destinado ao uso com valores primitivos (ou seja, não objetos) e não leva em conta as alterações no `Window.localStorage` devido a outro código. Ambos esses problemas podem ser facilmente resolvidos (por exemplo, serialização JSON e tratamento do evento `'storage'`).

Aqui está o código:

```jsx
const usePersistedState = (name, defaultValue) => {
  const [value, setValue] = React.useState(defaultValue);
  const nameRef = React.useRef(name);

  React.useEffect(() => {
    try {
      const storedValue = localStorage.getItem(name);
      if (storedValue !== null) {
        setValue(storedValue);
      } else {
        localStorage.setItem(name, defaultValue);
      }
    } catch {
      setValue(defaultValue);
    }
  }, []);

  React.useEffect(() => {
    try {
      localStorage.setItem(nameRef.current, value);
    } catch {}
  }, [value]);

  React.useEffect(() => {
    const lastName = nameRef.current;
    if (name !== lastName) {
      try {
        localStorage.setItem(name, value);
        nameRef.current = name;
        localStorage.removeItem(lastName);
      } catch {}
    }
  }, [name]);

  return [value, setValue];
};
```

```jsx
const MyComponent = ({ name }) => {
  const [value, setValue] = usePersistedState(name, 10);

  const handleInputChange = (event) => {
    setValue(event.target.value);
  };

  return <input value={value} onChange={handleInputChange} />;
};

const MyApp = () => {
  const [name, setName] = React.useState("my-value");

  const handleInputChange = (event) => {
    setName(event.target.value);
  };

  return (
    <>
      <MyComponent name={name} />
      <input value={name} onChange={handleInputChange} />
    </>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
