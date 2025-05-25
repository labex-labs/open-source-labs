# React useClickInside Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Para lidar com um evento de clique dentro de um componente, você pode criar um custom hook chamado `useClickInside` que recebe um `ref` e um `callback`. Use o hook `useEffect()` para anexar e limpar o evento `click`, e o hook `useRef()` para criar um `ref` para o seu componente de clique e passá-lo para o hook `useClickInside`. Aqui está o código:

```jsx
const useClickInside = (ref, callback) => {
  const handleClick = (e) => {
    if (ref.current && ref.current.contains(e.target)) {
      callback();
    }
  };

  React.useEffect(() => {
    document.addEventListener("click", handleClick);
    return () => {
      document.removeEventListener("click", handleClick);
    };
  }, [ref, callback]);
};
```

Você pode usar este hook em seu componente assim:

```jsx
const ClickBox = ({ onClickInside }) => {
  const clickRef = React.useRef();
  useClickInside(clickRef, onClickInside);

  return (
    <div
      className="click-box"
      ref={clickRef}
      style={{
        border: "2px dashed orangered",
        height: 200,
        width: 400,
        display: "flex",
        justifyContent: "center",
        alignItems: "center"
      }}
    >
      <p>Click inside this element</p>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <ClickBox onClickInside={() => alert("click inside")} />
);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
