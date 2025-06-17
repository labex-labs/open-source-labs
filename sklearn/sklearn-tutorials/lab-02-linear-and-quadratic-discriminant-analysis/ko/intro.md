# 소개

선형 판별 분석 (LDA) 과 2 차 판별 분석 (QDA) 은 머신 러닝에서 사용되는 두 가지 고전적인 분류기입니다. LDA 는 선형 결정 경계를 사용하는 반면, QDA 는 2 차 결정 경계를 사용합니다. 이러한 분류기는 닫힌 형태의 해를 가지고 실제로 잘 작동하며, 조정할 하이퍼파라미터가 없다는 점에서 인기가 많습니다.

이 실습에서는 파이썬의 인기 머신 러닝 라이브러리인 scikit-learn 을 사용하여 LDA 와 QDA 를 수행하는 방법을 살펴볼 것입니다.

## 가상 머신 팁

가상 머신 시작이 완료되면 왼쪽 상단 모서리를 클릭하여 **Notebook** 탭으로 전환하여 [Jupyter Notebook](https://support.labex.io/en/labex-vm/jupyter)을 연습에 사용할 수 있습니다.

때때로 Jupyter Notebook 이 완전히 로드되기까지 몇 초 정도 기다려야 할 수 있습니다. Jupyter Notebook 의 제한으로 인해 작업의 유효성 검사를 자동화할 수 없습니다.

학습 중 문제가 발생하면 Labby 에게 문의하십시오. 세션 후 피드백을 제공하면 문제를 신속하게 해결해 드리겠습니다.

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
이것은 가이드 실험입니다. 학습과 실습을 돕기 위한 단계별 지침을 제공합니다.각 단계를 완료하고 실무 경험을 쌓기 위해 지침을 주의 깊게 따르세요. 과거 데이터에 따르면, 이것은 <span class="text-orange-600 dark:text-orange-400">중급</span> 레벨의 실험이며 완료율은 <span class="text-orange-600 dark:text-orange-400">80%</span>입니다.학습자들로부터 <span class="text-primary-600 dark:text-primary-400">95%</span>의 긍정적인 리뷰율을 받았습니다.
</div>
