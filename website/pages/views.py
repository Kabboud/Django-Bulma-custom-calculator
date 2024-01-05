from django.shortcuts import render


def home(request):
    return render(request, 'pages/main.html')


def installation(request):
    return render(request, 'pages/installation.html')


def tutorial(request):
    return render(request, 'pages/tutorial.html', {'eval': '{{eval}}', 'error': '{{error}}', 'result': '{{result}}'})


def results(request):
    if 'value' in request.GET:
        evalString = request.GET['value']
        return render(request, 'pages/results.html', {'eval': evalString})
    elif 'result' in request.GET:
        if request.GET['result'] == '':
            return render(request, 'pages/results.html')
        try:
            evalString = str(eval(request.GET['result']))
            return render(request, 'pages/results.html', {'result': evalString})
        except ZeroDivisionError:
            return render(request, 'pages/results.html', {'error': 'Error: Div by 0'})
        except SyntaxError:
            return render(request, 'pages/results.html', {'error': 'Invalid Input'})
    elif 'delete' in request.GET:
        evalString = request.GET['delete'][:-1]
        return render(request, 'pages/results.html', {'eval': evalString})
    else:
        return render(request, 'pages/results.html')


def conclusion(request):
    return render(request, 'pages/conclusion.html')


def references(request):
    return render(request, 'pages/credits.html')