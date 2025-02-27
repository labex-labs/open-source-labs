# Exponieren von Pfaden mit dem Schlüsselwort pub

Lassen Sie uns zurückkehren zum Fehler in Listing 7-4, der uns mitgeteilt hat, dass das Modul `hosting` privat ist. Wir möchten, dass die `eat_at_restaurant`-Funktion im übergeordneten Modul auf die `add_to_waitlist`-Funktion im Untermodul zugreifen kann, daher markieren wir das Modul `hosting` mit dem Schlüsselwort `pub`, wie in Listing 7-5 gezeigt.

Dateiname: `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        fn add_to_waitlist() {}
    }
}

--snip--
```

Listing 7-5: Deklarieren des Moduls `hosting` als `pub`, um es aus `eat_at_restaurant` zu verwenden

Leider führt der Code in Listing 7-5 immer noch zu Compilerfehlern, wie in Listing 7-6 gezeigt.

```bash
$ cargo build
   Compiling restaurant v0.1.0 (file:///projects/restaurant)
error[E0603]: Funktion `add_to_waitlist` ist privat
 --> src/lib.rs:9:37
  |
9 |     crate::front_of_house::hosting::add_to_waitlist();
  |                                     ^^^^^^^^^^^^^^^ private Funktion
  |
note: Die Funktion `add_to_waitlist` ist hier definiert
 --> src/lib.rs:3:9
  |
3 |         fn add_to_waitlist() {}
  |         ^^^^^^^^^^^^^^^^^^^^

error[E0603]: Funktion `add_to_waitlist` ist privat
  --> src/lib.rs:12:30
   |
12 |     front_of_house::hosting::add_to_waitlist();
   |                              ^^^^^^^^^^^^^^^ private Funktion
   |
note: Die Funktion `add_to_waitlist` ist hier definiert
  --> src/lib.rs:3:9
   |
3  |         fn add_to_waitlist() {}
   |         ^^^^^^^^^^^^^^^^^^^^
```

Listing 7-6: Compilerfehler beim Erstellen des Codes in Listing 7-5

Was ist passiert? Das Hinzufügen des Schlüsselworts `pub` vor `mod hosting` macht das Modul öffentlich. Mit dieser Änderung können wir, wenn wir auf `front_of_house` zugreifen können, auch auf `hosting` zugreifen. Aber der _Inhalt_ von `hosting` ist immer noch privat; das Machen des Moduls öffentlich macht seine Inhalte nicht öffentlich. Das `pub`-Schlüsselwort auf einem Modul lässt nur Code in seinen Vorfahrenmodulen auf es verweisen, nicht auf seinen inneren Code zuzugreifen. Da Module Container sind, können wir mit nur dem Machen des Moduls öffentlich nicht viel tun; wir müssen noch weiter gehen und eine oder mehrere der Elemente innerhalb des Moduls ebenfalls öffentlich machen.

Die Fehler in Listing 7-6 sagen, dass die `add_to_waitlist`-Funktion privat ist. Die Privatsphäre-Regeln gelten für Structs, Enums, Funktionen und Methoden sowie für Module.

Lassen Sie uns auch die `add_to_waitlist`-Funktion öffentlich machen, indem wir das Schlüsselwort `pub` vor ihrer Definition hinzufügen, wie in Listing 7-7.

Dateiname: `src/lib.rs`

```rust
mod front_of_house {
    pub mod hosting {
        pub fn add_to_waitlist() {}
    }
}

--snip--
```

Listing 7-7: Hinzufügen des Schlüsselworts `pub` zu `mod hosting` und `fn add_to_waitlist` ermöglicht uns, die Funktion aus `eat_at_restaurant` aufzurufen.

Jetzt wird der Code kompilieren! Um zu verstehen, warum das Hinzufügen des Schlüsselworts `pub` uns ermöglicht, diese Pfade in `add_to_waitlist` in Bezug auf die Privatsphäre-Regeln zu verwenden, betrachten wir die absoluten und die relativen Pfade.

Im absoluten Pfad beginnen wir mit `crate`, der Wurzel unseres Kastenmodultrees. Das Modul `front_of_house` ist in der Kistenwurzel definiert. Obwohl `front_of_house` nicht öffentlich ist, können wir, da die `eat_at_restaurant`-Funktion in demselben Modul wie `front_of_house` definiert ist (d.h., `eat_at_restaurant` und `front_of_house` sind Geschwister), von `eat_at_restaurant` auf `front_of_house` verweisen. Als nächstes ist das Modul `hosting` mit `pub` markiert. Wir können auf das übergeordnete Modul von `hosting` zugreifen, daher können wir auf `hosting` zugreifen. Schließlich ist die `add_to_waitlist`-Funktion mit `pub` markiert und wir können auf ihr übergeordnetes Modul zugreifen, daher funktioniert dieser Funktionsaufruf!

Im relativen Pfad ist die Logik dasselbe wie im absoluten Pfad, mit Ausnahme des ersten Schritts: Anstatt von der Kistenwurzel aus zu beginnen, beginnt der Pfad von `front_of_house`. Das Modul `front_of_house` ist innerhalb desselben Moduls wie `eat_at_restaurant` definiert, daher funktioniert der relative Pfad, der von dem Modul ausgeht, in dem `eat_at_restaurant` definiert ist. Dann, da `hosting` und `add_to_waitlist` mit `pub` markiert sind, funktioniert der restliche Pfad und dieser Funktionsaufruf ist gültig!

Wenn Sie vorhaben, Ihre Bibliothekskiste zu teilen, so dass andere Projekte Ihren Code verwenden können, ist Ihre öffentliche API Ihr Vertrag mit den Benutzern Ihrer Kiste, der bestimmt, wie sie mit Ihrem Code interagieren können. Es gibt viele Überlegungen bei der Verwaltung von Änderungen an Ihrer öffentlichen API, um es Menschen einfacher zu machen, von Ihrer Kiste abzuhängen. Diese Überlegungen liegen außerhalb des Rahmens dieses Buches; wenn Sie an diesem Thema interessiert sind, finden Sie die Rust API Guidelines unter *https://rust-lang.github.io/api-guidelines*.

> **Best Practices für Pakete mit einem Binärprogramm und einer Bibliothek**
>
> Wir haben erwähnt, dass ein Paket sowohl eine Binärkistenwurzel `src/main.rs` als auch eine Bibliothekskistenwurzel `src/lib.rs` enthalten kann, und beide Kisten werden standardmäßig den Paketnamen haben. Typischerweise werden Pakete mit diesem Muster, das sowohl eine Bibliothek als auch ein Binärpaket enthält, nur so viel Code im Binärpaket haben, um ein ausführbares Programm zu starten, das Code mit der Bibliothekskiste aufruft. Dadurch können andere Projekte von der meiste Funktionalität profitieren, die das Paket bietet, da der Code der Bibliothekskiste geteilt werden kann.
>
> Der Modultree sollte in `src/lib.rs` definiert werden. Dann können alle öffentlichen Elemente im Binärpaket verwendet werden, indem Pfade mit dem Namen des Pakets begonnen werden. Das Binärpaket wird zu einem Benutzer der Bibliothekskiste, genauso wie ein völlig externes Paket die Bibliothekskiste verwenden würde: Es kann nur die öffentliche API verwenden. Dies hilft Ihnen, eine gute API zu entwerfen; nicht nur sind Sie der Autor, Sie sind auch ein Client!
>
> Im Kapitel 12 werden wir diese Organisationspraxis mit einem Befehlszeilenprogramm demonstrieren, das sowohl ein Binärpaket als auch eine Bibliothekskiste enthalten wird.
