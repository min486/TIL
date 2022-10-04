from django.db import models

# Create your models here.

# 모델 정의 (DB 설계)
# 1. 클래스 정의
class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
# 2. 마이그레이션 파일 생성
# 3. DB 반영 (migrate)