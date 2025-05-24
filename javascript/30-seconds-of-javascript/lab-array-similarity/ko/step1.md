# JavaScript 에서 배열 유사성 찾기

코딩 연습을 위해 터미널/SSH 를 열고 `node`를 입력하십시오. 이렇게 하면 두 배열 모두에 나타나는 요소의 배열을 찾는 방법을 이해하는 데 도움이 됩니다. 다음 단계를 따르십시오.

1. `Array.prototype.includes()` 메서드를 사용하여 `values`의 일부가 아닌 값을 결정합니다.
2. `Array.prototype.filter()` 메서드를 사용하여 해당 값을 제거합니다.

다음은 배열 유사성을 찾는 코드입니다.

```js
const similarity = (arr, values) => arr.filter((v) => values.includes(v));
```

다음 명령을 실행하여 이 코드를 테스트할 수 있습니다.

```js
similarity([1, 2, 3], [1, 2, 4]); // [1, 2]
```

그러면 출력으로 `[1, 2]`가 반환됩니다.
