# Concorrência Extensível com as Traits Send e Sync

Curiosamente, a linguagem Rust possui _muito_ poucas funcionalidades de concorrência. Quase todas as funcionalidades de concorrência sobre as quais falamos até agora neste capítulo fazem parte da biblioteca padrão, e não da linguagem. Suas opções para lidar com concorrência não se limitam à linguagem ou à biblioteca padrão; você pode escrever suas próprias funcionalidades de concorrência ou usar aquelas escritas por outros.

No entanto, dois conceitos de concorrência estão embutidos na linguagem: as traits `std::marker` `Send` e `Sync`.
