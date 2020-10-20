# Lektion 04 - Blender Add-ons in Python

In der letzten Lektion haben wir gesehen, wie Blender-Kommandos über da `bpy`-Modul aus Python-Code ausgeführt werden können. Hierzu wurde ein Python-Skript innerhalb des Text-Editors erstellt und ausgeführt.

Mit Python implementierte Blender-Automatisierung soll in vielen Fällen unabhängig von einer bestimmten Blender-Szene nutzbar sein. Vielmehr ist es wünschenswert, dass ein einmal erzeugtes Skript in allen Szenen, die mit Blender bearbeitet werden, ausgeführt werden kann. 

Zu diesem Zweck bietet Blender die Möglichkeit, Python-Skripte so anzulegen, dass diese als Add-ons verwendet werden können. Add-ons in Blender können über den "Add-on"-Tab im "User Preferences" Dialog (`Ctrl`-`Alt`-`U`) geladen, aktiviert, deaktiviert und entladen werden.

## Ein erstes (leeres) Add-On

Da ein Add-on nicht Bestandteil einer bestimmten ".blend"-Datei sein soll, sondern für alle möglichen Dateien, die von einer Blender-Installation bearbeitet werden, zur Verfügung stehen soll, muss das Add-on-Skript losgelöst von einer bestimmten ".blend"-Datei entwickelt werden. 

Dazu kann das Python-Skript aus dem ein Blender eingebauten Text-Editor unabhängig von der aktuell geöffneten ".bend"-Datei gespeichert werden. Empfehlenswert ist es allerdings, einen externen Python-Editor (z.B. Visuals Studio Code) zum Editieren der Python-Add-on-Datei zu verwenden

