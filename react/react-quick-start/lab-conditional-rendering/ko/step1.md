# 조건부 렌더링

> React 프로젝트는 이미 VM 에 제공되어 있습니다. 일반적으로 `App.js`에 코드만 추가하면 됩니다.

다음 명령을 사용하여 종속성을 설치하십시오.

```bash
npm i
```

React 에서는 조건을 작성하기 위한 특별한 구문이 없습니다. 대신, 일반 JavaScript 코드를 작성할 때 사용하는 것과 동일한 기술을 사용합니다. 예를 들어, `if` 문을 사용하여 JSX 를 조건부로 포함할 수 있습니다.

```js
if (isPacked) {
  return <li className="item">{name} ✔</li>;
}
return <li className="item">{name}</li>;
```

더 간결한 코드를 선호하는 경우, 조건부 `?` 연산자를 사용할 수 있습니다. `if`와 달리 JSX 내에서 작동합니다.

```js
return <li className="item">{isPacked ? name + " ✔" : name}</li>;
```

`else` 분기가 필요하지 않은 경우, 더 짧은 논리적 `&&` 구문을 사용할 수도 있습니다.

```js
return <li className="item">{isPacked && name + " ✔"}</li>;
```

`isPacked` prop 이 true 이면 이 코드는 다른 JSX 트리를 반환합니다. 이 변경으로 일부 항목은 끝에 체크 표시를 받습니다.

```js
// App.js
function Item({ name, isPacked }) {
  if (isPacked) {
    return <li className="item">{name} ✔</li>;
  }
  return <li className="item">{name}</li>;
}

export default function PackingList() {
  return (
    <section>
      <h1>Sally Ride's Packing List</h1>
      <ul>
        <Item isPacked={true} name="Space suit" />
        <Item isPacked={true} name="Helmet with a golden leaf" />
        <Item isPacked={false} name="Photo of Tam" />
      </ul>
    </section>
  );
}
```

프로젝트를 실행하려면 다음 명령을 사용하십시오. 그런 다음 **Web 8080** 탭을 새로 고쳐 웹 페이지를 미리 볼 수 있습니다.

```bash
npm start
```
