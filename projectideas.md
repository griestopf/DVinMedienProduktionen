# Vortrag 1. Semesterhälfte

Jede Gruppe soll zu einem Skripting/DV

## Ideen

### Fortgeschrittene Schleifen-Techniken und Anwendungsbeispiele in Blender

### B-Mesh und andere Geometrie-Datenstrukturen

https://wiki.blender.org/wiki/Source/Modeling/BMesh/Design


### Der Catmull-Clark-Algorithmus / Multiresolution Editing / Alternativen

### Skriptingmöglichkeiten in DaVinci-Resolve [oder anderer Medienproduktions-Software]

### Numpy und Anwendungen in Blender

https://www.blendernation.com/2018/01/13/tutorial-series-numpy-blender/


### Bild (Textur)-Manipulation per Python in Blender



### Motion-Tracking Daten aus Motive nach Blender

https://github.com/ratcave/natnetclient






# Aufgabe 2. Semesterhälfte

Freie Abgabe im Bereich 3D-CG, Postproduction, VFX mit Augenmerk auf Automatisierung und Skripting.

Die Aufgabe soll in Kleingruppen erarbeitet werden (max. drei Mitglieder pro Kleingruppe).

## Bewertungskriterien
- Wurde die zur Verfügung stehende Zeit genutzt? 
    - Negativ-Beispiele
        - am 2. Zwischenbereicht einen Aufguss der Ideenvorstellung vom 1. Zwischenbericht zeigen
        - Footage-Produktion so knapp geplant, dass bei Nicht-Verwendbarkeit kein zweiter Versuch möglich ist
        -   Kritische Punkte nicht identifiziert und nicht vor dem 2. Zwischenbericht ausprobiert
- Komplexität der Aufgabe
- Darstellung der Fertigkeiten im Bereich Skripting einer VFX/Compositing/3D-Anwendung
- Qualität der Vorträge (Vorbereitung, Visualisierungen, Folien, …)
- Lerneffekt der Vorträge (konnten Zuschauer etwas mitnehmen, war etwas Neues dabei)
- Umsetzung: Wie stark wurde der die Zielsetzung erreicht
- Handwerkliche Qualität der Arbeit (alles auf Kante genäht oder am Ergebnis gefeilt, bis es passt)
- Codequalität im Sinne von SW-Design


## Zwischenberichte

Zu den Zwischenberichten gilt Anwesenheitspflicht aller TeilnehmerInnen. Entschuldigung nur mit ärztlichem Attest.

### Zwischenbericht 1

Pro Gruppe etwa 10 Minuten Vortrag. Alle Gruppenmitglieder tragen vor

- Ideenvorstellung
- Risikoanalyse (was könnte schief laufen, kritische Pfade identifizieren)
- Arbeitsaufteilung (wer macht was)
- Bereits erfolgte Tätigkeiten
- Bereits gewonnene Erkenntnisse, ggf. auch Schwierigkeiten oder Fehlversuche
- Planung Schritte bis ZB 2, insbesondere Risikovermeidungsstrategien


### Zwischenbericht 2

Pro Gruppe etwa 10-15 Minuten Vortrag. Alle Gruppenmitglieder tragen vor

- Stand der Arbeit 
- Wie verlief die Risikovermeidung? 
- Ggf. Planänderungen
- Gewonnene Erkenntnisse, gerne kurze Live-Demonstration von Techniken und Teilschritten
- Planung Schritte zum Abschlussbericht


### Abschlussbericht

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
    
