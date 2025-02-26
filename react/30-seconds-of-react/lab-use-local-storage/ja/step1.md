# React useLocalStorage フック

> VM には既に `index.html` と `script.js` が提供されています。一般的には、`script.js` と `style.css` にのみコードを追加する必要があります。

この関数は、`localStorage` に保存される値とそれを変更する関数を作成します。その動作方法は以下の通りです。

1. 値を作成するには、遅延初期化用の関数と共に `useState()` フックを使用します。
2. `localStorage` から保存された値を取得するには、`try...catch` ブロックと `Storage.getItem()` を使用します。保存された値がない場合は、`Storage.setItem()` を使用して `defaultValue` を保存し、初期状態として使用します。エラーが発生した場合は、`defaultValue` を使用します。
3. 渡された値で状態変数を更新し、`Storage.setItem()` を使用して保存する関数を定義します。

以下がコードです。

```jsx
const useLocalStorage = (keyName, defaultValue) => {
  const [storedValue, setStoredValue] = React.useState(() => {
    try {
      const value = window.localStorage.getItem(keyName);

      if (value) {
        return JSON.parse(value);
      } else {
        window.localStorage.setItem(keyName, JSON.stringify(defaultValue));
        return defaultValue;
      }
    } catch (err) {
      return defaultValue;
    }
  });

  const setValue = (newValue) => {
    try {
      window.localStorage.setItem(keyName, JSON.stringify(newValue));
    } catch (err) {}
    setStoredValue(newValue);
  };

  return [storedValue, setValue];
};
```

この関数をアプリケーションで使用する方法は以下の通りです。

```jsx
const MyApp = () => {
  const [name, setName] = useLocalStorage("name", "John");

  return <input value={name} onChange={(e) => setName(e.target.value)} />;
};

ReactDOM.createRoot(document.getElementById("root")).render(<MyApp />);
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
