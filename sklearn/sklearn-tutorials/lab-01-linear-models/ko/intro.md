# 소개

이 실습에서는 scikit-learn 의 선형 모델을 탐색합니다. 선형 모델은 회귀 및 분류 작업에 사용되는 방법 집합입니다. 이 모델들은 목표 변수가 특징의 선형 결합이라고 가정합니다. 이러한 모델은 단순성과 해석 가능성으로 인해 머신 러닝에서 널리 사용됩니다.

다음 주제를 다룰 것입니다:

- 최소 제곱법
- 릿지 회귀
- 라쏘
- 로지스틱 회귀
- 확률적 경사 하강법
- 퍼셉트론

머신 러닝에 대한 사전 경험이 없으시면 [지도 학습: 회귀](https://labex.io/courses/supervised-learning-regression)를 참고하세요.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접근합니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사를 자동화할 수 없습니다.

학습 중 문제가 발생하면 Labby 에게 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
이것은 가이드 실험입니다. 학습과 실습을 돕기 위한 단계별 지침을 제공합니다.각 단계를 완료하고 실무 경험을 쌓기 위해 지침을 주의 깊게 따르세요. 과거 데이터에 따르면, 이것은 <span class="text-orange-600 dark:text-orange-400">중급</span> 레벨의 실험이며 완료율은 <span class="text-orange-600 dark:text-orange-400">57.85%</span>입니다.학습자들로부터 <span class="text-primary-600 dark:text-primary-400">94%</span>의 긍정적인 리뷰율을 받았습니다.
</div>
