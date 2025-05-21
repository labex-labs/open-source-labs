# 소문자 변환 함수 만들기

이제 객체 키에 접근하고 `reduce()` 메서드를 사용하는 방법을 이해했으므로, 객체의 모든 키를 소문자로 변환하는 함수를 만들어 보겠습니다.

Node.js 대화형 셸에서 다음 함수를 정의합니다.

```javascript
const lowerizeKeys = (obj) => {
  return Object.keys(obj).reduce((acc, key) => {
    acc[key.toLowerCase()] = obj[key];
    return acc;
  }, {});
};
```

이 함수가 수행하는 작업을 자세히 살펴보겠습니다.

1. `Object.keys(obj)`는 입력 객체의 모든 키를 가져옵니다.
2. `.reduce()`는 이러한 키를 새로운 객체로 변환합니다.
3. 각 키에 대해, 누산기 객체 (`acc`) 에 다음을 사용하여 새로운 항목을 만듭니다.
   - `key.toLowerCase()`를 사용하여 소문자로 변환된 키
   - 입력 객체 (`obj[key]`) 의 원래 값
4. 누산기의 초기 값으로 빈 객체 `{}`로 시작합니다.
5. 마지막으로, 소문자 키가 있는 새로운 객체인 누산기를 반환합니다.

이제 앞에서 만든 `user` 객체로 함수를 테스트해 보겠습니다.

```javascript
const lowercaseUser = lowerizeKeys(user);
lowercaseUser;
```

다음과 같은 출력을 볼 수 있습니다.

```
{ name: 'John', age: 30, email: 'john@example.com' }
```

완벽합니다! 이제 모든 키가 소문자로 되어 있습니다.

함수가 제대로 작동하는지 확인하기 위해 다른 예제를 시도해 보겠습니다.

```javascript
const product = {
  ProductID: 101,
  ProductName: "Laptop",
  PRICE: 999.99
};

lowerizeKeys(product);
```

출력은 다음과 같아야 합니다.

```
{ productid: 101, productname: 'Laptop', price: 999.99 }
```

함수는 다양한 키 대소문자 스타일을 가진 다른 객체에 대해 올바르게 작동합니다.
