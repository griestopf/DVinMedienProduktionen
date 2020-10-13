
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



## Termine

Zu den vereinbarten Gruppeneinzelterminen und den Vortrags-Terminen gilt Anwesenheitspflicht aller TeilnehmerInnen. Entschuldigung nur mit ärztlichem Attest.

### Gruppeneinzeltermine 

Pro Gruppe etwa 15 Minuten Darlegung des aktuellen Standes. 

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
    
