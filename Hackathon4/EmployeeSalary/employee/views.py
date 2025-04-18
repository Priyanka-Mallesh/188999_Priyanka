from django.shortcuts import render
import random
# Create your views here.

def employee_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gross_salary = float(request.POST.get('gross_salary'))
        tax = float(request.POST.get('tax'))
        bonus = float(request.POST.get('bonus'))

        net_salary = gross_salary - (gross_salary * tax / 100) + (gross_salary * bonus / 100)
        
        return render(request, 'result.html', {'name': name, 'net_salary': net_salary})
    return render(request, 'form.html')

def jumble_word(request):
    if request.method == 'POST':
        word = request.POST.get('word')
        jumbled_word = ''.join(random.sample(word, len(word)))
        return render(request, 'jumble_result.html', {'word': word, 'jumbled_word': jumbled_word})
    return render(request, 'jumble.html')
