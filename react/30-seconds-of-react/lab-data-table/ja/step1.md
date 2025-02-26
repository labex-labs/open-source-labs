# データテーブル

> VM には既に `index.html` と `script.js` が用意されています。一般的には、`script.js` と `style.css` にのみコードを追加すればよいです。

`ID` と `Value` の 2 つの列を持つテーブル要素を作成し、各行をプリミティブ値の配列から動的に生成します。

これを達成するには、`Array.prototype.map()` メソッドを使って、入力 `data` 配列の各項目を適切な `key` 付きの `<tr>` 要素として表す新しい JSX 要素の配列を作成します。各 `<tr>` 内に、行のインデックスと値をそれぞれ表示する 2 つの `<td>` 要素を追加します。

以下は例となる実装です：

```jsx
const DataTable = ({ data }) => {
  return (
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>Value</th>
        </tr>
      </thead>
      <tbody>
        {data.map((val, i) => (
          <tr key={`${i}_${val}`}>
            <td>{i}</td>
            <td>{val}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};
```

たとえば、人の名前の配列でこのコンポーネントを使う場合、次のように呼び出すことができます：

```jsx
const people = ["John", "Jesse"];
ReactDOM.createRoot(document.getElementById("root")).render(
  <DataTable data={people} />
);
```

右下隅の「Go Live」をクリックして 8080 ポートでウェブサービスを実行してください。その後、**Web 8080** タブを更新してウェブページをプレビューできます。
