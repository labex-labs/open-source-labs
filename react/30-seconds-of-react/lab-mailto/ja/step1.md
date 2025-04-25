# メールリンク

> `index.html` と `script.js` はすでに仮想マシン（VM）に用意されています。一般的には、`script.js` と `style.css` にコードを追加するだけです。

この関数は、クリックするとユーザーのメールクライアントを開き、指定された件名と本文の内容で新しいメールを作成するリンクを作成します。リンクは `mailto:` プロトコルを使用してフォーマットされます。

この関数を使用するには、受信者のメールアドレスを含む `email` プロップを指定し、オプションで `subject` と `body` プロップを指定して、メールに初期内容を設定します。これらのプロップは、リンク URL に追加される前に `encodeURIComponent` を使用して安全にエンコードされます。

リンクは、指定された `children` を内容としてレンダリングされます。

```jsx
const Mailto = ({ email, subject = "", body = "", children }) => {
  const params =
    subject || body
      ? `?subject=${encodeURIComponent(subject)}&body=${encodeURIComponent(
          body
        )}`
      : "";

  return <a href={`mailto:${email}${params}`}>{children}</a>;
};
```

使用例：

```jsx
ReactDOM.createRoot(document.getElementById("root")).render(
  <Mailto email="foo@bar.baz" subject="Hello & Welcome" body="Hello world!">
    Mail me!
  </Mailto>
);
```

右下隅にある「Go Live」をクリックして、ポート 8080 で Web サービスを実行してください。その後、**Web 8080** タブを更新すると、Web ページをプレビューできます。
