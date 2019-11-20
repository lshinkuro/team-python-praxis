from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField,SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError,AnyOf
from flaskblog.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(), Length(min=2, max=20)])

    tempatlahir = StringField('Tempat_lahir',validators=[DataRequired(),Length(min=2,max=20)])

    tanggal_lahir= StringField('Tanggal_lahir',validators=[DataRequired(),Length(min=2,max=20)])

    email = StringField('Email',validators=[DataRequired(), Email()])

    nomor_hp = StringField('Nomor hp',validators=[DataRequired()])

    alamat_tinggal = StringField('Alamat Tinggal',validators=[DataRequired()])

    kota_asal = StringField('Kota Asal',validators=[DataRequired()])

    pendidikan = SelectField('Pendidikan',choices=[('Diploma/sarjanaTerapan/vokasi atau Diploma lain'),('Strata1'),('Strata2 atau lebih tinggi',('other'))])

    nama_kampus = StringField('Nama Kampus',validators=[DataRequired(),Length(min=2,max=100)])

    Program_studi = StringField('Program Studi',validators=[DataRequired(),Length(min=2,max=100)])

    alamat_kampus = StringField('Alamat Kampus',validators=[DataRequired()])

    pengalaman_kerja = StringField('Pengalaman Kerja(jika ada)',validators=[DataRequired(),Length(min=2,max=100)])

    pengalaman_project = StringField('Pengalaman Project (jika ada)',)

    tujuan = StringField('Apa tujuan anda mengikuti proses pendidikan di Praxis Academy',validators=[DataRequired()])

    validation1 = SelectField('Apakah anda bersedia menyelesaikan pendidikan di praxis academy',choices=[('ya'),('tidak'),('Mungkin'),('Other')])

    validation2 = SelectField('Apakah anda bersedia Memberikan surat referensi',choices=[('ya'),('tidak'),('Mungkin'),('Other')])

    profil_medsos =StringField('Profil media sosial anda(sebutan media dan username anda)')

    validation3 =SelectField('Mengetahui informasi bootcamp dari',choices=[('Facebook'),('Twitter'),('Instagram'),('Whatsapp'),('Linkedln'),('Teman'),('Other:')])

    validation4 = StringField('Tuliskan nama pemberi informasi(Contoh:Ana-085-xxx-9890 atau Mira IG:@mira21)',validators=[DataRequired()])
    
    password = PasswordField('Password', validators=[DataRequired()])

    confirm_password = PasswordField('Confirm Password',validators=[DataRequired(), EqualTo('password')])

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


class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')
