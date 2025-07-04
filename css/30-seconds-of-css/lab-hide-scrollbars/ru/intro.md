# Введение

В этом практическом занятии мы изучим концепцию скрытия полос прокрутки на элементе, при этом позволяя ему по-прежнему быть прокручиваемым с использованием CSS. Мы будем использовать свойство `overflow: auto` для включения прокрутки и `scrollbar-width: none` для скрытия полос прокрутки в Firefox, а также `display: none` на псевдо-элементе `::-webkit-scrollbar` для скрытия полос прокрутки в браузерах на основе WebKit. Это практическое занятие даст опыт в реализации этой CSS-техники для улучшения пользовательского опыта при работе с прокручиваемыми элементами.

<div class="text-xs text-gray-500 dark:text-gray-400 mt-4 border-t border-l-2 border-gray-300 dark:border-gray-600 pt-2 pl-4">
Это Guided Lab, который предоставляет пошаговые инструкции, чтобы помочь вам учиться и практиковаться. Внимательно следуйте инструкциям, чтобы выполнить каждый шаг и получить практический опыт. Исторические данные показывают, что это лабораторная работа уровня <span class="text-green-600 dark:text-green-400">начальный</span> с процентом завершения <span class="text-green-600 dark:text-green-400">100%</span>. Он получил <span class="text-primary-600 dark:text-primary-400">100%</span> положительных отзывов от учащихся.
</div>
