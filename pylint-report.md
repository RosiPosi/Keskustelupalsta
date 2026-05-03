Pylint antaa seuraavan raportin sovelluksesta:

```
************* Module app
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:18:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:22:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:29:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:35:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:40:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:58:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:66:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:91:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:97:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:127:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:145:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:164:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:201:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:215:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:201:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:224:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:224:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:251:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:264:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:274:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:292:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:304:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:308:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:329:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:338:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:329:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:348:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module config
config.py:1:0: C0114: Missing module docstring (missing-module-docstring)
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
************* Module db
db.py:24:0: C0304: Final newline missing (missing-final-newline)
db.py:1:0: C0114: Missing module docstring (missing-module-docstring)
db.py:4:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:10:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:20:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:20:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
************* Module items
items.py:1:0: C0114: Missing module docstring (missing-module-docstring)
items.py:3:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:13:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:23:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:27:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:41:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:55:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:59:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:64:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:68:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:72:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:77:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:81:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:85:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:89:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:101:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:116:0: C0116: Missing function or method docstring (missing-function-docstring)
items.py:124:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module users
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:5:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:10:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:17:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:22:0: C0116: Missing function or method docstring (missing-function-docstring)
users.py:32:4: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)

------------------------------------------------------------------
Your code has been rated at 8.29/10 (previous run: 8.26/10, +0.03)
```

Käydään läpi tarkemmin raportin sisältö ja miksi kaikki ei ole korjattu.

## Docstring-ilmoitukset:
```
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:18:0: C0116: Missing function or method docstring (missing-function-docstring)
```

Raportissa mainitaan paljon docstring-kommentteiden puuttuminen. Sovelluksen teossa ei ollut tarvetta dokumentoida koodi docstring-kommenteilla, jolloin niiden yli voi hypätä tietoisesti.

## Tarpeeton else:
```
app.py:215:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
app.py:338:8: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
users.py:32:4: R1705: Unnecessary "else" after "return", remove the "else" and de-indent the code inside it (no-else-return)
```

Ensimmäiseen ilmoitukseen liittyvä koodi:
```python
if request.method == "POST":
    check_csrf()
    if "remove" in request.form:
        items.remove_item(item_id)
        return redirect("/")
    else:
        return redirect("/opinion/" + str(item_id))
```

Pylint haluaa koodin kirjoitettuna seuraavasti:
```python
if request.method == "POST":
    check_csrf()
    if "remove" in request.form:
        items.remove_item(item_id)
        return redirect("/")
    return redirect("/opinion/" + str(item_id))
```

Kehittäjän näkemyksellä `else`-haarojen lisääminen auttaa visualisoimaan mitä vaihtoehtoja tapahtumilla on. Tällöin koodi on jätetty tarpeettomilla `else`-haaroilla helpottamaan lukemista.

## Puuttuva palautusarvo:
```
app.py:201:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
app.py:224:0: R1710: Either all return statements in a function should return an expression, or none of them should. (inconsistent-return-statements)
```

Ensimmäiseen ilmoitukseen liittyvä koodi:
```python
@app.route("/remove_opinion/<int:item_id>", methods=["GET", "POST"])
def remove_item(item_id):
    check_login()

    item = items.get_item(item_id)
    if not item:
        abort(404)
    if item[ "user_id"] != session["user_id"]:
        abort(403)

    if request.method == "GET":
        return render_template("remove_item.html", item=item)

    if request.method == "POST":
        check_csrf()
        if "remove" in request.form:
            items.remove_item(item_id)
            return redirect("/")
        else:
            return redirect("/opinion/" + str(item_id))
```

Ilmoitus haluaa varoittaa, että koodi ei palauta arvoa, kun `request.method` ei ole `GET` tai `POST`. Tämä ei ole kuitenkaan mahdollista, sillä funktion dekoraattorissa vaaditaan, että metodin tulee olla `GET` tai `POST`. Tällöin ei ole riskiä, että funktio ei palauta mitään.

## Vakion nimi:
```
config.py:1:0: C0103: Constant name "secret_key" doesn't conform to UPPER_CASE naming style (invalid-name)
```

