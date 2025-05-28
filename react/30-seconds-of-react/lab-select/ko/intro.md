# 소개

이 랩에서는 콜백 함수를 사용하여 React 에서 제어되지 않는 `<select>` 요소를 생성하고, 해당 값을 부모 컴포넌트로 전달하는 방법을 배우겠습니다. `<select>` 요소의 초기 값을 설정하기 위해 `selectedValue` prop 을 사용하고, 새로운 값을 부모에게 보내기 위해 `onChange` 이벤트를 사용할 것입니다. 또한, 이 랩에서는 전달된 각 값에 대한 `<option>` 요소를 생성하기 위해 `Array.prototype.map()`을 사용하는 방법도 다룹니다.

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
이것은 가이드 실험입니다. 학습과 실습을 돕기 위한 단계별 지침을 제공합니다.각 단계를 완료하고 실무 경험을 쌓기 위해 지침을 주의 깊게 따르세요. 과거 데이터에 따르면, 이것은 <span class="text-green-600 dark:text-green-400">초급</span> 레벨의 실험이며 완료율은 <span class="text-green-600 dark:text-green-400">100%</span>입니다.
</div>
