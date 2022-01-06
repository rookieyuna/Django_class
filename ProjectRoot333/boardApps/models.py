from django.db import models
import os #remove()함수를 사용
from django.conf import settings #settings.py의 정보를 읽어옴

#게시판 작성을 위한 Post테이블 생성
class Post(models.Model):
    user_name = models.CharField(max_length=5)
    #email = models.EmailField(blank=True, null=True)
    viewCount = models.CharField(default=0, max_length=5)
    postdate =models.DateField(blank=True, null=True)
    titles = models.CharField(max_length=50)
    contents = models.TextField()
    #첨부이미지 : null을 허용하는 컬럼으로 생성(null=True: 빈값 허용)
    mainphoto = models.ImageField(blank=True, null=True)

#이 부분이 없으면 게시글제목이 안나오고 Post object(1),(2)로 나온다
    def __str__(self):
        return self.titles

    #delete()함수 오버라이딩
    def delete(self, *args, **kargs):
        if self.mainphoto:
            print("이미지 삭제")
            print(settings.MEDIA_ROOT, self.mainphoto.path)
            #여기서 이미지 삭제
            os.remove(os.path.join(settings.MEDIA_ROOT, self.mainphoto.path))
        super(Post, self).delete(*args, **kargs)
