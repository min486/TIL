from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        # Article 모델에서 title과 content 사용
        fields = ['title', 'content']
        # fields = '__all__'