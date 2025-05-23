# JavaScript 에서 배열 꼬리 (Tail) 얻는 방법

배열의 첫 번째 요소를 제외한 모든 요소를 얻으려면 `Array.prototype.slice()` 메서드를 사용할 수 있습니다. 배열 길이가 1 보다 크면 `slice(1)`을 사용하여 첫 번째 요소가 없는 배열을 반환합니다. 그렇지 않으면 전체 배열을 반환합니다.

JavaScript 에서 음수 슬라이싱 (예: `slice(-4)`) 이 가능하고 끝에서부터 슬라이싱하지만, 여기서는 `slice(1)`을 사용합니다. 그 이유는 다음과 같습니다.

1. 첫 번째 요소를 건너뛰려는 의도를 명확하게 전달합니다.
2. 배열 길이에 관계없이 일관되게 작동합니다.
3. 음수 슬라이싱을 사용하려면 동일한 결과를 얻기 위해 배열 길이를 알아야 합니다.

다음은 예제 코드입니다.

```js
const tail = (arr) => (arr.length > 1 ? arr.slice(1) : arr);
```

이제 `tail()` 함수를 사용하여 배열 꼬리를 얻을 수 있습니다.

```js
tail([1, 2, 3]); // [2, 3]
tail([1]); // [1]
```
