# React useKeyPress フック

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

この関数は、特定のキーの押下状態の変化を監視します。これを使用するには：

- 対象のキーを引数として `useKeyPress()` を呼び出します。
- `useKeyPress()` は、現在キーが押されているかどうかを示すブール値を返します。
- この関数は `useState()` フックを使用して、特定のキーの押下状態を保持する状態変数を作成します。
- キーが押されたときまたは離されたときに状態変数を更新する 2 つのハンドラ関数を定義します。
- `useEffect()` フックと `EventTarget.addEventListener()` を使用して、`'keydown'` と `'keyup'` イベントを処理します。
- 最後に、`EventTarget.removeEventListener()` を使用して、コンポーネントがアンマウントされた後のクリーンアップ処理を行います。

```jsx
const useKeyPress = (targetKey) => {
  const [isKeyPressed, setKeyPressed] = React.useState(false);

  const handleKeyDown = ({ key }) => {
    if (key === targetKey) setKeyPressed(true);
  };

  const handleKeyUp = ({ key }) => {
    if (key === targetKey) setKeyPressed(false);
  };

  React.useEffect(() => {
    window.addEventListener("keydown", handleKeyDown);
    window.addEventListener("keyup", handleKeyUp);

    return () => {
      window.removeEventListener("keydown", handleKeyDown);
      window.removeEventListener("keyup", handleKeyUp);
    };
  }, [targetKey]);

  return isKeyPressed;
};
```

ここでは、React コンポーネントでの `useKeyPress()` の使用例を示します：

```jsx
const MyApp = () => {
  const isWKeyPressed = useKeyPress("w");

  return <p>The "w" key is {!isWKeyPressed ? "not " : ""}pressed!</p>;
};

ReactDOM.render(<MyApp />, document.getElementById("root"));
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
