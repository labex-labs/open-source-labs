# 매핑된 배열 교집합 찾기 지침

두 배열의 각 요소에 함수를 적용한 후 공통 요소를 찾으려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력합니다.
2. 아래 제공된 코드를 사용합니다.

```js
const intersectionBy = (a, b, fn) => {
  const s = new Set(b.map(fn));
  return [...new Set(a)].filter((x) => s.has(fn(x)));
};
```

3. 코드에서 `a`와 `b`를 배열로, `fn`을 각 요소에 적용하려는 함수로 바꿉니다.
4. 코드를 실행하여 공통 요소가 있는 결과 배열을 얻습니다.

예시:

```js
intersectionBy([2.1, 1.2], [2.3, 3.4], Math.floor); // [2.1]
intersectionBy(
  [{ title: "Apple" }, { title: "Orange" }],
  [{ title: "Orange" }, { title: "Melon" }],
  (x) => x.title
); // [{ title: 'Orange' }]
```

첫 번째 예시에서는 함수 `Math.floor`가 배열 `[2.1, 1.2]`와 `[2.3, 3.4]`에 적용되어 공통 요소 `[2.1]`을 반환합니다.
두 번째 예시에서는 함수 `x => x.title`이 배열 `[{ title: 'Apple' }, { title: 'Orange' }]`와 `[{ title: 'Orange' }, { title: 'Melon' }]`에 적용되어 공통 요소 `[{ title: 'Orange' }]`을 반환합니다.
