from django.db import models
# Create your models here.

'''
장고에서는 테이블을 하나의 클래스로 정의하고,
테이블의 컬럼은 클래스의 변수로 매핑한다.

django.db.models.Model 클래스를 상속받아 정의하고,
각 클래스 타입도 장고에서 미리 정의해둔 필드클래스를 사용한다.
'''
#Question 테이블 생성 : 설문에 필요한 질문
class Question(models.Model):
    '''
    PK(기본키)는 별도로 지정하지 않아도 장고에서 자동으로 생성해준다
    컬럼명은 id로 not null, AutoIncrement 제약조건이 추가된다.
    '''
    question_text = models.CharField(max_length=200) #varchar(200)
    pub_date = models.DateTimeField('date published') #datetime, 문자열은 일종의 설명문
    
    '''
    __str__ : 객체를 문자열로 표현할 때 사용한다. 해당 함수를 
    정의하지 않으면 테이블명이 제대로 표시되지 않는다.
    '''
    def __str__(self):
        return self.question_text


#Choice 테이블 생성 : 질문에 대한 답변항목
class Choice(models.Model):
    '''
    FK는 항상 부모테이블의 PK와 연결되므로 Question 클래스만 지정하면된다.
    FK로 지정된 컬럼은 자동으로 _id라는 접미사가 붙게 된다.
    '''
    question = models.ForeignKey(Question, on_delete=models.CASCADE) #외래키설정
    choice_text = models.CharField(max_length=200) #답변항목, varchar(200)
    votes = models.IntegerField(default=0) #투표수, Integer
    
    def __str__(self):
        return self.choice_text
