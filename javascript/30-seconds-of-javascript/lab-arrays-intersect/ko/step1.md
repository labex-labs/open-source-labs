# 두 배열에 공통 항목이 있는지 확인하는 방법

두 배열에 공통 항목이 있는지 확인하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `b`에서 `Set`을 생성하여 `b`의 고유 값을 얻습니다.
3. `Array.prototype.some()`을 `a`에 사용하여 `Set.prototype.has()`를 통해 해당 값 중 `b`에 포함된 값이 있는지 확인합니다.
4. 아래 제공된 `intersects` 함수를 사용하여 배열을 테스트합니다.

```js
const intersects = (a, b) => {
  const s = new Set(b);
  return [...new Set(a)].some((x) => s.has(x));
};
```

`intersects` 함수를 사용하여 두 배열이 교차하는지 확인합니다.

```js
intersects(["a", "b"], ["b", "c"]); // true
intersects(["a", "b"], ["c", "d"]); // false
```

이 단계를 따르고 제공된 코드를 사용하면 두 배열에 공통 항목이 있는지 쉽게 확인할 수 있습니다.
