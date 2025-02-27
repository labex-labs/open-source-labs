# Cargo als Konvention

Bei einfachen Projekten bietet Cargo nicht viel mehr Wert als die reine Verwendung von `rustc`, aber seine Wertigkeit wird sich bei zunehmender Komplexität Ihrer Programme beweisen. Sobald Programme auf mehrere Dateien anwachsen oder Abhängigkeiten benötigen, ist es einfacher, Cargo zu verwenden, um den Build zu koordinieren.

Auch wenn das `hello_cargo`-Projekt einfach ist, verwendet es jetzt viel von den wirklichen Werkzeugen, die Sie in der restlichen Zeit Ihres Rust-Careers verwenden werden. Tatsächlich können Sie für jedes vorhandene Projekt die folgenden Befehle verwenden, um den Code mit Git herunterzuladen, in das Projektverzeichnis zu wechseln und zu bauen:

```bash
git clone example.org/someproject
cd someproject
cargo build
```

Weitere Informationen zu Cargo finden Sie in der Dokumentation unter *https://doc.rust-lang.org/cargo*.
