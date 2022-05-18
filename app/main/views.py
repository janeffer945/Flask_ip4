from . import main
from flask import render_template,request,redirect,url_for,abort,flash
from ..models import  Blog, User,Comment,Subscriber
from .forms import UpdateProfile,BlogForm,CommentForm
from .. import db,photos
from flask_login import login_required,current_user
from app.request import get_quotes
from ..email import mail_message

