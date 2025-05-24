# JavaScript 에서 Frozen Set 객체 생성하기

JavaScript 에서 frozen `Set` 객체를 생성하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Set` 생성자를 사용하여 `iterable`에서 새로운 `Set` 객체를 생성합니다.
3. 새로 생성된 객체의 `add`, `delete`, 그리고 `clear` 메서드를 `undefined`로 설정하여 객체를 효과적으로 고정합니다.

다음은 예시 코드 조각입니다.

```js
const frozenSet = (iterable) => {
  const s = new Set(iterable);
  s.add = undefined;
  s.delete = undefined;
  s.clear = undefined;
  return s;
};

console.log(frozenSet([1, 2, 3, 1, 2]));
// Output: Set { 1, 2, 3, add: undefined, delete: undefined, clear: undefined }
```

이 코드는 숫자 iterable 에서 frozen `Set` 객체를 생성하고, `add`, `delete`, 그리고 `clear` 메서드가 `undefined`로 설정된 객체를 반환합니다.
