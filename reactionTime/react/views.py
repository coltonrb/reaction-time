from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse

from react.models import *


def index(request):
    return render(request, 'react/game.html')

@csrf_exempt
def scores(request):
    if(request.method == 'POST'):
        # do stuff
        curScore = HighScore(user=request.POST['username'], score=request.POST['score'])
        print(curScore)
        curScore.save()
        return HttpResponse()
    else:
        high_scores = HighScore.objects.order_by('score')
        return render(request, 'react/scores.html', {'high_scores': high_scores})
