# 소개

이 튜토리얼에서는 분류, 회귀 및 이상치 탐지에 사용되는 지도 학습 방법인 서포트 벡터 머신 (SVM) 에 대해 배웁니다. SVM 은 고차원 공간에서 효과적이며, 차원의 수가 샘플의 수보다 클 때도 잘 작동할 수 있습니다.

SVM 의 장점으로는 고차원 공간에서의 효율성, 메모리 효율성, 다양한 커널 함수의 활용성이 있습니다. 그러나 과적합을 피하고 주어진 문제에 적합한 커널과 정규화 항을 선택하는 것이 중요합니다.

이 튜토리얼에서는 다음 주제를 다룰 것입니다.

1. SVM 을 이용한 분류
2. 다중 클래스 분류
3. 점수 및 확률
4. 불균형 문제
5. SVM 을 이용한 회귀
6. 밀도 추정 및 신선도 탐지

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근할 수 있습니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사를 자동화할 수 없습니다.

학습 중 문제가 발생하면 Labby 에 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
이것은 가이드 실험입니다. 학습과 실습을 돕기 위한 단계별 지침을 제공합니다.각 단계를 완료하고 실무 경험을 쌓기 위해 지침을 주의 깊게 따르세요. 과거 데이터에 따르면, 이것은 <span class="text-green-600 dark:text-green-400">초급</span> 레벨의 실험이며 완료율은 <span class="text-green-600 dark:text-green-400">85.71%</span>입니다.
</div>
