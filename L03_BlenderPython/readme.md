# Lektion 03 - Python in Blender

Hier machen wir erste Gehversuche mit Python als Skriptsprache in Blender

## Einführung

Wie viele andere Softwarepakete im Bereich der Medienproduktion lässt sich Blender mit der Programmiersprache Python automatisieren. Blender wird dazu mit einer eigenen Python-Distribution ausgeliefert und installiert (diese liegt im Blender-Installationsverzeichnis in einem eigenen `python` Unterverzeichnis). Obwohl Blender selbst in der Programmiersprache C++ geschrieben wurde, ist der gesamte Source-Code eng mit Python verzahnt. Nahezu jede Funktionalität, die sich in Blender über das User Interface auslösen lässt, kann auch mit Python-Befehlen aus einem Skript aufgerufen werden. Darüber hinaus sind sämtliche Daten innerhalb von Blender über Python-Strukturen zugreifbar. Dazu zählen u.a. 
- Szenen und Objekte
- Geometrie
- Kamera und Beleuchtung
- Materialien
- Texturen


## Erste Schritte

### Die interaktive Konsole

Für allererste Schritte in Python innerhalb von Blender eignet sich die in Blender als eigener Editor eingebaute Python Konsole. Mit dieser kann wie mit dem `python`-Befehl von der Kommandozeile des Betriebssystems interaktiv Python-Code Zeile für Zeile eingegeben werden.

#### TODO

> - Startet Blender -> Die Standard-Szene mit einem Würfel erscheint
> - Falls nicht geschehen: Selektiert den Würfel.
> - Wechselt den Editor am unteren Rand vom _Timeline_ Editor in den _Python Console_ Editor, in dem ihr im Editor Header ganz unten links auf das Icon klickt.
> - Gebt folgenden Befehl in der interaktiven Blender-Python-Console ein:
>   ```
>   >>> bpy.ops.transform.translate(value=(0, 2, 0))
>   ```
> - Ergebnis: Der Würfel wird um zwei Einheiten entlang der Y-Achse verschoben (transliert).

Was fällt uns hier ins Auge?:

- Alles, was Blender für das Skripten zur Verfügung stellt, ist über das Python-_Modul_ `bpy` abrufbar. Unterhalb von `bpy` gibt es eine weitere hierarchische Aufteilung, so dass Blender-Kommandos in Python folgende Struktur haben:
  ```
  bpy.abc.def.[...].command()
  ```
  Das Kommando ```bpy.ops.transform.translate()``` verwendet aus der Gesamtheit aller Blender-Python-Funktionalität (```bpy```) die Untergruppe der Operationen (```ops```), dort wird dann aus der Untergruppe der Transformations-Operationen (```transform```) die Methode ```translate``` aufgerufen.

- Funktionen (Methoden), die Parameter entgegen nehmen, verwenden meist _named_ Paramter. Im Beispiel oben muss daher der Verschiebungsvektor, der an die Methode ```translate``` übergeben wird, mit ```value=...``` explizit benannt werden. Bislang haben wir bei Python-Methoden die aus anderen Programmiersprachen bekannten _positional_ Parameter kennen gelernt, bei denen die Position in der Parameterliste eindeutig bestimmt, welcher Parameter gemeint ist.

- Vektoren werden in  einer 3D-Anwendung an allen möglichen Stellen verwendet. So auch in Blender, z.B. für die Angaben von Verschiebungen, Positionen, Normalen, Euler-Winkel, Textur-Koordinaten usw.. Diese können in Blender Python als _Tupel_ (Siehe Lektion 2 - Datentypen) angegeben werden. 



## Das Blender-Python-Modul `bpy`

Wie in anderen Programmiersprachen auch, lassen sich in Python Bibliotheken anlegen, die abrufbare Funktionalität in vordefinierten Klassen und Methoden (Funktionen) bereit halten. Diese heißen in Python _Module_. Um in Python-Skripten für Blender auf die von Blender vorgehaltene Funktionalität zugreifen zu können, steht in Blender-Python-Skripten das Modul `bpy` (Abk. f. _Blender Python_) zur Verfügung. 

In Blender-Skripten muss dieses Modul wie jedes andere Modul auch zunächst mit einer `import`-Anweisung eingebunden werden:

```Python
import bpy

# Rest des Skripts...
```

Wird die in Blender eingebaute interaktive Python-Konsole verwendet, ist dies automatisch schon geschehen, d.h. es kann direkt auf alles, was `bpy` bietet, zugegriffen werden.

### Aufteilung

Das Modul `bpy` bietet die gesamte skript-bare Blender-Funktionalität in acht "Unterebenen" an.

#### TODO
> - Gebt auf der Blender-Python-Console nur ```bpy.``` ein und drückt dann `Strg`-`Leertaste`, bzw. den Button "Autocomplete" 
> - &rarr; Es werden die acht möglichen "Unterebenen" angezeigt.

