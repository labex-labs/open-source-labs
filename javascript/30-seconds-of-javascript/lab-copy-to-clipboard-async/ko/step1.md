# 문자열을 클립보드에 복사하는 함수

문자열을 클립보드에 복사하려면 `copyToClipboardAsync` 함수를 사용합니다. 이 함수는 클립보드의 내용이 업데이트되면 resolve 되는 promise 를 반환합니다. 다음은 단계별 설명입니다.

1. `if` 문을 사용하여 `Navigator`, `Navigator.clipboard`, 그리고 `Navigator.clipboard.writeText`가 truthy 인지 확인하여 Clipboard API 의 가용성을 확인합니다.
2. Clipboard API 를 사용할 수 있는 경우, `Clipboard.writeText()`를 사용하여 주어진 값인 `str`을 클립보드에 씁니다.
3. 클립보드의 내용이 업데이트되면 resolve 되는 promise 인 `Clipboard.writeText()`의 결과를 반환합니다.
4. Clipboard API 를 사용할 수 없는 경우, `Promise.reject()`를 사용하여 적절한 오류 메시지와 함께 promise 를 reject 합니다.
5. 이전 브라우저를 지원해야 하는 경우, `Clipboard.writeText()` 대신 `Document.execCommand()`를 사용합니다. 이에 대한 자세한 내용은 `copyToClipboard` 코드 조각에서 확인할 수 있습니다.

다음은 `copyToClipboardAsync` 함수입니다.

```js
const copyToClipboardAsync = (str) => {
  if (navigator && navigator.clipboard && navigator.clipboard.writeText) {
    return navigator.clipboard.writeText(str);
  }
  return Promise.reject("The Clipboard API is not available.");
};
```

이 함수를 사용하려면, 복사하려는 문자열을 인수로 사용하여 `copyToClipboardAsync`를 호출합니다. 예시:

```js
copyToClipboardAsync("Lorem ipsum"); // 'Lorem ipsum' copied to clipboard.
```
