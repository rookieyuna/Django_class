from django.db import models

#책 테이블 생성
class Book(models.Model):
    #제목
    title = models.CharField(max_length=100)
    #저자이름 : Author테이블의 PK와 N:N관계를 설정. 저자는 여러권의 책을 쓸 수 있음
    authors = models.ManyToManyField('Author')
    #출판사 : Publisher테이블의 PK와 1:N관계를 설정. 책은 한 출판사에서만 출간
    #models.CASCADE 옵션:부모레코드 삭제시 자식레코드 같이 삭제(오라클과 동일)
    publisher = models.ForeignKey('Publisher', on_delete=models.CASCADE)
    #출판일
    #publication_date = models.DateField('date published') #일종의 설명문
    publication_date = models.DateField()
    
    def __str__(self): #Java의 toString()함수와 유사한 기능
        return self.title 

#저자 테이블 생성
class Author(models.Model):
    name = models.CharField(max_length=50) #저자이름
    salutation = models.CharField(max_length=100) #인사말
    email = models.EmailField() #이메일
    
    def __str__(self):
        return self.name
    
#출판사 테이블 생성
class Publisher(models.Model):
    name = models.CharField(max_length=50) #출판사명
    address = models.CharField(max_length=100) #주소
    website = models.URLField() #웹사이트 URL
    
    def __str__(self):
        return self.name 