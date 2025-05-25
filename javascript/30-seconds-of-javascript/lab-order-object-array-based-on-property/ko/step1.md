# 속성 순서를 기반으로 객체 배열 정렬하는 방법

속성 순서를 기반으로 객체 배열을 정렬하려면 다음 단계를 따르세요.

1. 터미널/SSH 를 열고 `node`를 입력하여 코딩 연습을 시작합니다.
2. `Array.prototype.reduce()`를 사용하여 `order` 배열에서 값을 키로, 원래 인덱스를 값으로 하는 객체를 생성합니다.
3. `Array.prototype.sort()`를 사용하여 주어진 배열을 정렬하고, `prop`이 비어 있거나 `order` 배열에 없는 요소는 건너뜁니다.

다음은 속성 순서를 기반으로 객체 배열을 정렬하는 예시 코드 조각입니다.

```js
const orderWith = (arr, prop, order) => {
  const orderValues = order.reduce((acc, v, i) => {
    acc[v] = i;
    return acc;
  }, {});
  return [...arr].sort((a, b) => {
    if (orderValues[a[prop]] === undefined) return 1;
    if (orderValues[b[prop]] === undefined) return -1;
    return orderValues[a[prop]] - orderValues[b[prop]];
  });
};
```

`orderWith` 함수를 사용하여 속성 순서를 기반으로 객체 배열을 정렬할 수 있습니다. 예를 들어:

```js
const users = [
  { name: "fred", language: "Javascript" },
  { name: "barney", language: "TypeScript" },
  { name: "frannie", language: "Javascript" },
  { name: "anna", language: "Java" },
  { name: "jimmy" },
  { name: "nicky", language: "Python" }
];
orderWith(users, "language", ["Javascript", "TypeScript", "Java"]);
/*
[
  { name: 'fred', language: 'Javascript' },
  { name: 'frannie', language: 'Javascript' },
  { name: 'barney', language: 'TypeScript' },
  { name: 'anna', language: 'Java' },
  { name: 'jimmy' },
  { name: 'nicky', language: 'Python' }
]
*/
```
