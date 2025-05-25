# 이벤트에 반응하기

> React 프로젝트는 이미 VM 에 제공되어 있습니다. 일반적으로 `App.js`에 코드를 추가하기만 하면 됩니다.

다음 명령을 사용하여 종속성을 설치하십시오.

```bash
npm i
```

React 를 사용하면 JSX 에 이벤트 핸들러를 추가할 수 있습니다. 이벤트 핸들러는 클릭, 마우스 오버, 폼 입력 포커스 등과 같은 상호 작용에 대한 응답으로 트리거될 사용자 정의 함수입니다.

이벤트 핸들러를 추가하려면 먼저 함수를 정의한 다음 [해당 함수를 prop 으로 전달](https://react.dev/learn/passing-props-to-a-component)하여 적절한 JSX 태그에 전달합니다. 예를 들어, 아직 아무것도 하지 않는 버튼이 있습니다.

```js
// App.js
export default function Button() {
  return <button>I don't do anything</button>;
}
```

다음 세 단계를 따르면 사용자가 클릭할 때 메시지를 표시하도록 할 수 있습니다.

1. `Button` 컴포넌트 내부에 `handleClick`이라는 함수를 선언합니다.
2. 해당 함수 내부에 로직을 구현합니다 (메시지를 표시하기 위해 `alert`를 사용합니다).
3. `<button>` JSX 에 `onClick={handleClick}`를 추가합니다.

```js
export default function Button() {
  function handleClick() {
    alert("You clicked me!");
  }

  return <button onClick={handleClick}>Click me</button>;
}
```

`handleClick` 함수를 정의한 다음 `<button>`에 prop 으로 전달했습니다. `handleClick`은 이벤트 핸들러입니다. 이벤트 핸들러 함수는 다음과 같습니다.

- 일반적으로 컴포넌트 내부에 정의됩니다.
- `handle`로 시작하고 이벤트 이름이 뒤따르는 이름을 갖습니다.

프로젝트를 실행하려면 다음 명령을 사용하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.

```bash
npm start
```

관례적으로 이벤트 핸들러의 이름을 `handle` 다음에 이벤트 이름을 붙여서 지정합니다. `onClick={handleClick}`, `onMouseEnter={handleMouseEnter}` 등과 같은 형식을 자주 볼 수 있습니다.

또는 JSX 에서 인라인으로 이벤트 핸들러를 정의할 수 있습니다.

```js
<button onClick={function handleClick() {
  alert('You clicked me!');
}}>
```

또는 화살표 함수를 사용하여 더 간결하게 표현할 수 있습니다.

```js
<button onClick={() => {
  alert('You clicked me!');
}}>
```

이러한 모든 스타일은 동일합니다. 인라인 이벤트 핸들러는 짧은 함수에 편리합니다.
