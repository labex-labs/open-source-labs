# 메모이제이션 함수 (Memoize Function)

코딩을 시작하려면 터미널/SSH 를 열고 `node`를 입력하세요. 이 함수는 메모이제이션된 (캐시된) 함수를 반환합니다. 이 함수를 사용하는 단계는 다음과 같습니다.

1. 빈 캐시를 생성하기 위해 새로운 `Map` 객체를 인스턴스화합니다.
2. 메모이제이션된 함수에 제공될 단일 인수를 받는 함수를 반환합니다. 함수를 실행하기 전에 해당 특정 입력 값에 대한 출력이 이미 캐시되어 있는지 확인합니다. 캐시되어 있다면 캐시된 출력을 반환하고, 그렇지 않으면 저장하고 반환합니다.
3. 필요한 경우 메모이제이션된 함수가 `this` 컨텍스트를 변경할 수 있도록 `function` 키워드를 사용합니다.
4. 반환된 함수에 `cache`를 속성으로 설정하여 접근할 수 있도록 합니다.

다음은 메모이제이션 함수를 구현하는 코드입니다.

```js
const memoize = (fn) => {
  const cache = new Map();
  const cached = function (val) {
    return cache.has(val)
      ? cache.get(val)
      : cache.set(val, fn.call(this, val)) && cache.get(val);
  };
  cached.cache = cache;
  return cached;
};
```

이 함수가 어떻게 작동하는지 확인하려면 `anagrams` 함수와 함께 사용할 수 있습니다. 다음은 예시입니다.

```js
const anagramsCached = memoize(anagrams);
anagramsCached("javascript"); // takes a long time
anagramsCached("javascript"); // returns virtually instantly since it's cached
console.log(anagramsCached.cache); // The cached anagrams map
```
