# Área de Arrastar e Soltar Arquivos (File Drag and Drop Area)

> `index.html` e `script.js` já foram fornecidos na VM. Em geral, você só precisa adicionar código a `script.js` e `style.css`.

Este componente permite a funcionalidade de arrastar e soltar para um único arquivo. Para implementar este componente, siga estes passos:

1. Crie uma referência chamada `dropRef` e vincule-a ao wrapper do componente.
2. Use o hook `useState()` para criar as variáveis `drag` e `filename`. Inicialize-as para `false` e `''` respectivamente.
3. As variáveis `dragCounter` e `drag` são usadas para determinar se um arquivo está sendo arrastado, enquanto `filename` é usado para armazenar o nome do arquivo solto.
4. Crie os métodos `handleDrag`, `handleDragIn`, `handleDragOut` e `handleDrop` para lidar com a funcionalidade de arrastar e soltar. `handleDrag` impede que o navegador abra o arquivo arrastado, `handleDragIn` e `handleDragOut` lidam com a entrada e saída do arquivo arrastado do componente, e `handleDrop` lida com o arquivo sendo solto e o passa para `onDrop`.
5. Use o hook `useEffect()` para lidar com cada um dos eventos de arrastar e soltar usando os métodos criados anteriormente.

Aqui está o CSS para o componente:

```css
.filedrop {
  min-height: 120px;
  border: 3px solid #d3d3d3;
  text-align: center;
  font-size: 24px;
  padding: 32px;
  border-radius: 4px;
}

.filedrop.drag {
  border: 3px dashed #1e90ff;
}

.filedrop.ready {
  border: 3px solid #32cd32;
}
```

Aqui está o JSX para o componente:

```jsx
const FileDrop = ({ onDrop }) => {
  const [drag, setDrag] = React.useState(false);
  const [filename, setFilename] = React.useState("");
  const dropRef = React.useRef(null);
  let dragCounter = 0;

  const handleDrag = (e) => {
    e.preventDefault();
    e.stopPropagation();
  };

  const handleDragIn = (e) => {
    e.preventDefault();
    e.stopPropagation();
    dragCounter++;
    if (e.dataTransfer.items && e.dataTransfer.items.length > 0) setDrag(true);
  };

  const handleDragOut = (e) => {
    e.preventDefault();
    e.stopPropagation();
    dragCounter--;
    if (dragCounter === 0) setDrag(false);
  };

  const handleDrop = (e) => {
    e.preventDefault();
    e.stopPropagation();
    setDrag(false);
    if (e.dataTransfer.files && e.dataTransfer.files.length > 0) {
      onDrop(e.dataTransfer.files[0]);
      setFilename(e.dataTransfer.files[0].name);
      e.dataTransfer.clearData();
      dragCounter = 0;
    }
  };

  React.useEffect(() => {
    const div = dropRef.current;
    div.addEventListener("dragenter", handleDragIn);
    div.addEventListener("dragleave", handleDragOut);
    div.addEventListener("dragover", handleDrag);
    div.addEventListener("drop", handleDrop);
    return () => {
      div.removeEventListener("dragenter", handleDragIn);
      div.removeEventListener("dragleave", handleDragOut);
      div.removeEventListener("dragover", handleDrag);
      div.removeEventListener("drop", handleDrop);
    };
  }, []);

  return (
    <div
      ref={dropRef}
      className={
        drag ? "filedrop drag" : filename ? "filedrop ready" : "filedrop"
      }
    >
      {filename && !drag ? <div>{filename}</div> : <div>Drop a file here!</div>}
    </div>
  );
};
```

Para usar o componente, chame `ReactDOM.createRoot(document.getElementById('root')).render(<FileDrop onDrop={console.log} />);`

Por favor, clique em 'Go Live' no canto inferior direito para executar o serviço web na porta 8080. Em seguida, você pode atualizar a aba **Web 8080** para visualizar a página web.
