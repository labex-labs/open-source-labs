# ReactのuseComponentDidMountフック

> VM内には既に`index.html`と`script.js`が用意されています。一般的には、`script.js`と`style.css`にのみコードを追加すればよいです。

コンポーネントがマウントされた直後にコールバック関数を実行するには、`useEffect()`フックに空の配列を2番目の引数として渡します。これにより、コンポーネントがマウントされたときに提供されたコールバックが1回だけ実行されることが保証されます。以下に示す`useComponentDidMount()`関数は、このフックを使って、クラスコンポーネントの`componentDidMount()`ライフサイクルメソッドと同じ動作を実現しています。

```jsx
const useComponentDidMount = (onMountHandler) => {
  React.useEffect(() => {
    onMountHandler();
  }, []);
};

const Mounter = () => {
  useComponentDidMount(() => console.log("Component did mount"));

  return <div>Check the console!</div>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Mounter />);
```

右下隅の「Go Live」をクリックして、ポート8080でウェブサービスを実行してください。その後、**Web 8080**タブを更新して、ウェブページをプレビューできます。