Von diesen acht Gruppen unterhalb von `bpy` sollen hier die folgenden drei näher betrachtet werden:
- ```bpy.ops```
- ```bpy.context```
- ```bpy.data```

### Was ist wo in Blender-Python?

Da man sich unmöglich alle Ebenen und Unterebenen der unterhalb con `bpy` aufgespannten Hierarchie merken kann, bietet Blender an zwei Stellen Unterstützung für Skript-Autoren an:

1. Der Arbeitsbereich des Info-Editors (Hauptmenüzeile) listet in Python-Klartext ein Protokoll sämtlicher Benutzer-Aktionen auf. Um diesen zu sehen, muss der untere Rand des normalerweise nur aus der Hauptmenü-Titelzeile bestehenden Info-Editors nach unten gezogen werden. Die hier gelisteten Python-Befehle können auch direkt zeilenweise selektiert werden und dann per Copy-and-Paste in die interaktive 

2. Die Tool-Tips, die beim Verweilen mit der Maus über UI-Elementen erscheinen, zeigen an, wie man per Skript auf das jeweilige UI-Element zugreifen kann. Das funktioniert auch in Abhängigkeit davon, was in der Szene gerade selektiert ist.

## Die wichtigsten "Untermodule" von `bpy`

### `bpy.context`

Klassen und Methoden unterhalb von `bpy.context` erlauben den Zugriff auf die aktuelle Auswahl wie z.B. Objekte, Faces, Kanten u. Vertices

### `bpy.data`

`bpy.data` ermöglicht den Zugriff auf die interne Datenstruktur der gerade in Blender geöffneten Datei. Letztendlich wird hier das ".blend"-Datenformat abgebildet. Auf alles, was in einer .blend-Datei enthalten ist, kann mit  `bpy.data` Zugegriffen werden. Einen Überblick darüber, was das ist, liefert der Outliner-Editor, wenn man ihn von "All Scenes" auf "Blender File" oder "All Data Blocks" umstellt. Python-Kommandos aus den Tool-Tips, die über Benutzerschnitsstellenelemente von Blender Zugriff auf Daten der Szene ermöglichen, sind meistens über `bpy.data`.

### `bpy.ops`

`bpy.ops` steht für "Operationen". Hierunter verbergen sich die Kommandos, die über Tastenkombinationen oder Menüeinträge eingegeben werden können. Die Kommandos, die im Arbeitsbereich des Info-Editors angezeigt werden, stammen meistens aus `bpy.ops`.

## Beispiel: Matrix Extrude



## Aufgaben

Implemeniert ein Skript zum unten beschriebenen "Matrix Extrude":

Insbesondere beim Box Modelling kommt folgende Abfolge von Bearbeitungsschritten auf einer Fläche häufig vor

1. Fläche wird in Richtung der Flächennormalen um eine Länge extrudiert.
2. Die extrudierte Fläche wird skaliert (z.B. verkleinert).
3. Die extrudierte Fläche wird rotiert.

Durch mehrfaches Wiederholen der o.g. Schritte lassen sich sehr gut "Auswüchse" aus einem bestehenden Box-Modell erzeugen, wie z.B. Arme, Beine, Tentakel u.ä.

Schreibt ein Skript, das die aktuell selektierten Flächen eines Mesh um einen bestimmten Betrag entlang der Normalen extrudiert, die Flächen um einen bestimmten Betrag skaliert und rotiert. Packt diese drei Anweisungen in eine Schleife, die eine definierte Anzahl von durchläufen wiederholt wird.

Tipp: Führt oben genannten Arbeitsschritte von Hand aus und schaut im Arbeitsbereich des Info-Editors, welche Python-Befehle sich dahinter verbergen. Die im Info-Editor angezeigten Befehele enthalten immer den vollen Parametersatz. Davon können viele Einstellungen weggelassen werden, wenn sie sowieso die voreingestellten Standardwerte sind. Dünnt die Aufrufe in Eurem Code aus.

Packt die vom Benutzer zu verändernden Werte wie Rotationswinkel/Achse, Skalierungsfaktor, Extrusions-Strecke und Anzahl der Wiederholungen in Variablen, die zentral am Anfang des Skriptes stehen und dort bequem geändert werden können.

- Arbeitet das einleitende Kapitel der offiziellen [Blender-Python-Dokumentation](https://docs.blender.org/api/blender_python_api_current/info_quickstart.html) durch.
  - Was ist das besondere an den `bpy`-Collections?
  - Wie wird ein neues Mesh erzeugt?
  - Wie setze ich das aktuell selektierte Objekt in Python?

- Sucht im Internet sinnvolle Python-Code-Schnipsel für die Verwendung der drei oben genannten "Untermodule" `bpy.context`, `bpy.data`, `bpy.ops`.
 - Probiert die Code-Schnipsel selbst aus.
 - Variiert den Code und schaut was sich ändert
 - Lest die Referenz-Doku u. ggf. andere Quellen zu den verwendeten Befehlen nach.
 - Gibt es im jweiligen Untermodul ähnliche Befehle? Welche Funktion haben diese