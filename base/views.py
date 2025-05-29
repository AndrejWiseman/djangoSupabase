from django.shortcuts import render
from .models import VrstaJela, Jelo


def index(request):

    # jelo = Jelo.objects.all()
    # vrste_jela = VrstaJela.objects.all()

    vrste_jela = VrstaJela.objects.prefetch_related('jela').all()

    return render(request, 'index.html', {'vrste_jela': vrste_jela})


    context = {
        # 'jelo': jelo,
        # 'vrste_jela': vrste_jela,
        
    }

    # return render(request, 'index.html', context)