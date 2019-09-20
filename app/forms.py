from flask_wtf import FlaskForm
from wtforms import BooleanField, TextAreaField
from wtforms.validators import DataRequired
from wtforms.widgets import TextArea


class InputTextForm(FlaskForm):
    inputText = TextAreaField(validators=[DataRequired()], render_kw={"rows": 18, "cols": 70})
    ignoreCase = BooleanField('ignore case', default=True)
    ignoreStopWords = BooleanField('ignore stopwords', default=True)    
