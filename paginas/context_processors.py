from categorias.models import Categoria

def categorias_context(request):
    return {
        'categorias_globales': Categoria.objects.all()
    }
