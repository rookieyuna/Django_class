from django import forms
from django.forms.fields import FileField
from django.forms.widgets import TextInput
from django.forms.widgets import PasswordInput 
'''
장고에서 제공하는 Form기능을 사용하려면 우선 forms.Form클래스를 상속
각 변수명은 해당 input태그의 name속성값으로 사용된다.
태그 생성시 required 속성 기본값은 True로 유효성검증을 한다.
'''
class QuestionForm(forms.Form):
    #<input type="text">를 생성. label은 타이틀로 사용
    user_id = forms.CharField(label='아이디', max_length=10)
    #가장 기본적인 input태그를 생성. 타이틀은 title로 표시됨
    title = forms.CharField()
    #여러줄의 텍스트를 입력할 수 있는 <textarea>를 생성
    content = forms.CharField(widget=forms.Textarea)
    #기본적인 input태그를 생성하되 type='email'로 생성
    email = forms.EmailField()
    #<input type="checkbox">를 생성. required => 유효성검증여부
    my_check = forms.BooleanField(required=False)
    
    ######################################################
    
    form1 = forms.CharField(widget=forms.TextInput) 
    #└▶ <input type="text" name="form1" required id="id_form1">
    form2 = forms.CharField(widget=forms.NumberInput)
    #└▶ <input type="number" name="form2" required id="id_form2">
    form3 = forms.CharField(widget=forms.PasswordInput(attrs={'size':'30'})) 
    #└▶ <input type="password" name="form3" required id="id_form3">
    ##추가속성 부여시에는 (attrs={'속성명':'속성값'}) 붙이기
    form4 = forms.CharField(widget=forms.Textarea)
    #└▶ <textarea name="form4" cols="40" rows="10" required id="id_form4">

    data01 = ['유비','관우','장비']
    data02 = [
        ('red', '빨강'),('green', '초록'),('blue', '파랑'),('black', '검정')
    ]
    
    form5 = forms.ChoiceField(
        widget=forms.Select, 
        choices=data02, #option태그 데이터
        initial='green', #selected 데이터의 value값
    )
    '''
    <select name="form5" id="id_form5">
        <option value="red">빨강</option>
        <option value="green" selected>초록</option>
        ....
    </select>
    '''  
    
    form6 = forms.MultipleChoiceField( #select태그지만 mutiple 속성을 부여
        widget=forms.SelectMultiple,
        choices=data02,
        initial=['black','red'] #리스트를 사용하여 다중항목 default선택 가능  
    )
    '''
    <select name="form6" required id="id_form6" multiple>
        <option value="red" selected>빨강</option>
        <option value="green">초록</option>
        <option value="blue">파랑</option>
        <option value="black" selected>검정</option>
    </select>
    '''
    
    form7 = forms.ChoiceField( 
        widget=forms.RadioSelect, #라디오버튼 표현
        choices=data02, #라디오 항목 데이터
        initial='green',
    )
    '''
    <div id="id_form7">
        <div>
            <label for="id_form7_0">
                <input type="radio" name="form7" value="red" required id="id_form7_0">빨강</label>
        </div>
        <div>
            <label for="id_form7_1">
                <input type="radio" name="form7" value="green" required id="id_form7_1" checked>초록</label>
        </div>
        ......
    </div>
    '''
    
    form8 = forms.MultipleChoiceField( 
        widget=forms.CheckboxSelectMultiple(attrs={'class':'red'}),
        #checkbox 타입 표현 #추가속성 부여시에는 (attrs={'속성명':'속성값'}) 붙이기
        choices=data02, #체크박스 항목 데이터
        initial=['black','red'], #리스트를 사용하여 다중항목 default선택 가능  
    )
    '''
    <div id="id_form8">
        <div>
            <label for="id_form8_0">
                <input type="checkbox" name="form8" value="red" id="id_form8_0" checked>빨강</label>
        </div>
        <div>
            <label for="id_form8_1">
                <input type="checkbox" name="form8" value="green" id="id_form8_1">초록</label>
        </div>
        .....
    </div>
    '''
    
    form9 = forms.FileField(required=False)
    # └▶ <input type="file" name="form9" id="id_form9">
    
    
class BoardForm(forms.Form):
    user_id = forms.CharField(label='작성자', max_length=10, 
                            widget=forms.TextInput(attrs={'class':'form-control w100'}))
    user_pw = forms.CharField(label='패스워드', max_length=20, 
                            widget=forms.TextInput(attrs={'class':'form-control w200'})) #widget=PasswordInput
    title = forms.CharField(label='제목', 
                            widget=forms.TextInput(attrs={'class':'form-control'}))
    content = forms.CharField(label='내용', 
                            widget=forms.Textarea(attrs={'class':'form-control'}))
    my_check = forms.FileField(label='첨부파일', required=False,
                            widget=forms.FileInput(attrs={'class':'form-control'}))