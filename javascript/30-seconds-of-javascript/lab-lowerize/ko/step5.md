# 재사용 가능한 모듈 만들기

이제 작동하는 함수가 있으므로, 다른 프로젝트로 가져올 수 있는 재사용 가능한 JavaScript 모듈 파일을 만들어 보겠습니다.

먼저, Ctrl+C 를 두 번 누르거나 `.exit`를 입력하고 Enter 키를 눌러 Node.js 대화형 셸을 종료합니다.

이제 프로젝트 디렉토리에 `object-utils.js`라는 새 파일을 만듭니다.

1. WebIDE 에서 왼쪽의 파일 탐색기 패널로 이동합니다.
2. 프로젝트 디렉토리에서 마우스 오른쪽 버튼을 클릭하고 "New File"을 선택합니다.
3. 파일 이름을 `object-utils.js`로 지정합니다.
4. 파일에 다음 코드를 추가합니다.

```javascript
/**
 * Converts all keys of an object to lowercase
 * @param {Object} obj - The input object
 * @returns {Object} A new object with all keys in lowercase
 */
const lowerizeKeys = (obj) => {
  return Object.keys(obj).reduce((acc, key) => {
    acc[key.toLowerCase()] = obj[key];
    return acc;
  }, {});
};

/**
 * Recursively converts all keys of an object and its nested objects to lowercase
 * @param {Object} obj - The input object
 * @returns {Object} A new object with all keys in lowercase (including nested objects)
 */
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

// Export the functions
module.exports = {
  lowerizeKeys,
  deepLowerizeKeys
};
```

이제 모듈이 제대로 작동하는지 확인하기 위해 테스트 파일을 만들어 보겠습니다. `test.js`라는 새 파일을 만듭니다.

1. WebIDE 에서 왼쪽의 파일 탐색기 패널로 이동합니다.
2. 프로젝트 디렉토리에서 마우스 오른쪽 버튼을 클릭하고 "New File"을 선택합니다.
3. 파일 이름을 `test.js`로 지정합니다.
4. 파일에 다음 코드를 추가합니다.

```javascript
// Import the functions from our module
const { lowerizeKeys, deepLowerizeKeys } = require("./object-utils");

// Test with a simple object
const user = {
  Name: "John",
  AGE: 30,
  Email: "john@example.com"
};

console.log("Original object:");
console.log(user);

console.log("\nObject with lowercase keys:");
console.log(lowerizeKeys(user));

// Test with a nested object
const nestedObject = {
  User: {
    Name: "John",
    Contact: {
      EMAIL: "john@example.com",
      PHONE: "123-456-7890"
    }
  }
};

console.log("\nNested object:");
console.log(nestedObject);

console.log("\nNested object with lowercase keys (shallow):");
console.log(lowerizeKeys(nestedObject));

console.log("\nNested object with lowercase keys (deep):");
console.log(deepLowerizeKeys(nestedObject));
```

이제 테스트 파일을 실행해 보겠습니다.

```bash
node test.js
```

다음과 유사한 출력을 볼 수 있습니다.

```
Original object:
{ Name: 'John', AGE: 30, Email: 'john@example.com' }

Object with lowercase keys:
{ name: 'John', age: 30, email: 'john@example.com' }

Nested object:
{
  User: {
    Name: 'John',
    Contact: { EMAIL: 'john@example.com', PHONE: '123-456-7890' }
  }
}

Nested object with lowercase keys (shallow):
{
  user: {
    Name: 'John',
    Contact: { EMAIL: 'john@example.com', PHONE: '123-456-7890' }
  }
}

Nested object with lowercase keys (deep):
{
  user: {
    name: 'John',
    contact: { email: 'john@example.com', phone: '123-456-7890' }
  }
}
```

축하합니다! 객체 키를 소문자로 변환하는 함수가 있는 재사용 가능한 JavaScript 모듈을 성공적으로 만들었습니다. 이 모듈은 이제 JavaScript 프로젝트에 가져올 수 있습니다.
