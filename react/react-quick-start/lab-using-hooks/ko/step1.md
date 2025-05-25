# 훅 (Hooks) 사용하기

> React 프로젝트는 이미 VM 에 제공되어 있습니다. 일반적으로 `App.js`에 코드를 추가하기만 하면 됩니다.

다음 명령을 사용하여 종속성을 설치하십시오.

```bash
npm i
```

use 로 시작하는 함수는 훅 (Hooks) 이라고 합니다. useState 는 React 에서 제공하는 내장 훅입니다. API 참조에서 다른 내장 훅을 찾을 수 있습니다. 기존 훅을 결합하여 자신만의 훅을 작성할 수도 있습니다.

훅은 다른 함수보다 더 제한적입니다. 훅은 컴포넌트 (또는 다른 훅) 의 최상위에서만 호출할 수 있습니다. 조건문이나 반복문에서 useState 를 사용하려면 새로운 컴포넌트를 추출하여 그 안에 넣으십시오.

이전 예제에서 각 `MyButton`은 자체적인 독립적인 `count`를 가지고 있었고, 각 버튼을 클릭하면 클릭된 버튼의 `count`만 변경되었습니다.

![Not using hooks](../assets/1.png)

그러나 종종 컴포넌트가 데이터를 공유하고 항상 함께 업데이트해야 할 필요가 있습니다.

두 MyButton 컴포넌트가 동일한 count 를 표시하고 함께 업데이트되도록 하려면 상태를 개별 버튼에서 모든 버튼을 포함하는 가장 가까운 컴포넌트 "위로" 이동해야 합니다.

이 예제에서는 MyApp 입니다.

![Using hooks](../assets/2.png)

이제 버튼을 클릭하면 `MyApp`의 `count`가 변경되어 `MyButton`의 두 count 가 모두 변경됩니다. 코드로 이를 표현하는 방법은 다음과 같습니다.

먼저, 상태를 `MyButton`에서 `MyApp`으로 이동합니다.

```js
// App.js
export default function MyApp() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <div>
      <h1>Counters that update separately</h1>
      <MyButton />
      <MyButton />
    </div>
  );
}

function MyButton() {
  // ... we're moving code from here ...
}
```

그런 다음, 공유된 클릭 핸들러와 함께 상태를 `MyApp`에서 각 `MyButton`으로 전달합니다. `<img>`와 같은 내장 태그에서 이전에 했던 것처럼 JSX 중괄호를 사용하여 정보를 `MyButton`으로 전달할 수 있습니다.

```js
export default function MyApp() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <div>
      <h1>Counters that update together</h1>
      <MyButton count={count} onClick={handleClick} />
      <MyButton count={count} onClick={handleClick} />
    </div>
  );
}
```

이처럼 전달하는 정보를 props 라고 합니다. 이제 `MyApp` 컴포넌트는 `count` 상태와 `handleClick` 이벤트 핸들러를 포함하고 있으며, 둘 다 props 로 각 버튼에 전달합니다.

마지막으로, `MyButton`을 변경하여 상위 컴포넌트에서 전달한 props 를 읽습니다.

```js
function MyButton({ count, onClick }) {
  return <button onClick={onClick}>Clicked {count} times</button>;
}
```

버튼을 클릭하면 `onClick` 핸들러가 실행됩니다. 각 버튼의 `onClick` prop 은 `MyApp` 내부의 `handleClick` 함수로 설정되었으므로 해당 내부의 코드가 실행됩니다. 해당 코드는 `setCount(count + 1)`을 호출하여 `count` 상태 변수를 증가시킵니다. 새로운 `count` 값은 각 버튼에 prop 으로 전달되므로 모두 새로운 값을 표시합니다. 이를 "상태 끌어올리기 (lifting state up)"라고 합니다. 상태를 위로 이동함으로써 컴포넌트 간에 공유했습니다.

```js
import { useState } from "react";

export default function MyApp() {
  const [count, setCount] = useState(0);

  function handleClick() {
    setCount(count + 1);
  }

  return (
    <div>
      <h1>Counters that update together</h1>
      <MyButton count={count} onClick={handleClick} />
      <MyButton count={count} onClick={handleClick} />
    </div>
  );
}

function MyButton({ count, onClick }) {
  return <button onClick={onClick}>Clicked {count} times</button>;
}
```

프로젝트를 실행하려면 다음 명령을 사용하십시오. 그런 다음, **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.

```bash
npm start
```
