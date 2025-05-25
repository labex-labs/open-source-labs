# React useError Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Este código cria um despachante de erros. Ele usa três hooks do React para gerenciar o estado de erro e despachá-lo para a interface do usuário.

Veja como o código funciona:

1. O hook `useState()` cria uma variável de estado chamada `error` que armazena o objeto de erro. Ele recebe um valor inicial de `err`, que é passado como um argumento para o hook.

2. O hook `useEffect()` é usado para "lançar" o erro sempre que for avaliado como verdadeiro (truthy). Este hook recebe uma função e um array de dependências como argumentos. Neste caso, a função verifica se a variável de estado `error` é avaliada como verdadeira (ou seja, não nula, indefinida, 0, falsa ou uma string vazia) e a lança se for. O array de dependências é `[error]`, o que significa que o efeito será executado novamente sempre que a variável `error` mudar.

3. O hook `useCallback()` é usado para criar uma função em cache chamada `dispatchError`, que atualiza a variável de estado `error` e retorna a nova função. Este hook recebe uma função e um array de dependências como argumentos. Neste caso, a função recebe um argumento `err`, que é o novo objeto de erro a ser despachado. O array de dependências é `[]`, o que significa que a função em cache só será recriada se o componente for renderizado novamente.

Aqui está um exemplo de como usar o hook `useError()` em um componente:

1. Crie um novo componente chamado `ErrorButton`.

2. Dentro do componente, chame o hook `useError()` para obter a função `dispatchError`.

3. Crie uma função de manipulador de clique chamada `clickHandler` que chama `dispatchError` com um novo objeto de erro.

4. Renderize um botão que chama `clickHandler` quando clicado.

Aqui está o código:

```jsx
const useError = (err = null) => {
  const [error, setError] = React.useState(err);

  React.useEffect(() => {
    if (error) {
      throw error;
    }
  }, [error]);

  const dispatchError = React.useCallback((err) => {
    setError(err);
  }, []);

  return dispatchError;
};

const ErrorButton = () => {
  const dispatchError = useError();

  const clickHandler = () => {
    dispatchError(new Error("Error!"));
  };

  return <button onClick={clickHandler}>Throw error</button>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<ErrorButton />);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
