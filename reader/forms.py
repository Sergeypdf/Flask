from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, NumberRange, ValidationError
from reader.models import Book

class BookForm(FlaskForm):
    title = StringField('Kirjan nimi', validators=[DataRequired(),
                                             Length(min=5, max=100)])
    author = StringField('Tekijä', validators=[DataRequired(),
                                             Length(min=5, max=100)])
    genre = StringField('Genre', validators=[DataRequired(),
                                             Length(min=5, max=20)])
    cover = FileField('Kirjan kansi', validators=[FileAllowed(['jpg', 'png'])])
    rating = IntegerField('Minun arvosana', validators=[DataRequired(), NumberRange(min=1, max=5)])
    description = TextAreaField('Juoni',
                                validators=[DataRequired(),
                                            Length(max=500)])
    notes = TextAreaField('Muistiinpanoja',
                                validators=[DataRequired(),
                                            Length(max=500)])
    submit = SubmitField('Lisätä')

    def validate_title(self, title):
        title = Book.query.filter_by(title=title.data).first()
        if title:
            raise ValidationError('Tämä kirja on jo lukijalistalla.')


class UpdateBook(FlaskForm):
    title = StringField('Kirjan nimi', validators=[DataRequired(),
                                             Length(min=5, max=100)])
    author = StringField('Tekijä', validators=[DataRequired(),
                                             Length(min=5, max=100)])
    genre = StringField('Genre', validators=[DataRequired(),
                                             Length(min=5, max=20)])
    cover = FileField('Kirjan kansi', validators=[FileAllowed(['jpg', 'png'])])
    rating = IntegerField('Minun arvosana', validators=[DataRequired(), NumberRange(min=1, max=5)])
    description = TextAreaField('Juoni',
                                validators=[DataRequired(),
                                            Length(max=500)])
    notes = TextAreaField('Muistiinpanoja',
                                validators=[DataRequired(),
                                            Length(max=500)])
    submit = SubmitField('Päivittää')