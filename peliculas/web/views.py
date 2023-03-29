from django.shortcuts import render

# Create your views here.


def index(request):
    peliculas = [
        {
            'titulo': 'AVATAR 2',
            'imagen': 'https://cloudfront-us-east-1.images.arcpublishing.com/gruponacion/DFFLHUVNEJGYFESCBUN74Z3UGQ.jpg'
        },
        {
            'titulo': 'MARIO BROS',
            'imagen': 'https://i.blogs.es/b9f542/1500x500-5-/1366_2000.jpeg'
        },
        {
            'titulo': 'BARRENDEROS ESPACIALES',
            'imagen': 'https://i.ytimg.com/vi/q7i77k8ZMJ4/maxresdefault.jpg'
        }
    ]
    context = {
        'peliculas': peliculas
    }
    return render(request, 'index.html', context)
