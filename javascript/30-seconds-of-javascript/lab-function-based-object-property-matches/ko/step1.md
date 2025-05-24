# 함수를 사용하여 객체 속성 일치시키기

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.

이 함수는 두 객체를 비교하고 첫 번째 객체가 두 번째 객체와 동일한 속성 값을 포함하는지 확인합니다. 제공된 함수를 기반으로 이를 수행합니다.

이 함수를 사용하려면 다음 단계를 따르십시오.

- `Object.keys()`를 사용하여 두 번째 객체의 모든 키를 검색합니다.
- `Array.prototype.every()`, `Object.prototype.hasOwnProperty()`, 그리고 제공된 함수를 사용하여 모든 키가 첫 번째 객체에 존재하고 동일한 값을 갖는지 확인합니다.
- 함수가 제공되지 않으면 동등 연산자를 사용하여 값을 비교합니다.

```js
const matchesWith = (obj, source, fn) =>
  Object.keys(source).every((key) =>
    obj.hasOwnProperty(key) && fn
      ? fn(obj[key], source[key], key, obj, source)
      : obj[key] == source[key]
  );
```

이 함수를 사용하는 방법의 예는 다음과 같습니다.

```js
const isGreeting = (val) => /^h(?:i|ello)$/.test(val);
matchesWith(
  { greeting: "hello" },
  { greeting: "hi" },
  (oV, sV) => isGreeting(oV) && isGreeting(sV)
); // true
```

이 예제는 두 객체가 `greeting` 속성에 대해 동일한 값을 갖는지 확인합니다. `isGreeting` 함수를 사용하여 두 값이 모두 유효한 인사말인지 확인합니다.
