from flask import Flask, request, render_template, redirect, url_for, jsonify, abort

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
    book = biblioteka.get(book_id)
    form = Book(data=book)

    if request.method == "POST":
        if form.validate_on_submit():
            biblioteka.update(book_id, form.data)
        return redirect(url_for("biblioteka_list"))
    return render_template("ksiazka.html", form=form, book_id=book_id)

@app.route('/api/biblioteka/', methods=['GET'])
def biblioteka_list_api():
    return jsonify(biblioteka.all())

@app.route('/api/biblioteka/<int:book_id>', methods=['GET'])
def book_details_api(book_id):
    book=biblioteka.get(book_id)
    return jsonify(book)

@app.route('/api/biblioteka/<int:book_id>', methods=['PUT'])
def update_ksiazka(book_id):
    ksiazka = biblioteka.get(book_id)
    if not ksiazka:
        abort(404)
    if not request.json:
        abort(400)
    data = request.json
    if any([
        'title' in data and not isinstance(data.get('title'), str),
        'author' in data and not isinstance(data.get('author'), str),                                          
        'rented' in data and not isinstance(data.get('rented'), str),
        'read' in data and not isinstance(data.get('read'), bool)
    ]):
        abort(400)
    ksiazka = {
        'csrf_token': 1,
        'title': data.get('title', ksiazka['title']),
        'author': data.get('author', ksiazka['author']),
        'rented': data.get('rented', ksiazka['rented']),
        'read': data.get('read', ksiazka['read'])
    }
    biblioteka.update(book_id, ksiazka)
    return jsonify({'ksiazka': ksiazka})

@app.route("/api/biblioteka/<int:book_id>", methods=['DELETE'])
def delete_ksiazka(book_id):
    result = biblioteka.delete(book_id)
    if not result:
        abort(404)
    return jsonify({'result': result})

@app.route("/api/biblioteka/", methods=['POST'])
def create_ksiazka():
    if not request.json or not 'title' in request.json:
        abort(400)
    ksiazka = {
        'csrf_token': 1,
        'title': request.json['title'],
        'author': request.json.get('author', ""),
        'rented': request.json.get('rented', ""),                           
        'read': True
        
    }
    biblioteka.create(ksiazka)
    return jsonify({'ksiazka': ksiazka}), 201


if __name__ == "__main__":
    app.run(debug=True)