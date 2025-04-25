# React の usePersistedState フック

> VM 内には既に`index.html`と`script.js`が用意されています。一般的には、`script.js`と`style.css`にのみコードを追加すればよいです。

このフックは、`localStorage`に永続化された状態付きの値と、それを更新するために使用できる関数を返します。これを使用するには、次の手順に従います。

1. `useState()`フックを使用して、`value`を`defaultValue`に初期化します。
2. `useRef()`フックを使用して、`Window.localStorage`内の値の`name`を保持する ref を作成します。
3. それぞれ初期化、`value`の変更、および`name`の変更に対して、`useEffect()`フックのインスタンスを 3 つ使用します。
4. コンポーネントが最初にマウントされたとき、保存された値があれば`Storage.getItem()`を使用して`value`を更新し、そうでなければ`Storage.setItem()`を使用して現在の値を永続化します。
5. `value`が更新されたとき、`Storage.setItem()`を使用して新しい値を保存します。
6. `name`が更新されたとき、`Storage.setItem()`を使用して新しいキーを作成し、`nameRef`を更新し、`Storage.removeItem()`を使用して`Window.localStorage`から以前のキーを削除します。
7. このフックは、プリミティブ値（つまりオブジェクトではない値）に対して使用することを想定しており、他のコードによる`Window.localStorage`の変更には対応していません。これらの問題はどちらも簡単に対処できます（たとえば、JSON シリアル化と`'storage'`イベントの処理）。

以下はコードです。

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

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080**タブを更新してウェブページをプレビューできます。
