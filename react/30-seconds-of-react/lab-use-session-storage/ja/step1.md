# React useSessionStorage フック

> VM 内には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

`sessionStorage` に永続化される状態付きの値とそれを更新する関数を作成するには、次の手順に従います。

1. `useState()` フックを使用して、その値を遅延初期化する関数を指定します。
2. `try...catch` ブロックと `Storage.getItem()` を使用して、`Window.sessionStorage` から値を取得しようとします。値が見つからない場合は、`Storage.setItem()` を使用して `defaultValue` を保存し、初期状態として使用します。エラーが発生した場合は、`defaultValue` を初期状態として使用します。
3. 渡された値で状態変数を更新する関数を定義し、`Storage.setItem()` を使用して保存します。

以下は、実装例です。

```jsx
const useSessionStorage = (keyName, defaultValue) => {
  const [storedValue, setStoredValue] = React.useState(() => {
    try {
      const value = window.sessionStorage.getItem(keyName);

      if (value) {
        return JSON.parse(value);
      } else {
        window.sessionStorage.setItem(keyName, JSON.stringify(defaultValue));
        return defaultValue;
      }
    } catch (err) {
      return defaultValue;
    }
  });

  const setValue = (newValue) => {
    try {
      window.sessionStorage.setItem(keyName, JSON.stringify(newValue));
    } catch (err) {}
    setStoredValue(newValue);
  };

  return [storedValue, setValue];
};
```

このフックをアプリケーションで使用するには、次のようにします。

```jsx
const MyApp = () => {
  const [name, setName] = useSessionStorage("name", "John");

  return <input value={name} onChange={(e) => setName(e.target.value)} />;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
