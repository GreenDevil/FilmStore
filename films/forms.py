from django.forms import ModelForm
from films.models import Comments, Order
from django import forms


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comments_text']

class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['quantity']