# React の useError フック

> `index.html` と `script.js` はすでに仮想マシン（VM）に用意されています。一般的には、`script.js` と `style.css` にコードを追加するだけです。

このコードはエラーディスパッチャーを作成します。エラー状態を管理し、それをユーザーインターフェイスにディスパッチするために、3 つの React フックを使用しています。

コードの動作原理は以下の通りです。

1. `useState()` フックは、エラーオブジェクトを保持する `error` という状態変数を作成します。このフックには、引数として渡される `err` を初期値として設定します。

2. `useEffect()` フックは、`error` が真の値を持つ場合にエラーを「スロー」するために使用されます。このフックは関数と依存配列を引数として受け取ります。この場合、関数は `error` 状態変数が真（つまり、null、undefined、0、false、または空文字列ではない）かどうかをチェックし、真の場合はエラーをスローします。依存配列は `[error]` であり、これは `error` 変数が変更されるたびに副作用が再実行されることを意味します。

3. `useCallback()` フックは、`dispatchError` というキャッシュされた関数を作成するために使用されます。この関数は `error` 状態変数を更新し、新しい関数を返します。このフックは関数と依存配列を引数として受け取ります。この場合、関数は引数 `err` を受け取り、これはディスパッチする新しいエラーオブジェクトです。依存配列は `[]` であり、これはコンポーネントが再レンダリングされた場合にのみキャッシュされた関数が再作成されることを意味します。

コンポーネントで `useError()` フックを使用する例を以下に示します。

1. `ErrorButton` という新しいコンポーネントを作成します。

2. コンポーネント内で `useError()` フックを呼び出し、`dispatchError` 関数を取得します。

3. 新しいエラーオブジェクトを引数に `dispatchError` を呼び出す `clickHandler` というクリックハンドラー関数を作成します。

4. クリックされたときに `clickHandler` を呼び出すボタンをレンダリングします。

コードは以下の通りです。

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

右下隅にある「Go Live」をクリックして、ポート 8080 で Web サービスを実行してください。その後、**Web 8080** タブを更新すると、Web ページをプレビューできます。
