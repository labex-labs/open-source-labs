# 키 배열을 사용하여 객체 내 중첩된 값 검색 방법

중첩된 JSON 객체에서 특정 값을 검색하려면 `deepGet` 함수를 사용할 수 있습니다. 이 함수는 객체와 키 배열을 입력으로 받아 객체에 대상 값이 있으면 해당 값을 반환합니다.

`deepGet` 함수를 사용하려면:

- 중첩된 JSON 객체에서 검색하려는 키의 배열을 생성합니다.
- 객체와 키 배열을 사용하여 `deepGet` 함수를 호출합니다.
- 함수는 대상 값이 있으면 해당 값을 반환하고, 없으면 `null`을 반환합니다.

다음은 `deepGet` 함수의 코드입니다:

```js
const deepGet = (obj, keys) =>
  keys.reduce(
    (xs, x) => (xs && xs[x] !== null && xs[x] !== undefined ? xs[x] : null),
    obj
  );
```

다음은 `deepGet` 함수를 사용하는 예시입니다:

```js
let index = 2;
const data = {
  foo: {
    foz: [1, 2, 3],
    bar: {
      baz: ["a", "b", "c"]
    }
  }
};
deepGet(data, ["foo", "foz", index]); // returns 3
deepGet(data, ["foo", "bar", "baz", 8, "foz"]); // returns null
```

코딩 연습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.
