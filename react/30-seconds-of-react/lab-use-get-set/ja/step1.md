# React useGetSet フック

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

このコード スニペットは、状態付きの値を作成し、その値を取得および設定するための一対の関数を返す、`useGetSet` と呼ばれるカスタム React フックを定義しています。`Counter` コンポーネントは、このフックを使用して、ボタンに表示されるカウントの遅延インクリメントを実装しています。

```jsx
const useGetSet = (initialState) => {
  const stateRef = React.useRef(initialState);
  const [, update] = React.useReducer(() => ({}), {});

  const getState = React.useCallback(() => stateRef.current, []);
  const setState = React.useCallback((newState) => {
    stateRef.current = newState;
    update();
  }, []);

  return [getState, setState];
};

const Counter = () => {
  const [getCount, setCount] = useGetSet(0);
  const onClick = React.useCallback(() => {
    setTimeout(() => {
      setCount(getCount() + 1);
    }, 1000);
  }, [getCount, setCount]);

  return <button onClick={onClick}>Count: {getCount()}</button>;
};

ReactDOM.createRoot(document.getElementById("root")).render(<Counter />);
```

右下隅の「Go Live」をクリックして、ポート 8080 でウェブ サービスを実行してください。その後、**Web 8080** タブを更新して、ウェブ ページをプレビューできます。
