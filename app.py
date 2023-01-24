from flask import Flask, request, render_template, redirect, url_for

from forms import Book
from models import biblioteka

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

@app.route("/biblioteka/", methods=["GET", "POST"])
def biblioteka_list():
    form = Book()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            biblioteka.create(form.data)
            biblioteka.save_all()
        return redirect(url_for("biblioteka_list"))

    return render_template("biblioteka.html", form=form, books=biblioteka.all(), error=error)


@app.route("/biblioteka/<int:book_id>/", methods=["GET", "POST"])
def book_details(book_id):
    book = biblioteka.get(book_id - 1)
    form = Book(data=book)

    if request.method == "POST":
        if form.validate_on_submit():
            biblioteka.update(book_id - 1, form.data)
        return redirect(url_for("biblioteka_list"))
    return render_template("ksiazka.html", form=form, book_id=book_id)


if __name__ == "__main__":
    app.run(debug=True)