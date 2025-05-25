# 객체가 특정 값을 포함하는지 확인하는 함수

객체가 특정 값을 포함하는지 확인하려면 다음 함수를 사용하십시오.

```js
const hasValue = (obj, value) => Object.values(obj).includes(value);
```

이 함수를 사용하려면 검색하려는 객체와 대상 값을 인수로 전달합니다. 객체가 값을 포함하면 함수는 `true`를 반환하고, 그렇지 않으면 `false`를 반환합니다.

다음은 예시입니다.

```js
const obj = { a: 100, b: 200 };
console.log(hasValue(obj, 100)); // true
console.log(hasValue(obj, 999)); // false
```

코딩을 시작하려면 터미널/SSH 를 열고 `node`를 입력하십시오.
