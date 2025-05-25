# React useClickOutside Hook

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Este código lida com o evento de clicar fora de um componente encapsulado. Ele funciona criando um hook personalizado que recebe uma `ref` e um `callback` para lidar com o evento `click`. O hook `useEffect()` é usado para adicionar e limpar o evento `click`, enquanto o hook `useRef()` é usado para criar uma `ref` para o componente de clique e passá-la para o hook `useClickOutside`.

```jsx
const useClickOutside = (ref, callback) => {
  const handleClick = (e) => {
    if (ref.current && !ref.current.contains(e.target)) {
      callback();
    }
  };
  React.useEffect(() => {
    document.addEventListener("click", handleClick);
    return () => {
      document.removeEventListener("click", handleClick);
    };
  });
};

const ClickBox = ({ onClickOutside }) => {
  const clickRef = React.useRef();
  useClickOutside(clickRef, onClickOutside);
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
      <p>Click out of this element</p>
    </div>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(
  <ClickBox onClickOutside={() => alert("click outside")} />
);
```

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
