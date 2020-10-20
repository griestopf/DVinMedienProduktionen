
## Ideen

### Fortgeschrittene Schleifen-Techniken und Anwendungsbeispiele in Blender

- Wie sind typische 3D-Daten in Blender Python organisiert?
- Welche Schleifen-Techniken existieren und wie kann in Blender damit umgegangen werden?

### B-Mesh und andere Geometrie-Datenstrukturen

Um Geometrie in Editing-Werkzeugen zu repräsentieren sind fortgeschrittene 
Speicherungstechniken und Datenstrukturen notwendig. Die aus dem 2. Semester
bekannte Kombination aus Vertexliste und und Dreiecks-/Polygon-Indexliste reicht
nicht aus, um z. B. einzelne Vertices oder Kanten ohne Polygone darzustellen. 
Zudem sind Nachbarschaftsverhältnisse von Vertices, Kanten und Polygonen nicht
explizit darstellbar.

https://wiki.blender.org/wiki/Source/Modeling/BMesh/Design


### Der Catmull-Clark-Algorithmus / Multiresolution Editing / Alternativen

Zentraler Bestandteil in der Modellierung ist die Verfeinerung einfacher
Modelle mittels des Catmull-Clark-Algorithmus, der in Blender
im Subdivision-Surface und im Multiresolution Modifier Anwendung findet.

Wie funktioniert der Algorithmus? Welche Alternativen gibt es / gab es? Warum
ist er so berühmt (er hat sogar den Oscar gewonnen!)?

### Skriptingmöglichkeiten in DaVinci-Resolve [oder anderer Medienproduktions-Software]

Neben Blender können auch andere Skripting-fähige Medienproduktions-Werkzeuge
untersucht und deren Skripting-Möglichkeiten daragestellt werden. 

- DaVinci-Resolve als kostenlos erhältliches extrem mächtiges Werkzeug ist sowohl 
in Python als auch in der Skript-Sprache Lua erweiterbar.

- In Blender kann die Farbberechnung beim Rendern mit Cycles durch die Open Shading Language durch eigene Programmierung erweitert/ersetzt werden.

- Adobe CC Applikationen können mit [Adobe CEP](https://github.com/Adobe-CEP) erweitert werden.


### Numpy und Anwendungen in Blender

Numpy ist eine umfangreiche Mathematische Library und ermöglicht viele Operationen,
die auch für 3D-Geometrie, Texturen etc. sinnvoll sein können.

Siehe [Numpy in Blender](https://www.blendernation.com/2018/01/13/tutorial-series-numpy-blender/).


### Bild (Textur)-Manipulation per Python in Blender

- Kann auf einzelne Pixel einer Textur zugegriffen werden und wenn ja, wie?
- Können Standard-Python-Bildbearbeitungs-Libraries in Blender verwendet werden? Welche? Wie geht das?
- Performance?


### Motion-Tracking Daten aus Motive nach Blender

Die MoCap-Anlage im MSL liefert Bewegungsdaten, die mit der Schnittstelle [NatNet](https://github.com/ratcave/natnetclient) in Echtzeit abgegriffen werden können.

Kann in Blender auf diese Daten zugegriffen werden? Können die Daten direkt in Eevie-Echtzeit-Renderings übertragen werden?



# Aufgabe 2. Semesterhälfte

Freie Aufbgabe im Bereich 3D-CG, Postproduction, VFX mit Augenmerk auf Automatisierung und Skripting.

Die Aufgabe soll in Kleingruppen erarbeitet werden (max. drei Mitglieder pro Kleingruppe).


### Gruppeneinzeltermine 

Pro Gruppe etwa 15 Minuten Darlegung des aktuellen Standes. 

- Ideenvorstellung
- Risikoanalyse (was könnte schief laufen, kritische Pfade identifizieren)
- Arbeitsaufteilung (wer macht was)
- Bereits erfolgte Tätigkeiten
- Bereits gewonnene Erkenntnisse, ggf. auch Schwierigkeiten oder Fehlversuche
- Planung Schritte bis zum Vortrag, insbesondere Risikovermeidungsstrategien


### Vorträge Abgabe

Pro Gruppe etwa 10-15 Minuten Vortrag. Alle Gruppenmitglieder tragen vor

- Präsentation der fertigen Abgabe in Aktion
- Erkenntnisse, Gelerntes, was würden wir beim nächsten Mal anders machen?
- Worauf sind wir stolz?
- Gerne kurze Live-Demonstration von Techniken und Teilschritten
- Ausblick (wie könnte eine Weiterentwicklung/Überarbeitung aussehen)



## Ideen-Pool

- Skriptfähigkeit von DaVinci Resolve untersuchen. 
- Verbesserung von GreenScreen-Ergebnissen
    - vermutlich in Resolve
    - z.B. Automatisierung der ["Rabinowitz-Methode"](https://www.youtube.com/watch?v=-UdeEEppEIA)

- Automatisierung beim Verwenden von MoCap-Daten
    - Hilfe/Automation beim Zuordnen von MoCap-Gelenken zu Model-Gelenken
    - Hilfe/Automation beim Matchen von Größenverhältnissen (Schlanker MoCap-Darsteller -> dicker CG-Character: Durchdringungen verhindern)
    - Tools aus MotionBuilder nach-implementieren. Ziel: Blender als MotionBuilder-Ersatz.

- Blender-Add-on zur automatisierten Generierung von Geometrie, z.B.
    - Treppen
    - Gebäude
    - Strassenzüge (aus OpenStreetMap-Daten?)
    - Sterne, Zahnräder, Blumen
    - Nachbau des Matrix-Extrude-Befehls aus C4D

- Komplexe Geometrie-Operationen mit bmesh
    
