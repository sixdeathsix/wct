from .models import *

class ApiProvider:
    
    def __init__(self, request):
        self.request = request

    def getData(self):
        stations = []
        filter = []
        wells = []
        array = []

        user_id = self.request.user.id
        station_id = self.request.user.groups.all()[0]

        if str(station_id) == "director":
            station = Station.objects.all().filter(director_id = user_id).values()
        else:
            station = Station.objects.all().filter(group_id = station_id).values()

        for i in station:
            stations.append(i['id'])

        well_count = Wells.objects.all().values()
        array_filter = Wells.objects.all().filter(station_id_id__in = stations).values()
        well = Wells.objects.all().filter(oil_count = 0).values()

        for i in well:
            wells.append(i['id']-1)

        for i in array_filter:
            filter.append(i['id']-1)

        for i in range(len(well_count)):
            well = Wells.objects.all().filter(id = i+1).values().latest('id')
            debit = Well_data.objects.all().filter(well_id = i+1).values().latest('id')
            well['q_oil'] = debit['q_oil']
            array.append(well)

        return array, wells, filter