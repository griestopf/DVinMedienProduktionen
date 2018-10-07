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

## Schleifen

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









## Aufgaben

- Verwendet

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

  