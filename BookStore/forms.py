from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField 
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from BookStore.models import User,Admin,Book


class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')


class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    address= TextAreaField ('Address')
    state= StringField('State')
    pincode= StringField('Pincode')
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email is taken. Please choose a different one.')
                

class AdminLoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

 
class AddBookForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    author = StringField('Author',validators=[DataRequired()])
    publication = StringField('Publication',validators=[DataRequired()])
    ISBN = StringField('ISBN',validators=[DataRequired()]) 
    content = TextAreaField ('Content',validators=[DataRequired()])
    price = StringField('Price',validators=[DataRequired()])
    piece = StringField('Piece',validators=[DataRequired()])
    picture = FileField('Add Book Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Add Book')

    def validate_title(self, title):
        title = Book.query.filter_by(title=title.data).first()
        if title:
            raise ValidationError('That Tittle Book is already in Store.')

    def validate_ISBN(self, ISBN):
        isbn = Book.query.filter_by(ISBN=ISBN.data).first()
        if isbn:
            raise ValidationError('That ISBN Book is already in Store.') 
            
class UpdateBookForm(FlaskForm):
    title = StringField('Title',validators=[DataRequired()])
    author = StringField('Author',validators=[DataRequired()])
    publication = StringField('Publication',validators=[DataRequired()])
    ISBN = StringField('ISBN',validators=[DataRequired()]) 
    content = TextAreaField ('Content',validators=[DataRequired()])
    price = StringField('Price',validators=[DataRequired()])
    piece = StringField('Piece',validators=[DataRequired()])
    picture = FileField('Add Book Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update Book')            