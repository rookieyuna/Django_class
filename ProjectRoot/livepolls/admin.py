from django.contrib import admin
from livepolls.models import Question, Choice




#4. 외래키 테이블을 한 화면에서 편집하기
#class ChoiceInline(admin.StackedInline): #세로형태 배치
class ChoiceInline(admin.TabularInline): #가로형태 배치
    model = Choice #테이블 선택
    extra = 4 #입력상자 수

##B[관리자 설정 변경]
#1. 필드 순서 변경하기 : 테이블에 적용되진 않고 관리자모드에서만 순서변경
'''class QuestionChanger(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']
'''

#2. 필드 분리해서 보여주기 + 순서변경 (1번과 동시사용 불가)
class QuestionChanger(admin.ModelAdmin):
    fieldsets = [
        ('질문을 입력하세요', {'fields':['question_text']}),
        #3. 필드 접기 : 'classes': ['collapse'] 만 추가하면 접기 기능 구현
        ('날짜를 입력하세요', {'fields':['pub_date'], 'classes': ['collapse']}),
    ]
    #4번 class생성 후 설정추가
    inlines = [ChoiceInline]

    #5. list_filter 추가하기
    list_display = ('question_text', 'pub_date')
    list_filter = ['pub_date']

    #6. search_fields 추가하기
    search_fields = ['question_text']


'''
##A
models.py에서 테이블을 생성하면 관리자 모드에 적용하기 위해
아래와 같이 등록절차가 필요하다.
'''
admin.site.register(Question, QuestionChanger) #관리자모드 설정위해 QuestionChanger 추가
admin.site.register(Choice)