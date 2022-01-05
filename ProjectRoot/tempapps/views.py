from django.shortcuts import render

from tempapps.forms import QuestionForm
from django.http import HttpResponseRedirect
from tempapps.forms import QuestionForm, BoardForm

#tempapps의 index화면 : 바로가기 링크만 있음
def index(request):
    return render(request, 'index.html')

# Template Filter를 사용하기 위한 여러종류의 변수선언 및 Template 호출
def templateFilter(request):
    #정수형 변수
    num1 = 1
    num2 = 10
    #문자형 변수
    engStr = "nakja's MustHave\r\njava <b>web</b>programming" #특수기호와 태그를 포함
    hanStr = "낙자쌤의 자바 웹 프로그래밍"
    #컬렉션형 변수
    dictVar = {'a':'유비', 'b':'관우', 'c':'장비'} #딕셔너리
    listVar = ['손오공','저팔계','사오정'] #리스트
    
    context = {'num1': num1, 'num2': num2, 'engStr': engStr, 'hanStr': hanStr,
               'dictVar': dictVar, 'listVar': listVar}
    #템플릿 호출 및 값 전달
    return render(request, 'template_filter.html', context)

#템플릿 태그
def templateTag(request):
    #딕셔너리를 인자로 가진 리스트
    books = [
        {"name":"자바", "price":1000},
        {"name":"HTML", "price":2000},
        {"name":"JSP", "price":3000},
        
    ]
    #빈 리스트
    hobbys =[]
    favorites = ['운동','공부','여행','경제']
    iVar = range(1,11)
    
    context = {'books':books, 'hobbys':hobbys,'favorites':favorites,'iVar':iVar}
    return render(request, 'template_tag.html', context)


#장고의 폼 생성기능 사용하기
def formCreate(request):
    '''
    Servlet의 doGet(), doPost()와 같이 하나의 함수에서 폼 출력과
    전송된 값 처리를 동시에 하도록 권장하고 있다.
    즉, POST인 경우라면 폼값을 입력한 후 전송할 때의 처리를 말한다.
    '''
    #진입시 전송방식이 POST라면 submit된 폼값을 처리한다.
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        # 폼값의 유효성 검증
        if form.is_valid():
            #폼 데이터가 유효하면 클린데이터로 복사한다
            user_id = form.cleaned_data['user_id']
            
            #폼 데이터에 문제가 없다면 DB에 입력하거나 혹은 비즈니스 로직을 수행한다
            
            #return HttpResponseRedirect('/thanks/') #페이지 이동
            return render(request, 'thanks.html', {'user_id':user_id}) #템플릿 렌더링
    else:
        #전송방식이 GET이라면 입력폼으로 진입한다
        form = QuestionForm()
    #입력폼 진입을 위해 템플릿을 렌더링한다.
    return render(request, 'form_create.html', {'form':form})

    
def thanks(request):
    return render(request, 'thanks.html')


def boardWrite(request):
    if request.method == 'POST':
        template_path = 'boardWrite.html'
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            return render(request, 'thanks.html', {'user_id':user_id}) #템플릿 렌더링
    else:   
        form = BoardForm()
        template_path = 'boardWrite.html'
    
    return render(request, template_path, {'form':form})