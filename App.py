from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, template_folder="templates", static_folder="static")

todo = [{"task": "Sample Todo", "done": False}]

@app.route("/")
def index():
    return render_template("index.html", todos=todo)

@app.route("/add", methods=["POST"])
def add():
    task = request.form['todo']
    todo.append({"task": task, "done": False})
    return redirect(url_for('index'))

@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    task = todo[index]
    if request.method == "POST":
        task['task'] = request.form["todo"]
        return redirect(url_for('index'))
    return render_template("edit.html", todo=task, index=index)

@app.route("/check/<int:index>")
def check(index):
    todo[index]['done'] = not todo[index]['done']
    return redirect(url_for('index'))

@app.route("/delete/<int:index>")
def delete(index):
    del todo[index]
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)
