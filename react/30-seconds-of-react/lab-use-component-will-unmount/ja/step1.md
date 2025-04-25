# React の useComponentWillUnmount フック

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

コンポーネントがアンマウントされ破棄される直前にコールバックを実行するには、2 番目の引数として空の配列を持つ `useEffect()` フックを使うことができます。クリーンアップ前に一度だけ実行されるように提供されたコールバックを返します。この動作は、クラスコンポーネントの `componentWillUnmount()` ライフサイクルメソッドに似ています。また、以下のコードスニペットを使って、`onUnmountHandler` 関数を引数として取り、コンポーネントがアンマウントされる前にそれを実行するカスタムフック `useComponentWillUnmount()` を作成することもできます。

```jsx
const useComponentWillUnmount = (onUnmountHandler) => {
  React.useEffect(
    () => () => {
      onUnmountHandler();
    },
    []
  );
};
```

その後、このカスタムフックを関数型コンポーネントで次のように使うことができます。

```jsx
const Unmounter = () => {
  useComponentWillUnmount(() => console.log("Component will unmount"));

  return <div>Check the console!</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Unmounter />);
```

これにより、コンポーネントがアンマウントされる直前にコンソールに "Component will unmount" が表示されます。

右下隅の「Go Live」をクリックして、ポート 8080 でウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
