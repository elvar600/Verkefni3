#10.09.18
#Verkefni3

from bottle import*

@route("/")
def index():
    gogn = {
        "title" : "Modular template",
        "content" : "<h1>Hallo mofulate tamplates:</h1>",
        "footer" : "Höfundur &copy; 2018 Elvar H.H.S."
    }
    return template("base.tpl",gogn)

@route("/page1")
def index():
    return template("index1.tpl")

@route("/page2")
def index():
    return template("index2.tpl", name = elvar)

@route("/page3")
def index():
    return template("index2.tpl", name = elvar)




run(host="localhost", port=8080, reloader=True, debug=True)