#### TODO
> - Erzeugt eine neue Datei "EmptyAddOn.py" und fügt dieser folgenden Code hinzu: 
>   ```python
>   bl_info = {"name": "My Test Addon", "category": "Object"}
>   def register():
>       print("Hello World")
>   def unregister():
>       print("Goodbye World")
> 
>  - Erklärt euch, was in dieser Datei passiert.
>  - Öffnet den "User Preferences" Dialog und ladet das Add-on:
>    - "Install Add-on from File..." -> Python-Datei auswählen.
>    - Das Add-on sollte im  _Supported Level_ "Community" unter der _Category_ "User" als **Object: My Test Addon** erscheinen.
>  - Öffnet die Blender System Console (Blender-Hauptmenü "Window" -> "Open System Console").
>  - Registriert und Deregistriert das Add-on über die Checkbox neben dem Add-on im "User Preferences" Dialog -> Die o.a. `print`-Ausgaben sollten in der System Console erscheinen.

Folgende Beobachtungen sind bemerkenswert:

- Der minimale Code, um ein Blender-Add-on zu implementieren, ist nicht umfangreich. Es muss noch nicht mal `bpy` importiert werden.
- Ein Add-on in Blender kann registriert und deregistriert werden, dazu muss in der Add-on ".py"-Datei eine `register` und eine `unregister` Funktion definiert werden. Hier kann Code ausgeführt werden, der bei den entsprechenden Aktionen von Bedeutung ist. 
- Ein Blender-Add-on-Skript enthält eine beschreibende Struktur `bl_info` in Form eines Dictionary, in dem u.A. der Name des Add-On und die sog. Kategorie, in der das Add-on erscheinen soll, 
- Die Namen `register`, `unregister` und `bl_info` haben im Kontext von Blender-Add-ons eine besondere Bedeutung.
- Durch die Installation wird das Add-on entweder direkt in das  Blender-Installations-Verzeichnis kopiert (z. B.: C:\Programme\Blender Foundation\Blender\2.79\scripts\addons) oder in das Benutzerdaten-Verzeichnis (z. B.: C:\Users\\_user_\AppData\Roaming\Blender Foundation\Blender\2.79\scripts\addons). Um das Add-on wieder rückstandsfrei zu entfernen, muss die Sktipt-Datei von dort gelöscht werden.

#### TODO
> - Findet die Stelle auf der Festplatte, an die das Add-on installiert wurde.



## Funktionalität hinzufügen

Nun soll das Add-on mit der Matrix-Extrude-Funktionlität der letzten Lektion gefüllt werden.

#### TODO
> - Installiert das Add-on-Skript [MatrixExtrudeAddon.py](MatrixExtrudeAddon.py).
> - Verwendet das Add-on indem ihr im 3D-View mit der Leertaste das Kommando-Menü erscheinen lasst und dann durch die Eingabe von `Matrix Extrude` den neuen Matrix-Extrude-Befehl ausführt.
> - Konnektiert den neuen Matrix-Extrude-Befehl im "User Preferences" Dialog mit einer Tastenkombination Eurer Wahl, in dem ihr den internen Namen des Kommandos `mesh.matrix_extrude` verwendet.

Der Code enthält eine Reihe von bemerkenswerten neuen Eigenschaften.

- Das Dictionary `bl_info` enthält eine Reihe weiterer Einträge.
- Die `register` und `unregister` Funktionen verwenden nun entsprechende Methoden aus `bpy.utils`, um eine selbst definierte Klasse namens `MatrixExtrude` zu registrieren.
- Die Klasse `MatrixExtrude` enthält eine einzige Methode namens `execute`. Hier befindet sich der Code, der die Matrix-Extrudierung durchführt.
- `execute` gibt ein Objekt mit der Eigenschaft `'FINISHED'` zurück.
- Die Klasse  `MatrixExtrude` erbt von `bpy.types.Operator`.
- Daneben enthält die Klasse `MatrixExtrude` die Eigenschaften `bl_idname`, `bl_label` und `bl_options`.

Mit diesem Add-on wurde nun ein so genannter **Operator** in Blender erstellt. Sämtliche eingebauten und auch per Add-on hinzugefügten Operatoren sind wiederum über das Modul `bpy.ops` abrufbar.


## Properties

Die wenigsten Operatoren sind einfach so ohne weitere Angaben ausführbar. Fast alle Operatoren lassen sich in ihrer Funktionalität durch Parameter beeinflussen. In Blender heißen solche Parameter von Operatoren _Properties_.

Properties lassen sich ganz einfach als Eigenschaften der Klasse, die den Operator definiert implementieren (also die Klasse, die von `bpy.types.Operator` erbt und die eine `execute`-Methode definiert). Hierzu können einfach auf Klassenebene Eigenschaften definiert werden, denen ein Aufruf einer der folgenden Funktionen zugewiesen wird.

 - `bpy.props.IntProperty`
 - `bpy.props.BoolProperty`
 - `bpy.props.FloatProperty`
 - `bpy.props.FloatVectorProperty`

Im Beispielcode [MatrixExtrudeAddonProps.py](MatrixExtrudeAddonProps.py) wurden dem Matrix-Etrude-Operator drei solcher Properties hinzugefügt:
- `segment_count` 
- `scale` und
- `angle`

#### TODO
> - Installiert [MatrixExtrudeAddonProps.py](MatrixExtrudeAddonProps.py) als Add-on (ersetzt das alte Add-on damit). 
> - Beobachtet, wie die Properties im unteren Teil des Tool-Tabs (linke Seite des 3D-Editors) erscheinen und wie diese interaktiv verändert werden können.


## Add-ons debuggen

- python-Pfad in der Blender-Installation umbenennen.
- Systemweit Python in der gleichen Version wie Blender installieren.
- Visual Studio Code
- Python Extension
- PTVSD (Python Visual Studio Debugger) `pip install ptvsd`
- Im Skript:
  ```python
  import ptvsd
  ptvsd.enable_attach()
  ```
- In Blender: "User Preferences" -> "File" -> "Scripts": Pfad bis zum "addons"-Unterverzichnis, in dem das zu debuggende Skript liegt. Blender neu starten und Add-on mittels Häkchen registrieren.
- In VS Code: addons-Ordner öffnen und Debug-Konfiguration(en) hinzufügen (im Debug-Pfeil-Dropout).
- Breakpoint in der `execute`-Methode. 
- `Attach`-Debugging starten
- Add-on (Operator) ausführen.

## Aufgabe

- Fügt dem Matrix-Extrude-Operator zwei weitere Properties hinzu:
  - `distance` (Float) - Wie weit soll jedes Face pro Extrusionschritt transliert werden?
  - `proportional` (bool) - Soll die `distance` pro Extrusionsschritt mit `scale` skaliert werden oder soll in jedem Schritt der selbe Abstand verwendet werden?

- Lest euch die Dokumentation zu [`bl_info` im Blender Wiki](https://wiki.blender.org/wiki/Process/Addons/Guidelines/metainfo) durch.

- Informiert euch über die Parameter, die beim Anlegen von Operator-Properties angegeben werden können: https://docs.blender.org/api/blender_python_api_2_77_0/bpy.props.html

- Ersetzt das `angle` Property durch einen FloatVectorProperty, der als Euler-Winkel funktioniert. Dazu müsst ihr die Eulerwinkel, die vom Benutzer in Grad angegeben werden in einen Angle-Axis Wert umrechnen. Das geht mit Hilfe der Blender-Python-Klassen `mathutil.Euler` und `mathutil.Quaternion`.

- Vollzieht das Debugging mit o.b. Methode nach.
