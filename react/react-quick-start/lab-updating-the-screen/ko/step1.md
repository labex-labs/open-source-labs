# 화면 업데이트

> React 프로젝트는 이미 VM 에 제공되어 있습니다. 일반적으로 `App.js`에 코드를 추가하기만 하면 됩니다.

의존성을 설치하려면 다음 명령을 사용하십시오.

```bash
npm i
```

종종 컴포넌트가 정보를 "기억"하고 표시하도록 할 것입니다. 예를 들어, 버튼이 클릭된 횟수를 세고 싶을 수 있습니다. 이를 위해 컴포넌트에 상태 (state) 를 추가합니다.

먼저 React 에서 `useState`를 가져옵니다.

```js
import { useState } from "react";
```

이제 컴포넌트 내에서 상태 변수를 선언할 수 있습니다.

```js
function MyButton() {
  const [count, setCount] = useState(0);
  // ...
```

`useState`에서 두 가지를 얻게 됩니다. 현재 상태 (`count`) 와 상태를 업데이트할 수 있는 함수 (`setCount`) 입니다. 원하는 이름을 지정할 수 있지만, 관례적으로 `[something, setSomething]`으로 작성합니다.

버튼이 처음 표시될 때 `count`는 `0`이 됩니다. 왜냐하면 `useState()`에 0 을 전달했기 때문입니다. 상태를 변경하려면 `setCount()`를 호출하고 새 값을 전달합니다. 이 버튼을 클릭하면 카운터가 증가합니다.

```js
function MyButton() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return <button onClick={handleClick}>Clicked {count} times</button>;
}
```

React 는 컴포넌트 함수를 다시 호출합니다. 이번에는 `count`가 `1`이 됩니다. 그 다음에는 `2`가 됩니다. 이런 식으로 계속됩니다.

동일한 컴포넌트를 여러 번 렌더링하면 각 컴포넌트는 자체 상태를 갖게 됩니다. 각 버튼을 개별적으로 클릭하십시오.

```js
// App.js
import { useState } from "react";

export default function MyApp() {
  return (
    <div>
      <h1>Counters that update separately</h1>
      <MyButton />
      <MyButton />
    </div>
  );
}

function MyButton() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return <button onClick={handleClick}>Clicked {count} times</button>;
}
```

각 버튼이 자체 `count` 상태를 "기억"하고 다른 버튼에 영향을 미치지 않는 것을 확인하십시오.

프로젝트를 실행하려면 다음 명령을 사용하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.

```bash
npm start
```
