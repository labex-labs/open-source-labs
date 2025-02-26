# React useForm フック

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加する必要があります。

フォームのフィールドから状態付きの値を作成するには、`useState()` フックを使用してフォーム内の値用の状態変数を作成します。次に、フォームフィールドによってトリガーされる適切なイベントに基づいて状態変数を更新する関数を作成します。

以下はサンプルの実装です：

```jsx
const useForm = (initialValues) => {
  const [values, setValues] = React.useState(initialValues);

  return [
    values,
    (e) => {
      setValues({
        ...values,
        [e.target.name]: e.target.value
      });
    }
  ];
};
```

上記の例では、`useForm()` は初期状態オブジェクトを受け取り、`useState()` を使って状態変数 `values` を作成し、`values` とそれに渡されたイベントに基づいて `values` を更新する関数を含む配列を返します。

次のようにして、フォームコンポーネントで `useForm()` を使用できます：

```jsx
const Form = () => {
  const initialState = { email: "", password: "" };
  const [values, setValues] = useForm(initialState);

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log(values);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input type="email" name="email" onChange={setValues} />
      <input type="password" name="password" onChange={setValues} />
      <button type="submit">Submit</button>
    </form>
  );
};

ReactDOM.createRoot(document.getElementById("root")).render(<Form />);
```

`Form` コンポーネントでは、初期状態オブジェクトを使って `useForm()` を呼び出し、`values` と `setValues()` を含む配列が返されます。`handleSubmit()` 関数は、フォームが送信されたときに `values` オブジェクトをコンソールに出力します。`input` 要素は、`setValues()` 関数を使ってフォームの値を更新するように設定されています。

右下隅の「Go Live」をクリックして 8080 ポートでウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
