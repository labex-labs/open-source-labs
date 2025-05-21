# 각 단어 대문자화

이제 문자열을 단어로 분리할 수 있으므로 각 단어의 첫 글자를 대문자로 만들고 나머지는 소문자로 만들어야 합니다. 이 기능을 구현해 보겠습니다.

1. Node.js 세션에서 단일 단어를 대문자화하는 함수를 작성해 보겠습니다. 다음을 입력합니다.

```javascript
function capitalizeWord(word) {
  return word.charAt(0).toUpperCase() + word.slice(1).toLowerCase();
}

// Test with a few examples
console.log(capitalizeWord("hello"));
console.log(capitalizeWord("WORLD"));
console.log(capitalizeWord("javaScript"));
```

출력 결과는 다음과 같습니다.

```
Hello
World
Javascript
```

2. 이제 `map()` 메서드를 사용하여 이 함수를 단어 배열에 적용해 보겠습니다. 다음을 입력합니다.

```javascript
let words = ["hello", "WORLD", "javaScript"];
let capitalizedWords = words.map((word) => capitalizeWord(word));
console.log(capitalizedWords);
```

출력 결과는 다음과 같습니다.

```
[ 'Hello', 'World', 'Javascript' ]
```

`map()` 메서드는 원래 배열의 각 요소에 함수를 적용하여 새 배열을 생성합니다. 이 경우, `capitalizeWord` 함수를 각 단어에 적용하고 있습니다.

3. 마지막으로, 대문자화된 단어를 함께 연결하여 Pascal case 문자열을 형성해 보겠습니다.

```javascript
let pascalCase = capitalizedWords.join("");
console.log(pascalCase);
```

출력 결과는 다음과 같습니다.

```
HelloWorldJavascript
```

`join("")` 메서드는 제공된 구분 기호 (이 경우 빈 문자열) 를 각 요소 사이에 사용하여 배열의 모든 요소를 단일 문자열로 결합합니다.

이러한 단계는 문자열을 Pascal case 로 변환하는 핵심 프로세스를 보여줍니다.

1. 문자열을 단어로 분리합니다.
2. 각 단어를 대문자화합니다.
3. 구분 기호 없이 단어를 연결합니다.
