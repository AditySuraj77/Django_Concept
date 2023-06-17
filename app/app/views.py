from django.http import HttpResponse
from django.shortcuts import render
from .form import Userform
from apple.models import Fruit
from team.models import Player
from django.core.paginator import Paginator


def index(request):
    data = {
        'title': 'Home Page',  # render a variable to template to showing data by using dictionary key
        'heading': 'Welcome To Home Page',
        'courselist': ['Python', 'Python OOP', 'GUI', 'Django', 'Machine Learning', 'Deep Learning', 'NLP',
                       'Computer Vision'],  # THis All dictionary item render to index.html page by using
        'symbol': 'Courses',  # Django for loop in index.html page
        'course_detail': [
            {'name': 'Machine Learning', 'Duraton': '8 Hours'},
            {'name': 'Deep Learning', 'Duraton': '6 Hours'},
            {'name': 'NLP', 'Duraton': '3 Hours'},
            {'name': 'Computer Vision', 'Duraton': '2 Hours'}
        ],
        'Numbers': [2, 4, 6, 8, 3, 10, 12, 45, 34, 56]  # this all list item render to index.html page by using django
    }  # if else Statement  or Condition
    return render(request, 'index.html', data)  # render a templates any page


def about(request):
    return render(request, 'about.html')


def contact(request):
    fn = Userform()
    try:
        # email = request.GET.get('email')
        # name = request.GET.get('name')  # Using GET method to collect data from to Contact.html page
        # phone = request.GET.get('phone')
        email = request.POST.get('email')
        name = request.POST.get('name')  # Using POST method to collect data from to Contact.html page
        phone = request.POST.get('phone')
    except:
        pass
    # data = {'email': email, 'name': name, 'phone': phone, 'forms': fn}
    # return render(request, 'Contact.html', data)
    # return redirect('/about/') # Redirect


def course(request):
    return HttpResponse('List of Courses')


def coursesDetails(request, courseid):  # Making Dynamic url      int,str slug
    return HttpResponse(courseid)


def calculator(request):
    result = ''
    try:
        if request.method == "POST":
            num1 = eval(request.POST.get('num1'))
            num2 = eval(request.POST.get('num2'))
            operation = request.POST.get('operation')
            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = num1 / num2

    except:
        result = 'Invalid Operation Please Choose Right Operations'
    return render(request, 'Calculator.html', {'result': result})


def evenodd(request):
    even_or_odd = ''
    if request.method == "POST":
        if (request.POST.get('num')) == "":
            return render(request, 'evenodd.html', {'error': 'ERROR Enter Number'})
        num = eval(request.POST.get('num'))
        if num % 2 == 0:
            even_or_odd = 'Even Number'
        else:
            even_or_odd = 'Odd Number'
    return render(request, 'evenodd.html', {'even_or_odd': even_or_odd})


def marksheet(request):
    data = {}
    if request.method == 'POST':
        num1 = eval(request.POST.get('num1'))
        num2 = eval(request.POST.get('num2'))
        num3 = eval(request.POST.get('num3'))
        num4 = eval(request.POST.get('num4'))
        num5 = eval(request.POST.get('num5'))
        t = num1 + num2 + num3 + num4 + num5
        p = t * 100 / 500
        if p >= 60:
            d = 'First Division'
        elif p >= 48:
            d = 'Second Division'
        elif p >= 35:
            d = 'Third Division'
        else:
            d = 'Fail'
        data = {
            'total': t,
            'percentage': p,
            'division': d
        }
    return render(request, 'marksheet.html', data)


def fruit(request):
    Fruitdata = Fruit.objects.all()
    paginator = Paginator(Fruitdata,1)
    page_number = request.GET.get('page')
    FruitdataFinal = paginator.get_page(page_number)

     #Limiting Query [:4] Limiting content on page
     #dataservices = Fruit.objects.all().order_by('name')[:]
     #if -name is Descinding Order Without - Default mean Ascending Order
     #for i in dataservices:
     #print(i.name)



    """ # Activ Search Bar by using this course
    dataservices = Fruit.objects.all()
    if request.method == 'POST':
        st = request.GET.get('searchdata')
        if st != None:  # Active Search Bar With this Multiple Line of code
            dataservices = Fruit.objects.filter(name__icontains=st)

    databasedata = {
        'dbdata': dataservices
    }
    return render(request, 'fruit.html', databasedata)
    """
    databasedata = {
        #'dbdata': dataservices,
        'Fruitdata':FruitdataFinal
    }
    return render(request, 'fruit.html', databasedata)


def player(request):
    team = Player.objects.all()
    data = {
        'player': team
    }
    return render(request, 'player.html', data)


def playerdetail(request):
    team = Player.objects.all()
    data = {
        'player': team
    }

    return render(request, 'playerdetail.html', data)
