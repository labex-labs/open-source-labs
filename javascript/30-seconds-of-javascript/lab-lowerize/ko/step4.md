# 엣지 케이스 처리

우리의 함수는 간단한 객체에 대해서는 잘 작동하지만, 더 복잡한 경우에는 어떨까요? 몇 가지 엣지 케이스를 살펴보고 함수가 어떻게 처리하는지 살펴보겠습니다.

## 빈 객체

먼저, 빈 객체로 테스트해 보겠습니다.

```javascript
lowerizeKeys({});
```

출력은 빈 객체여야 합니다.

```
{}
```

## 중첩된 객체가 있는 객체

객체에 중첩된 객체가 포함되어 있다면 어떨까요? 시도해 보겠습니다.

```javascript
const nestedObject = {
  User: {
    Name: "John",
    Contact: {
      EMAIL: "john@example.com",
      PHONE: "123-456-7890"
    }
  }
};

lowerizeKeys(nestedObject);
```

출력은 다음과 같습니다.

```
{ user: { Name: 'John', Contact: { EMAIL: 'john@example.com', PHONE: '123-456-7890' } } }
```

최상위 키 `User`만 소문자로 변환된 것을 확인하세요. 중첩된 객체 내부의 키는 변경되지 않습니다.

중첩된 객체를 처리하려면, 모든 객체를 재귀적으로 처리하도록 함수를 수정해야 합니다. 향상된 버전을 만들어 보겠습니다.

```javascript
const deepLowerizeKeys = (obj) => {
  return Object.keys(obj).reduce((acc, key) => {
    const value = obj[key];
    // Check if the value is an object and not null
    const newValue =
      value && typeof value === "object" && !Array.isArray(value)
        ? deepLowerizeKeys(value)
        : value;

    acc[key.toLowerCase()] = newValue;
    return acc;
  }, {});
};
```

이 향상된 함수는 다음을 수행합니다.

1. 각 값이 객체인지 확인합니다 (배열 또는 null 이 아닌지 확인).
2. 객체인 경우, 해당 중첩된 객체에 대해 자체적으로 재귀적으로 호출합니다.
3. 그렇지 않은 경우, 원래 값을 사용합니다.

중첩된 객체로 테스트해 보겠습니다.

```javascript
const deepLowerizedObject = deepLowerizeKeys(nestedObject);
deepLowerizedObject;
```

이제 중첩된 객체에서도 모든 키가 소문자로 변환된 것을 볼 수 있습니다.

```
{ user: { name: 'John', contact: { email: 'john@example.com', phone: '123-456-7890' } } }
```

잘하셨습니다! 중첩된 객체를 처리할 수 있는 고급 함수를 만들었습니다.
