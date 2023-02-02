from django.shortcuts import render
from django.http import HttpResponseRedirect
from trucks.forms import TruckForm
from trucks.models import Truck


def add_trucks(request):
    '''
    Метод реализует заполнение и внесение данные в БД
    '''
    if request.method == 'POST':
        # оборачиваем вызов в форму
        form = TruckForm(request.POST)
        if form.is_valid():
            truck = Truck(
                model = form.cleaned_data['model'],
                number = form.cleaned_data['number'],
                tonnage = form.cleaned_data['tonnage'],
                workload = form.cleaned_data['workload'],
                overload = form.cleaned_data['overload']
                )
            truck.save()
            return HttpResponseRedirect('/')
    if request.method == 'GET':
        form = TruckForm()
    return render(request, 'add_trucks.html', {'form': form})

def show_trucks(request):
    '''
    Метод реализует получение информации из БД посредством запроса пользователя
    '''
    show_trucks = Truck.objects.all()
    if request.method == 'GET':
        return render(
            request,
            'show_trucks.html',
            {
                'filter_trucks_name': show_trucks.values('model').distinct(),
                'trucks_info': show_trucks
            },
        )
    if request.method == 'POST':
        truck_model = request.POST['model']
        # вызываем данные в соответсвии с выбором пользователя
        # если пользователь выбрал 'Все модели' - вызываем данные всех объектов
        if truck_model == 'Все модели':
            return render(
                request,
                'show_trucks.html',
                {
                    'filter_trucks_name': show_trucks.values('model').distinct(),
                    'trucks_info': show_trucks
                },
            )
        # в другом случае, вызываются объекты по названию модели
        else:
            get_model_truck = Truck.objects.filter(model=truck_model)
            return render(
                request,
                'show_trucks.html',
                {
                    'filter_trucks_name': show_trucks.values('model').distinct(),
                    'trucks_info': get_model_truck
                },
            )
            