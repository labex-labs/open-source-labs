# データの表示

JSX を使うと、マークアップを JavaScript に埋め込むことができます。波括弧を使うと、JavaScript に戻ることができるので、コード内の変数を埋め込んでユーザーに表示することができます。たとえば、これは `user.name` を表示します。

```js
// App.js
const user = {
  name: "Hedy Lamarr"
};
export default function Profile() {
  return (
    <>
      <h1>{user.name}</h1>
    </>
  );
}
```

また、JSX 属性からも JavaScript に「脱出」できますが、クォートの代わりに波括弧を使う必要があります。たとえば、`className="avatar"` は CSS クラスとして `"avatar"` 文字列を渡しますが、`src={user.imageUrl}` は JavaScript の `user.imageUrl` 変数の値を読み取り、その値を `src` 属性として渡します。

```js
// App.js
const user = {
  name: "Hedy Lamarr",
  imageUrl: "https://i.imgur.com/yXOvdOSs.jpg"
};
export default function Profile() {
  return (
    <>
      <h1>{user.name}</h1>
      <img className="avatar" src={user.imageUrl} />
    </>
  );
}
```
