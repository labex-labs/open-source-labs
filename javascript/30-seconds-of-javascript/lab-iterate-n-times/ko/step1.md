# 코드 연습: N 번 반복하기

코딩 연습을 위해 터미널/SSH 를 열고 `node`를 입력하세요. 그런 다음, 다음 함수를 사용하여 콜백을 `n`번 반복합니다.

```js
const times = (n, fn, context = undefined) => {
  let i = 0;
  while (fn.call(context, i) !== false && ++i < n) {}
};
```

이 함수를 사용하려면 `times()`를 호출하고 다음 인수를 전달합니다.

- `n`: 콜백 함수를 반복하려는 횟수
- `fn`: 반복하려는 콜백 함수
- `context` (선택 사항): 콜백 함수에 사용할 컨텍스트 (지정하지 않으면 `undefined` 객체 또는 비 엄격 모드에서 전역 객체를 사용합니다)

다음은 `times()` 함수를 사용하는 예입니다.

```js
var output = "";
times(5, (i) => (output += i));
console.log(output); // 01234
```

이렇게 하면 콜백 함수 `i => (output += i)`를 5 번 반복하고 출력을 `output` 변수에 저장합니다. 그런 다음 출력이 콘솔에 기록되어 `01234`가 표시됩니다.
