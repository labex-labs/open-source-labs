# 스타일 추가하기

React 에서는 `className`으로 CSS 클래스를 지정합니다. HTML [class](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/class) 속성과 동일하게 작동합니다.

```html
<img className="avatar" />
```

그런 다음 별도의 CSS 파일에 대한 CSS 규칙을 작성합니다.

```css
/* App.css */
.avatar {
  border-radius: 50%;
}
```

React 는 CSS 파일을 추가하는 방법을 규정하지 않습니다. 가장 간단한 경우 HTML 에 `<link>` 태그를 추가합니다. 빌드 도구 또는 프레임워크를 사용하는 경우, 프로젝트에 CSS 파일을 추가하는 방법을 배우려면 해당 설명서를 참조하십시오.

```js
// App.js
import "./App.css";
```

JSX 중괄호 안에 더 복잡한 표현식을 넣을 수도 있습니다. 예를 들어, [문자열 연결](https://javascript.info/operators#string-concatenation-with-binary)과 같습니다.

```js
// App.js
const user = {
  name: "Hedy Lamarr",
  imageUrl: "https://i.imgur.com/yXOvdOSs.jpg",
  imageSize: 90
};

export default function Profile() {
  return (
    <>
      <h1>{user.name}</h1>
      <img
        className="avatar"
        src={user.imageUrl}
        alt={"Photo of " + user.name}
        style={{
          width: user.imageSize,
          height: user.imageSize
        }}
      />
    </>
  );
}
```

위의 예에서 `style={{}}`은 특별한 구문이 아니라 `style={ }` JSX 중괄호 안에 있는 일반적인 `{}` 객체입니다. 스타일이 JavaScript 변수에 의존하는 경우 `style` 속성을 사용할 수 있습니다.
