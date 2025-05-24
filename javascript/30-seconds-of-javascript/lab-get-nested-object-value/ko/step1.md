# 경로 문자열에서 중첩된 객체 속성을 검색하는 방법

코딩 연습을 하려면 터미널/SSH 를 열고 `node`를 입력하세요.

다음 함수는 경로 문자열에 지정된 선택자를 사용하여 객체에서 일련의 속성을 검색합니다. 이를 위해 다음 단계를 따르세요.

1. `Array.prototype.map()`을 사용하여 각 선택자를 반복하고 `String.prototype.replace()`를 적용하여 대괄호를 점으로 바꿉니다.
2. `String.prototype.split()`을 사용하여 각 선택자를 문자열 배열로 분할합니다.
3. `Array.prototype.filter()`를 사용하여 빈 값을 제거합니다.
4. `Array.prototype.reduce()`를 사용하여 각 선택자가 나타내는 값을 검색합니다.

다음은 함수입니다.

```js
const get = (from, ...selectors) =>
  [...selectors].map((s) =>
    s
      .replace(/\[([^\[\]]*)\]/g, ".$1.")
      .split(".")
      .filter((t) => t !== "")
      .reduce((prev, cur) => prev && prev[cur], from)
  );
```

이 함수를 사용하여 경로 문자열을 사용하여 중첩된 객체에서 값을 검색할 수 있습니다. 다음은 예시입니다.

```js
const obj = {
  selector: { to: { val: "val to select" } },
  target: [1, 2, { a: "test" }]
};
get(obj, "selector.to.val", "target[0]", "target[2].a");
// ['val to select', 1, 'test']
```
