# 소개

이 랩에서는 JavaScript 에서 얕은 복사 (shallow cloning) 의 개념을 탐구합니다. 얕은 복사는 원본 객체의 모든 속성을 가진 새로운 객체를 생성하지만, 속성 자체는 복사되지 않습니다. 대신, 참조로 복사되므로 원본 객체의 속성에 변경 사항이 생기면 복사된 객체에도 반영됩니다. 이 랩을 통해 JavaScript 에서 `Object.assign()` 메서드를 사용하여 객체의 얕은 복사본을 만드는 방법을 이해할 것입니다.

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
이것은 가이드 실험입니다. 학습과 실습을 돕기 위한 단계별 지침을 제공합니다.각 단계를 완료하고 실무 경험을 쌓기 위해 지침을 주의 깊게 따르세요. 과거 데이터에 따르면, 이것은 <span class="text-green-600 dark:text-green-400">초급</span> 레벨의 실험이며 완료율은 <span class="text-green-600 dark:text-green-400">100%</span>입니다.
</div>
