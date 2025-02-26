# データ リスト

> VM には既に `index.html` と `script.js` が提供されています。一般的には、`script.js` と `style.css` にのみコードを追加する必要があります。

この関数は、プリミティブ値の配列から項目のリストをレンダリングします。`isOrdered` プロップの値に基づいて、順序付きまたは無順序のリストを条件付きでレンダリングするために使用できます。`data` 配列の各項目をレンダリングするには、`Array.prototype.map()` を使用して、各項目に固有の `key` を持つ `<li>` 要素を作成します。

```jsx
const DataList = ({ data, isOrdered = false }) => {
  const list = data.map((value, index) => (
    <li key={`${index}_${value}`}>{value}</li>
  ));

  return isOrdered ? <ol>{list}</ol> : <ul>{list}</ul>;
};
```

このコンポーネントを使用する方法の例を以下に示します。

```jsx
const names = ["John", "Paul", "Mary"];
ReactDOM.createRoot(document.getElementById("root")).render(
  <>
    <DataList data={names} />
    <DataList data={names} isOrdered={true} />
  </>
);
```

この例では、名前の配列を `DataList` コンポーネントに渡して 2 回レンダリングしています。1 回目は無順序のリストをレンダリングし、2 回目は順序付きのリストをレンダリングしています。

右下隅の「Go Live」をクリックして、ポート 8080 でウェブ サービスを実行してください。その後、**Web 8080** タブを更新してウェブ ページをプレビューできます。
