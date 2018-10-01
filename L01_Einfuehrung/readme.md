# Lektion 01 - Einführung

## Ziel der Veranstaltung

### Digitale Medienproduktionen
Die meisten Prozesse in digitalen Medienproduktionen werden mit Hilfe hochspezialisierter Softwaretools durchgeführt. 3D-Modelle und Animationen, Post-Produktion, Color-Grading, Greenscreen Keying, Camera-Tracking usw. sind nur effizient mit Hilfe speziell dafür entwickelter Softwarepakete in Produktionen einsetzbar. 

Ohne jeglichen Anspruch auf Vollständigkeit hier ein paar Beispiele häufig zum Einsatz kommender Werkzeuge:

- Maya
- Cinema 4D
- Nuke
- Blender
- After Effects
- DaVinci Resolve


### Effizienz bei Bewegtbild-Produktionen
Speziell bei Bewegtbild-Medien genügt aber oft nicht die manuelle Bedienung dieser Werkzeuge. Da hier zwischen 24 und 60 Bilder pro Sekunde, bei Stereoproduktionen sogar doppelt so viele, bearbeitet oder generiert werden müssen, ist eine manueller Bild-für-Bild Prozess zu ineffizient.

Eine ausreichende Effizienz lässt sich hier meistens nur mit Hilfe von automatisierten, selbst ablaufenden Prozessen erzielen - also möglichst ohne viel zeitaufwändige und kostenintensive menschliche Interaktion.

### Automatisierung durch Skripting
Derartige automatisierte Prozesse lassen sich meist nur mit Hilfe von Algorithmen, also durch Programmierung, realisieren. Alle oben genannten Beispiele bieten hierzu eine Programmierschnittstelle an, mit der sich meist sämtliche Funktionen der Software per Code ansprechen lassen. Oftmals ist bereits in die Software ein Code-Editor eingebaut. Damit ist die Programmierung so genannter  _Skripte_ oder _Makros_ möglich.


### Die Rolle von Python in der Medienproduktion

In vielen Software-Paketen, die in Medienproduktionen zum Einsatz kommen, wird die Programmiersprache _Python_ verwendet - so können zum Beispiel alle oben genannten Produkte durch Python-Skripte automatisiert werden.

In dieser Veranstaltung soll daher die Verwendung von _Python_ im Umfeld von Medienproduktionen gelehrt werden. Nach einer allgemeinen Einführung in die Programmiersprache wird schnell die Verwendung von Python in der 3D- und Compositing/VFX-Software _Blender_ erarbeitet.

## Einführung in Python

### Historie

