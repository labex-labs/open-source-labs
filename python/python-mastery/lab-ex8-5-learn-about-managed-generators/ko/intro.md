# 소개

이 랩에서는 관리형 제너레이터에 대해 배우고, 이를 특이한 방식으로 구동하는 방법을 이해하게 됩니다. 또한 간단한 작업 스케줄러를 구축하고 제너레이터를 사용하여 네트워크 서버를 만들 것입니다.

Python 의 제너레이터 함수는 실행을 위해 외부 코드가 필요합니다. 예를 들어, 반복 제너레이터는 `for` 루프로 반복될 때만 실행되며, 코루틴은 `send()` 메서드를 호출해야 합니다. 이 랩에서는 고급 애플리케이션에서 제너레이터를 구동하는 실용적인 예제를 살펴봅니다. 이 랩에서 생성되는 파일은 `multitask.py`와 `server.py`입니다.

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
이것은 가이드 실험입니다. 학습과 실습을 돕기 위한 단계별 지침을 제공합니다.각 단계를 완료하고 실무 경험을 쌓기 위해 지침을 주의 깊게 따르세요. 과거 데이터에 따르면, 이것은 <span class="text-green-600 dark:text-green-400">초급</span> 레벨의 실험이며 완료율은 <span class="text-green-600 dark:text-green-400">84%</span>입니다.학습자들로부터 <span class="text-primary-600 dark:text-primary-400">80%</span>의 긍정적인 리뷰율을 받았습니다.
</div>
