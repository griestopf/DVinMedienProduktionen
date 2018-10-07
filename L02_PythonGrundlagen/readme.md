# Lektion 02 - Grundlagen von Python

In dieser Lektion werden die Grundlagen der Programmierung in Python dargestellt. 

## Datentypen

Wie andere Programmiersprachen auch, besitzt Python grundlegende Datentypen. Python verfügt allerdings schon von sich aus über mehr eingebaute Funktionalität als viele andere Sprachen. Collection-Funktinalität wie z.B. dynamisch wachsende Listen oder assoziative Speicher wie Dictionarys sind ebenso bereits direkt in die Sprache eingebaut wie komplexe Zahlen. Einen detaillierten Einblick in diese gibt die [offizielle Python-Dokumentation](https://docs.python.org/3/library/stdtypes.html). Hier nur eine kurze Übersicht: 

- **Numerics**
	- Ganzzahlen (`int`, z. B. `42`)
	- Fließkommazahlen (`float`, z. B. `3.1415`)
	- Komplexe Zahlen (`complex`, z. B. `47.3+11.4`**`j`**)
	- Bool'sche Werte (`bool`, z. B. `True` oder `False`)
- **Sequenzen**
	- Listen (`list`, z. B. **`[`**`4, 3, 2, 1`**`]`**)
	- Tupel (`tuple`, z. B. **`(`**`42, 43, 44, 45`**`)`**)
	- Bereiche (`range`, z. B. `range(10)`)
	- Strings (`string`, z. B. `"Hello, World!"`)
- **Mappings**
	- Dictionary/Hashtable (`dict`, z.B. **`{`**`"Müller":2529, "Pietsch":2528, "Fries":2526`**`}`**)

## Strukturierte Programmierung

Auf die Besonderheit von Python, dass die Einrückung von Code-Blöcken eine syntaktische Rolle spielt, wurde bereits eingegangen. Im Folgenden werden noch mal die am häufigsten gebrauchten Anweisungen zur strukturierten Programmierung gezeigt. Da die meisten dieser Anweisungen als Bedingung einen Bool'schen Wert abfragen, wird zunächst noch darauf eingegangen, wie mehrere Bool'sche Werte mit den üblichen Operationen ("und", "oder", "nicht") in Python kombiniert werden können.

In vielen Programmiersprachen haben sich Operator-Symbole für die Verkettung von Wahrheitswerten (Bool'sche Werte, in Python `True` und `False`) durchgesetzt. In Python hingegen werden hierfür reservierte Worte verwendet:

Operation | Operator in Python | Beispiel | Operator in Java/C/C++/C#/JS/TS 
----------|--------|----------|----------------------------------
Und | `and` | `if A and B:` | `A && B`
Oder | `or` | `while A or B:` | `A || B`
Nicht | `not` | `if not A:` | `!A`

Operatoren, deren Operanden zwar üblicherweise keine Bool'schen Werte sind, die aber als Ergebnis einen Bool'schen Wert generieren sind die üblichen Vergleichsoperatoren. Zudem gibt es in Python noch ein paar weitere solcher Operatoren, die alle typischerweise in Bedingungen von Strukturanweisungen verwendet werden können:

Operator in Python | Bedeutung
-------------------|------------
`==` | Sind linker und rechter Operand gleich? (nicht unbedingt dasselbe Objekt, siehe `is`)
`!=` | Sind linker und rechter Operand nicht gleich? (vgl. `A != B` vs. `not A == B`)
`<>` | Das selbe wie `!=`
`<` und `<=` | Ist der linke Operand kleiner (oder gleich) dem rechten Operanden
`>` und `>=` | Ist der linke Operand größer (oder gleich) dem rechten Operanden
`in` und `not in` | Befindet sich ein Element (nicht) in einer Sequenz? 
`is` und `is not` | Referenzieren zwei Variablen (nicht) dasselbe Objekt?



### Verzweigung/Alternative

Die in fast jeder Programmiersprache bekannte if-Anweisung gibt es auch in Python, die bereits in Lektion 1 kurz beschrieben wurde. Eine Besonderheit gegenüber bekannten Programmiersprachen wie Java/C# ist das Schlüsselwort `elif`, mit denen so genannte if-else-Ketten eleganter aufgebaut werden können, als mit Hilfe
von immer tiefer verschachtelten else-Zweigen.


#### `if`-Beispiel mit `elif`

```python
if a == 1:
	print('eins')
elif a == 2:
	print('zwei')
else:
	print('viele')
```


#### Was ist mit `switch`-`case`?

Die aus vielen Programmiersprachen bekannte switch-case-Anweisung hat kein direktes Äquivalent in Python. Hier bietet sich die Verwendung einer if-elif-Kette an. Auf [Stackoverflow gibt es einen interessanten Thread](https://stackoverflow.com/questions/60208/replacements-for-switch-statement-in-python), der eine Reihe von weiteren Möglichkeiten beschreibt, switch-case-artige Konstrukte in Python zu realisieren.


#### Conditional Operator

Der ebenfalls aus vielen Programmiersprachen bekannte "ternäre" oder "conditional" Operator (`?:`), der oft in Zuweisungen verwendet wird, um einer Variablen einen Wert in Abhängigkeit einer Bedingung zuzuweisen hat in Python hingegen ein Äquivalent. Obwohl hier die Schlüsselworte `if` und `else` vorkommen handelt es sich allerdings _nicht_ um eine if-else-Anweisung. Am besten erklärt sich die Verwendung an einem Beispiel, zunächst in C#

```c#
int alter = 17:
string status = (alter >= 18) ? "erwachsen" : "minderjährig";
```

Der Variablen `status` wird eine Zeichenkette (String) in Abhängigkeit des Alters zugewiesen. 

Hier eine vergleichbare Anweisung in Python

```Python
alter = 17
status = "erwachsen" if alter >= 18 else "minderjährig"
```

Natürlich kann in C# wie auch in Python das gleiche Ergebnis über eine klassische if-else-Anweisung realisiert werden (Übung). 

### Schleifen

Das klassische Schleifenkonstrukt ist es, einen Code-Block so lange zu wiederholen, so lange einer Wiederhol-Bedingung gegeben ist. Die Bedingung wird dabei pro Schleifendurchlauf erneut überprüft. Wie in vielen anderen Programmiersprachen auch, kann dies in Python mit der `while`-Anweisung realisiert werden. Allerdings mit den üblichen Python-Syntax-Merkmalen:

- Doppelpunkt nach der Bedingung
- Einrückung des Schleifenrumpf-Code-Blocks

#### `while` Beispiel

```Python
a = 0
while a < 10:
	print(a)
	a = a+1
```

Solange der Inhalt der Variablen `a` kleiner als zehn ist, wird der Wert ausgegeben und der Inhalt von `a` um eins erhöht. Als Bedingung sind alle möglichen Ausdrücke denkbar, solange sie nur einen Bool'schen Wert (`True` oder `False` liefern).


Sehr oft wird eine Schleife verwendet, um die einzelnen Elemente einer Sequenz (z.B. einer Liste) zu durchlaufen. Hierzu eignet sich die `for`-Anweisung, die genau dieses tut. Hier ein Beispiel

#### `for`-Beispiel

```Python
liste = ["Montag", "Dienstag", "Mittwoch", "Donnerstag"]
for tag in liste:
	print(tag)
```

Im `while`-Beispiel oben ging es darum, mit einer Zählvariablen (`a`) einen Zahlenbereich (von 0 bis 9) zu durchlaufen. Auch hier kann die `for`-Schleife verwendet werden. Da diese allerdings eine Sequenz benötigt, über deren Elemente sie iteriert, muss eine solche Sequenz erst mal erzeugt werden. Da eine Liste zu aufwändig wäre, kann hier stattdessen ein so genannter Bereich (Range) helfen. Dieser ist mit der Funktion `range()` dann auch schnell erzeugt.

#### `for`-Beispiel mit `range`

```Python
for a in range(10):
	print(a)
```


## Klassen

In vielen Programmiersprachen können mit Hilfe von Klassen  _eigene_ Datentypen erschaffen werden, um damit die Komplexität des Programms zu strukturieren. Klassen eignen sich, um zusammengehörende Daten und Methoden zusammenzufassen. Auf der Website pythonbuch.com wird im [Kapitel 8](https://pythonbuch.com/objekte.html) sehr anschaulich und schrittweise darauf eingegangen, wie in Python eigene Klassen erzeugt und verwendet werden können. Hier soll nur in Kürze darauf eingegangen werden.

Die einfachste Klassendklaration in Python definiert nur den Klassennamen:

#### Eine Klassendeklaration

```Python
class Person:
	pass
```

Die `pass`-Anweisung ist nur ein Platzhalter, der die notwendige Einrückung nach dem `:` in der vorangegangen Zeile ausfüllt. Diese hier deklarierte Klasse `Person` besitzt überhaupt keine Eigenschaften: weder Datenbestandteile (die in Python _Instanzvariablen_ heißen (in Java _Attribute_ und in C# _Felder_)), noch Methoden.

Trotzdem kann mit einer derart lasch deklarierten `Person` schon gearbeitet werden:

#### Instanzen (Objekte) von Klassen erzeugen

Um ein Objekt vom Typ anzulegen, muss es erzeugt werden. Im Gegensatz zu vielen anderen Programmiersprachen wird hier _nicht_ das Schlüsselwort `new` verwendet.

```Python
p = Person()
```

#### Instanzvariablen (Felder) beschreiben

```Python
p.Name = "Horst"
p.Alter = 42
print (p.Name, p.Alter)
```

Wie es scheint ist `Person` ein Sammelbecken für alle möglichen Daten, die jedem Objekt beliebig nach der Erzeugung zugewiesen werden können. Es spräche nichts dagegen, einem Objekt vom Typ Person nach dessen Erzeugen auch einen Hubraum und eine PS-Angabe zuzuweisen. Probiert es aus.

Tatsächlich kann man sich ein Objekt von einer wie oben deklarierten "leeren" Klasse eher wie ein Dictionary vorstellen: Unter beliebigen Namen können beliebige Werte abgelegt werden, die dann auch wieder ausgelesen werden können. Manchmal ist aber diese Beliebigkeit etwas zu ungenau.

#### Instanzvariablen (Felder) "deklarieren"

Wie kann nun erreicht werden, dass jede Person schon beim Erzeugen eine vordefinierte Menge an Eigenschaften (Instanzvariablen) besitzt? Wir wollen festlegen, dass jede Person einen Namen und ein Alter hat. Das geht wie folgt:

#### Die `__init__` Methode: Konstruktor und Instanzvariablendeklaration in einem

```Python
class Person:
	def __init___(self, name, alter):
		self.Name = name
		self.Alter = alter
```

Hier müssen ein paar Dinge erklärt werden:

- Mit der `def`-Anweisung wird eine Methode definiert. 
- `__init__` ist ein spezieller Methodenname, der dem Konstruktor in anderen Programmiersprachen gleichkommt.
- Der Parameter `self` in der Parameterliste macht die Methode zu einer Instanzmethode. `self` referenziert dabei die Instanz selbst.
- Die Zuweisungen im Methodenrumpf an `self.Name` und `self.Alter` der als Parameter übergebenen Werte bewirken jeweils drei Dinge:
	1. Die Instanzvariablen `Name` und `Alter` werden deklariert
	2. Die Typen dieser Instanzvariablen werden die Typen der als Parameter übergebenen Werte.
	3. Die Werte dieser Instanzvariablen werden aus den als Parameter übergebenen Werten zugewiesen.

Auf diese Weise ist sichergestellt, dass beim Erzeugen einer neuen Instanz vom Typ `Person` ein Name und ein Alter angegeben werden muss.

#### Instanzen (Objekte) von Klassen mit "Konstruktor" erzeugen

```Python
p = Person("Horst", 42)
print(p.Name, p.Alter)
```

#### Die Rolle von `self`

In der Parameterliste der `__init__`-Methode (in runden Klammern) ist der erste Parameter der Instanzparameter `self`, der zweite Parameter ist der initiale Name und der dritte das initiale Alter. Beim Erzeugen einer Person (`p = Person("Horst", 42)`) entspricht dann `self` der neu angelegten Instanz, während alle Parameter ab dem zweiten als Parameterliste beim Erzeugen angegeben werden müssen. In Python spielt `self` die Rolle der `this`-Referenz aus anderen Programmiersprachen. 

Nicht nur die `__init__`-Methode sondern sämtliche Methoden, die auf Instanzdaten zugreifen sollen, müssen in der Deklaration als ersten Parameter den reservierten Namen `self` deklarieren.

#### Instanzmethoden deklarieren und verwenden

Da mit `__init__` gleich eine spezielle Methode, nämlich der Konstruktor, definiert wurde, ist jetzt aber auch klar, wie "normale" Instanzmethoden deklariert werden. Jede Person soll sich vorstellen können:

```Python
class Person:
	def __init___(self, name, alter):
		self.Name = name
		self.Alter = alter
	def StellDichVor(self):
		print("Ich bin " + self.Name + " und bin " + str(self.Alter) + " Jahre alt.")
```

Nun kann eine Person nach dem Erzeugen aufgefordert werden, sich selbst vorzustellen:

```Python
p = Person("Horst", 42)
p.StellDichVor()
```

Auch hier ist zu bemerken, dass in der Definition von `StellDichVor` als erster (und einziger) Parameter `self` vorkommt. Beim Aufruf von `StellDichVor` ist dann die Parameterliste leer. Der Parameter `self` wird dann durch das Objekt ersetzt, auf dem die Methode aufgerufen wird. Im Beispiel oben als `p`.

Genau genommen kann man die Methode `StellDichVor` auch ohne vorangestellte Instanz verwenden, sondern nur über den Klassennamen `Person`. Dann muss allerdings der Parameter `self` explizit im Aufruf angegeben werden:

```Python
p = Person("Horst", 42)
Person.StellDichVor(p)
```


## Aufgaben

- Arbeitet die Kapitel 4 bis 8 des [Python Buch](https://pythonbuch.com/) durch und notiert Fragen/Ungereimtheiten. Verwendet Visual Studio Code beim Nachvollziehen der Code-Beispiele.

- Lest den Abschnitt [Looping Techniques](https://docs.python.org/3/tutorial/datastructures.html#tut-loopidioms) (Kapitel 5.6 des offiziellen Python-Tutorials) und spielt die Beispiele mit eigenen Varianten durch. Folgende Fragen sollten beantwortet werden können:
	- Wie kann man durch sämtliche Einträge eines Dictionary iterieren?
	- Was bringt einem die Funktion `enumerate()`? Was müsste man machen, wenn es diese nicht gäbe?
	- Was passiert, wenn `zip()` auf unterschiedlich großen Sequenzen angewendet wird?
	- Wie würde man eine `for`-Schleife programmieren, die von 50 in 5-er-Schritten bis 0 herunterzählt?
	- Warum muss im folgenden Beispiel aus o.g. Kapitel die `set()`-Funktion noch aufgerufen werden?
		```Python
		basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
		for f in sorted(set(basket)):
			print(f)	
		```

- Erzeugt ein Kommandozeilenprogramm in Python mit folgender Funktionalität
	- Es soll eine Liste von Personen gespeichert werden können (nicht auf Platte, nur im Speicher des Rechners so lange das Programm läuft).
	- Jede Person soll einen Namen, einen Vornamen und eine Personalnummer besitzen
	- Bei Programmstart soll ein (Text) Menü mit folgender Auswahl erscheinen
		1. Liste von Personen anzeigen
		2. Neue Person anlegen
		3. Person ändern
		4. Person löschen
		5. Programm beenden
	- Ein Benutzer soll dann durch die Eingabe von 1 bis 4 das jeweilige Kommando ausführen können. Nach dem Ausführen des Kommandos soll wieder wie beim Start o.g. Menü erscheinen und eine weitere Auswahl möglich sein.
	- Das Kommando _Liste von Personen anzeigen_ gibt die aktuell gespeicherte Liste von Personen aus. Neben den Angaben Name, Vorname und Personalnummer wird in der Liste auch eine 
	- Das Kommando _Neue Person anlegen_ bewirkt, dass ein Benutzer nacheinander nach Namen, Vornamen und Personalnummer gefragt wird. Sind alle Daten eingegeben, wird die Liste der gespeicherten Personen um die neue Person ergänzt.
	- Das Kommando _Person ändern_ fragt zunächst nach der laufenden Nummer des Eintrags, der geändert werden soll. Dann wird nacheinander Name, Vorname und Personalnummer eingegeben. Ist die Benutzereingabe hier leer, wird das entsprechende Feld _nicht_ geändert. 
	- Das Kommando _Person löschen_ fragt zunächst nach der laufenden Nummer des Eintrags, der gelöscht werden soll. Ist die eingegebene laufende Nummer kleiner oder gleich der Zahl der aktuell gespeicherten Personen, wird die aktuelle Person gelöscht.

- Für Forgeschrittene: Erweitert o.g. Programm um folgende Funktionalität
  - Macht das Programm robust für Fehleingaben. Es sollte nie abstürzen.
  - Erlaubt es, nach gespeicherten Personen über deren Namen, Vornamen oder Personalnummer zu suchen. Erlaubt ggf. die Eingabe von Teil-Angaben und listet alle Personen, die auf das Suchkriterium zutreffen auf.
  - Untersucht die Eingaben auf Plausibilität: Namen dürfen keine Ziffern enthalten. Die Personalnummer sollte nur aus Ziffern bestehen.
  - Erlaubt die Eingabe von Namen und Vornamen in beliebiger Groß- und Kleinschreibung, aber speichert diese so ab, dass jeweils der erste Buchstabe groß und alle anderen klein sind.
  - Erlaubt es, die Personen nach Name, Vorname oder Personalnummer sortiert auszugeben.

  