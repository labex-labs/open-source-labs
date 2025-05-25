# 컴포넌트 생성 및 중첩

> React 프로젝트는 이미 VM 에 제공되어 있습니다. 일반적으로 `App.js`에 코드를 추가하기만 하면 됩니다.

다음 명령을 사용하여 종속성을 설치하십시오:

```bash
npm i
```

React 앱은 컴포넌트 (component) 로 구성됩니다. 컴포넌트는 자체 로직과 모양을 가진 UI(사용자 인터페이스) 의 일부입니다. 컴포넌트는 버튼만큼 작거나 전체 페이지만큼 클 수 있습니다.

React 컴포넌트는 마크업 (markup) 을 반환하는 JavaScript 함수입니다:

```js
// App.js
function MyButton() {
  return <button>I'm a button</button>;
}
```

`MyButton`을 선언했으므로 다른 컴포넌트에 중첩할 수 있습니다:

```js
// App.js
export default function MyApp() {
  return (
    <div>
      <h1>Welcome to my app</h1>
      <MyButton />
    </div>
  );
}
```

`<MyButton />`이 대문자로 시작하는 것을 확인하십시오. 이것이 React 컴포넌트임을 알 수 있는 방법입니다. React 컴포넌트 이름은 항상 대문자로 시작해야 하는 반면, HTML 태그는 소문자여야 합니다.

`export default` 키워드는 파일의 메인 컴포넌트를 지정합니다. JavaScript 구문 중 일부에 익숙하지 않은 경우, [MDN](https://developer.mozilla.org/en-US/docs/web/javascript/reference/statements/export) 및 [javascript.info](https://javascript.info/import-export)에서 훌륭한 참고 자료를 제공합니다.

프로젝트를 실행하려면 다음 명령을 사용하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.

```bash
npm start
```
