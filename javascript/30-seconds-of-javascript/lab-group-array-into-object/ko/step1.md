# 배열을 객체로 그룹화하는 방법

배열을 객체로 그룹화하려면 다음 단계를 따르세요.

1. 터미널 또는 SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.reduce()` 메서드를 사용하여 두 배열로부터 객체를 생성합니다.
3. 유효한 프로퍼티 식별자 배열과 값 배열을 제공합니다.
4. 프로퍼티 배열의 길이가 값 배열보다 길면, 나머지 키는 `undefined`로 설정됩니다.
5. 값 배열의 길이가 프로퍼티 배열보다 길면, 나머지 값은 무시됩니다.

다음은 배열을 객체로 그룹화하는 방법을 보여주는 코드 예제입니다.

```js
const zipObject = (props, values) =>
  props.reduce((obj, prop, index) => ((obj[prop] = values[index]), obj), {});

zipObject(["a", "b", "c"], [1, 2]); // {a: 1, b: 2, c: undefined}
zipObject(["a", "b"], [1, 2, 3]); // {a: 1, b: 2}
```
