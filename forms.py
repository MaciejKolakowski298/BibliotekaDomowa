from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField


class Book(FlaskForm):
    title=StringField('Tytuł')
    author=StringField('Autor')
    read=BooleanField('Czy przeczytane')
    rented=StringField('Pożyczone komu')