Python wurde 1991 von Guido van Rossum während seiner Tätigkeit am _Centrum Wiskunde & Informatica_ in den Niederlanden entwickelt. Der Name _Python_ soll an die britische Comedy-Truppe _Monty Python_ erinnern. Die Sprache wurde im Hinblick auf die Code-Lesbarkeit entwickelt. Bemerkenswert hier ist die besondere Bedeutung von Leerzeichen und Einrückungen, die in vielen anderen Sprachen zwar per Konvention von Programmierern zur Erhöhung der Code-Lesbarkeit verwendet werden können, in Python aber eine syntaktische Rolle spielen und bei falscher Verwendung auch zu Fehlern führen kann (siehe den englischen 
[Wikipedia-Artikel zur Syntax von Python](https://en.wikipedia.org/wiki/Python_syntax_and_semantics#Indentation)).

Vermutlich das besondere Augenmerk auf die Code-Lesbarkeit und das Bestreben, für viele Probleme möglichst nur einen Weg zu bieten, haben stark zur Beliebtheit von Python beigetragen. 

Neben der Verwendung von Python als Skriptsprache in großen Software-Paketen, vor allem in der Medienproduktion, erfreut sich Python auch in wissenschaftlichen Anwendungen großer Beliebtheit. Es gibt zahlreiche Software-Bibliotheken für Python, die auf wissenschaftliche Anwendungen spezialisiert sind. Zudem sind eine Reihe von Technologien im Bereich Maschinelles Lernen und künstliche neuronale Netze auf Python basiert - allen voran die ML-Umgebung **Tensor-Flow** von Google.

### Wichtige Syntax-Elemente

Die wichtigsten syntaktischen Elemente sind hier in Kürze zusammengefasst. Die meisten dieser Merkmale unterscheiden sich deutlich von den Mainstream-Programmiersprachen Java/C/C++/C#/Javascript/Typescript. Der Unterschied ist in den folgenden Abschnitten jeweils aufgeführt.


#### Kommentare

Komentare in Python beginnen mit einem einleitenden `#` und
laufen bis zum Ende der Zeile

##### Beispiel in Python
```Python
# Dies ist ein Kommentar
a = 42  # der Variablen a wird Zwoundvierzig zugewiesen
```

##### Beispiel in C#
```java
// Dies ist ein Kommentar
int a = 42;  // der Variablen a wird Zwoundvierzig zugewiesen
```

#### Blöcke

Zusammengehörige Anweisungen, die hintereinander ausgeführt werden sollen, werden in vielen Programmiersprachen mit geschweiften Klammern `{` und `}` markiert. Zusätzlich rücken Programmierer solche Blöcke im Programmtext ein, um die Lesbarkeit zu erhöhen und die Zusammengehörigkeit zu verdeutlichen. In Python werden Blöcke _nicht_ durch spezielle Anfangs- und Ende-Marker gekennzeichnet, sondern gleich durch eine passende Einrückung. Innerhalb von Blöcken werden Anweisungen mit `;` voneinander getrennt. Das erlaubt es theoretische, mehrere Anweisungen in eine Zeile zu setzen, obwohl die meiste Programmierer nur eine Anweisung pro Zeile verwenden, um die Lesbarkeit zu erhöhen. In Python kann nur eine Anweisung pro Zeile verwendet werdnen, dafür ist aber auch das Semikolon nicht
nötig.

##### Beispiel in Python
```Python
if alter >= 18:
	print("Du bist volljährig")
	EnterAdultZone()
NextStep()
```

##### Beispiel in C#
```java
if (alter >= 18)
{
	Console.WriteLine("Du bist volljährig");
	EnterAdultZone();
}
NextStep();
```

#### Variablen

Im Gegensatz zu einigen der o.G. Programmiersprachen müssen in Python Variablen _nicht_ vor ihrer Verwendung deklariert werden. Die erste Verwendung (Zuweisung) einer Variablen deklariert diese auch gleichzeitig. Der Typ der Variablen wird dann ebenfalls aus dem Kontext der ersten Zuweisung ermittelt und festgelegt.

##### Beispiel in Python
```Python
a = 42        # an integer
b = 3.1415    # a float
c = "Hello"   # a string
```

##### Beispiel in C#
```c#
int a = 42;          // an integer
double b = 3.1415;   // a float
string c = "Hello";  // a string
```

## Aufgaben

- Installiert die neueste [Python Version](https://code.visualstudio.com/docs/python/python-tutorial). 

- Installiert [Visual Studio Code](https://code.visualstudio.com/download).

- Installiert die [Python Extension für Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-python.python).

- Arbeitet das [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial) Tutorial durch und stellt sicher,
das die o.g. Werkzeuge laufen.

- Arbeitet die ersten drei Kapitel des [Python Buch](https://pythonbuch.com/) durch und notiert Fragen/Ungereimtheiten. Verwendet Visual Studio Code beim Nachvollziehen der Code-Beispiele.

- Erzeugt ein kleines Python Programm, das eine oder mehrere Texteingaben entgegennimmt und auf Grund dieser eine Ausgabe produziert.

## Literatur

### Einführung in Python auf Deutsch
https://pythonbuch.com/

### Erste Schritte in Python mit Visual Studio Code
https://code.visualstudio.com/docs/python/python-tutorial


### Lynda.com Kurs: Blender Python Scripting

https://www.lynda.com/Blender-tutorials/Python-Scripting-Blender/486043-2.html?org=hs-furtwangen.de


### E-BOOK: The Blender Python API

The Blender Python API : Precision 3D Modeling and Add-on Development 
von Conlan, Chris 
Veröffentlicht: Berkeley, CA Apress, 2017
Als E-Book in der Bibliothek

### Thesis "The Role of Python in Visual Effects Pipeline"

https://www.theseus.fi/bitstream/handle/10024/115922/Kazakov_Vladislav.pdf?sequence=1




