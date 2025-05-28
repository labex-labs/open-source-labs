# 소개

지도 학습 (supervised learning) 에서는 관측 데이터 `X`와 예측하고자 하는 외부 변수 `y` 사이의 관계를 학습하려고 합니다.
지도 학습 문제는 크게 분류 (classification) 와 회귀 (regression) 의 두 가지 유형으로 나뉩니다. 분류에서는 관측치의 클래스 또는 카테고리를 예측하는 것을 목표로 하고, 회귀에서는 연속적인 목표 변수를 예측하는 것을 목표로 합니다.

이 실습에서는 지도 학습의 개념을 탐구하고, 파이썬의 인기 머신러닝 라이브러리인 scikit-learn 을 사용하여 이를 구현하는 방법을 살펴볼 것입니다. 최근접 이웃 분류, 선형 회귀, 서포트 벡터 머신 (SVMs) 과 같은 주제를 다룰 것입니다.

## VM 팁

VM 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 연습을 위한 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)에 접속합니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제약으로 인해 작업의 유효성 검사를 자동화할 수 없습니다.

학습 중 문제가 발생하면 Labby 에 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
이것은 가이드 실험입니다. 학습과 실습을 돕기 위한 단계별 지침을 제공합니다.각 단계를 완료하고 실무 경험을 쌓기 위해 지침을 주의 깊게 따르세요. 과거 데이터에 따르면, 이것은 <span class="text-green-600 dark:text-green-400">초급</span> 레벨의 실험이며 완료율은 <span class="text-green-600 dark:text-green-400">100%</span>입니다.
</div>
