'''
단축함수 : 장고에서 웹 프로그램 개발 시 자주 사용하는 기능들을
    내장함수로 제공하고 있는데 이를 단축함수라 한다.
    ex) render() 함수 
'''
from django.shortcuts import render
from django.shortcuts import get_object_or_404

#Model을 사용하기 위한 import
from livepolls.models import Question
from livepolls.models import Choice

from django.http import HttpResponseRedirect
from django.urls import reverse

#메인화면 : 기능은 없고 단순히 바로가기 링크만 있음
def main(request): #views에 함수 정의 시 request 내장객체는 필수요소임
    return render(request, 'livepolls/main.html')

#투표앱의 첫번째 화면으로 질문이 리스팅 된다.
def index(request):
    #Question 테이블의 pub_date를 내림차순정렬하여 최근 게시물 5개를 가져옴
    latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    #템플릿으로 데이터를 전달하기 위해 딕셔너리에 저장
    context ={'latest_question_list': latest_question_list}
    #render함수를 통해 템플릿을 로드하면서 데이터를 전달
    return render(request, 'livepolls/index.html', context)

'''
get_object_or_404(모델클래스, 검색조건)
    : 모델클래스(테이블)에서 검색 조건에 맞는 객체를 조회하여 반환한다.
    만약 조건에 맞는 객체가 없다면 Http404를 발생시킨다.
'''
def detail(request, question_id):
    #URL패턴을 통해 전달된 일련번호로 Question테이블을 검색 후 반환한다.
    question = get_object_or_404(Question, pk=question_id)
    #조회된 데이터를 딕셔너리를 통해 템플릿으로 반환
    return render(request, 'livepolls/detail.html',{'question':question})

#투표 처리 : 선택한 항목의 vote 컬럼을 +1한다.
def vote(request, question_id):
    #선택한 질문의 일련번호를 통해 레코드를 가져온다.
    question = get_object_or_404(Question, pk=question_id)
    try:
        #detail페이지에서 선택한 항목을 통해 choice테이블에서 레코드를 가져온다.
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        #예외발생시 detail페이지를 다시 보여준다. 이때 에러메세지를 전달
        return render(request, 'livepolls/detail.html',{
                'question':question,
                'error_message':"You didn't select a choice"
        })
    else: 
        # try절의 코드가 정상실행되면 가져온 레코드로 votes 항목을 +1
        selected_choice.votes += 1
        # 실제 테이블에 업데이트 처리
        selected_choice.save()
        # 처리완료 후 result 페이지로 이동한다.
        return HttpResponseRedirect(reverse('livepolls:results', args=(question.id,)))
        '''
            reverse(urls의 별칭, 인수)
                :별칭과 인수를 통해 URL을 만들기 위한 함수이다.
                보통은 요청이 있을 때 URL을 분석한 후 필요한 view를 호출하지만
                이 경우에는 별칭을 통해 거꾸로 URL을 만들기 때문에 reverse라는 이름이 붙었다
        '''
#투표 결과 보기
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'livepolls/results.html', {'question':question})