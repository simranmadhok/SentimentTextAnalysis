from flask_wtf import FlaskForm
from wtforms import BooleanField, TextAreaField
from wtforms.validators import DataRequired


class InputTextForm(FlaskForm):
    inputText = TextAreaField(validators=[DataRequired()])
    ignoreCase = BooleanField('ignore case', default=True)
    ignoreStopWords = BooleanField('ignore stopwords', default=True)    
