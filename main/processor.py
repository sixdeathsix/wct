from .models import Wells


def foos(request):

    return {'wells': Wells.objects.all()}

