from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .apiprovider import ApiProvider
from .models import Wells, Well_data

from .neiro import *


@login_required(login_url='auth/login')
def index(req):
    print(123)
    return render(req, 'main/pages/index.html')


@login_required(login_url='auth/login')
def layout(req):
    print(123)
    wells = Wells.objects.all()

    return render(req, '../layout.html', {'wells': wells})


@login_required(login_url='auth/login')
def importance(req):
    array = ApiProvider(req).getData()[0]
    wells = ApiProvider(req).getData()[1]
    filter = ApiProvider(req).getData()[2]

    fig = Figure(array, wells, filter).fig__bar().to_html()

    context = {'fig': fig}

    return render(req, "main/pages/importance.html", context)


@login_required(login_url='auth/login')
def predicted(req):
    array = ApiProvider(req).getData()[0]
    wells = ApiProvider(req).getData()[1]
    filter = ApiProvider(req).getData()[2]
    
    fig = Figure(array, wells, filter).fig__scatter().to_html()

    context = {'fig': fig}

    return render(req, "main/pages/predicted.html", context)


@login_required(login_url='auth/login')
def difference(req):

    array = ApiProvider(req).getData()[0]
    wells = ApiProvider(req).getData()[1]
    filter = ApiProvider(req).getData()[2]

    fig = Figure(array, wells, filter).predict_list().to_html(index=False)
    percent = Figure(array, wells, filter).percent()
    
    context = {'fig': fig, 'percent': percent}

    return render(req, "main/pages/difference.html", context)


@login_required(login_url='auth/login')
def forecastwell(req):

    array = ApiProvider(req).getData()[0]
    wells = ApiProvider(req).getData()[1]
    filter = ApiProvider(req).getData()[2]
    isNull = Figure(array, wells, filter).predict().empty
    fig = Figure(array, wells, filter).predict().to_html(index=False)
    percent = Figure(array, wells, filter).percent()
    
    context = {'fig': fig, 'percent': percent, 'isNull': isNull}

    return render(req, 'main/pages/forecastwell.html', context)


@login_required(login_url='auth/login')
def onewell(req, id):

    wells_data = list(Well_data.objects.all().filter(well_id=id).values())
    well = Wells.objects.all().filter(pk=id).values()
    wct = []
    dates = []

    for data in wells_data:
        wct.append(data['wct'])

    for data in wells_data:
        dates.append(data['created_date'])

    df = pd.DataFrame(dict(
        y = wct,
        x = dates
    ))
    fig = px.line(df, x="x", y="y", labels={
        "x": "Обводненность (%)",
        "y": "Дата (cm)"
    }, title=well[0]['name'])
    fig = fig.to_html()

    context = {'fig': fig}

    return render(req, 'main/pages/onewell.html', context)