from django.shortcuts import render


#def index(request):
#    return render(request, 'mainApp/homePage.html')

def index(request):
    return render(request, 'mainApp/index.html')

def contact(request):
    pass
#    return render(request, 'mainApp/basic.html', {'values': [
#        'Если у вас остались вопросы то задавайте их мне по телефону',
#        '(068) 068-68-68',
#        'example@mail.ru'
#    ]})
