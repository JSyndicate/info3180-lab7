# Add any form classes for Flask-WTF here

from wsgiref.validate import validator
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_wtf import TextAreaField
from wtforms.validators import DataRequired

class UploadForm(FlaskForm):
    description= TextAreaField('description',validators=[DataRequired()])
    photo = FileField('photo',validators=[FileRequired(),FileAllowed(['jpg','jpeg','png'],'Image Files Allowed Only!!!')])
    