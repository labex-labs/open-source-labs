# JSON 객체에서 중첩된 값 가져오는 방법

주어진 키를 기반으로 중첩된 JSON 객체에서 대상 값을 검색하려면 다음 단계를 따르세요.

- 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
- `in` 연산자를 사용하여 `obj`에 `target`이 존재하는지 확인합니다.
- `target`이 발견되면 `obj`에서 해당 값을 반환합니다.
- `target`이 발견되지 않으면 `Object.values()`와 `Array.prototype.reduce()`를 사용하여 첫 번째 일치하는 키/값 쌍이 발견될 때까지 각 중첩 객체에 대해 `dig` 함수를 재귀적으로 호출합니다.

다음은 `dig` 함수의 코드입니다.

```js
const dig = (obj, target) =>
  target in obj
    ? obj[target]
    : Object.values(obj).reduce((acc, val) => {
        if (acc !== undefined) return acc;
        if (typeof val === "object") return dig(val, target);
      }, undefined);
```

`dig` 함수를 사용하려면 먼저 다음과 같이 중첩된 레벨이 있는 JSON 객체를 생성합니다.

```js
const data = {
  level1: {
    level2: {
      level3: "some data"
    }
  }
};
```

그런 다음 JSON 객체와 원하는 키를 사용하여 `dig` 함수를 호출합니다.

```js
dig(data, "level3"); // 'some data'
dig(data, "level4"); // undefined
```

이 예제는 `data` 객체에서 `level3` 키의 값을 반환하고 존재하지 않는 `level4` 키에 대해 `undefined`를 반환합니다.
