# 데이터 표시

JSX 를 사용하면 마크업을 JavaScript 에 넣을 수 있습니다. 중괄호를 사용하면 JavaScript 로 "다시 탈출"하여 코드에서 일부 변수를 포함하고 사용자에게 표시할 수 있습니다. 예를 들어, 이것은 `user.name`을 표시합니다.

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

JSX 속성에서도 JavaScript 로 "탈출"할 수 있지만, 따옴표 대신 중괄호를 사용해야 합니다. 예를 들어, `className="avatar"`는 `"avatar"` 문자열을 CSS 클래스로 전달하지만, `src={user.imageUrl}`은 JavaScript `user.imageUrl` 변수 값을 읽은 다음 해당 값을 `src` 속성으로 전달합니다.

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
