# ファイルのドラッグアンドドロップエリア

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加する必要があります。

このコンポーネントは、単一のファイルに対するドラッグアンドドロップ機能を備えています。このコンポーネントを実装するには、次の手順に従ってください。

1. `dropRef` という参照を作成し、コンポーネントのラッパーにバインドします。
2. `useState()` フックを使用して、`drag` と `filename` の変数を作成します。それぞれを `false` と `''` に初期化します。
3. `dragCounter` と `drag` の変数は、ファイルがドラッグされているかどうかを判断するために使用されます。一方、`filename` はドロップされたファイルの名前を格納するために使用されます。
4. `handleDrag`、`handleDragIn`、`handleDragOut`、および `handleDrop` のメソッドを作成して、ドラッグアンドドロップ機能を処理します。`handleDrag` は、ドラッグされたファイルをブラウザで開かないように防止します。`handleDragIn` と `handleDragOut` は、ドラッグされたファイルがコンポーネントに入ったり出たりすることを処理します。`handleDrop` は、ファイルがドロップされることを処理し、それを `onDrop` に渡します。
5. `useEffect()` フックを使用して、先に作成したメソッドを使ってそれぞれのドラッグアンドドロップイベントを処理します。

ここにコンポーネント用の CSS です。

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

ここにコンポーネント用の JSX です。

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

コンポーネントを使用するには、`ReactDOM.createRoot(document.getElementById('root')).render(<FileDrop onDrop={console.log} />);` と呼び出します。

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新して、ウェブページをプレビューできます。
