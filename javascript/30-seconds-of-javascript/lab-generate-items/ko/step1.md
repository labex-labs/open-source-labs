# 코드 실습

코딩 실습을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오. 그런 다음 `generateItems` 함수를 사용하여 특정 수의 항목이 있는 배열을 생성할 수 있습니다.

- 원하는 항목 수와 항목을 생성하는 데 사용될 함수를 사용하여 `generateItems`를 호출합니다.
- `generateItems`는 `Array.from()`을 사용하여 지정된 길이의 빈 배열을 생성하고, 새로 생성된 각 요소의 인덱스를 사용하여 제공된 함수를 호출합니다.
- 제공된 함수는 하나의 인수를 받습니다. 각 요소의 인덱스입니다.

```js
const generateItems = (n, fn) => Array.from({ length: n }, (_, i) => fn(i));
```

다음은 `generateItems`를 사용하여 10 개의 난수 배열을 생성하는 예입니다.

```js
generateItems(10, Math.random);
// [0.21, 0.08, 0.40, 0.96, 0.96, 0.24, 0.19, 0.96, 0.42, 0.70]
```
