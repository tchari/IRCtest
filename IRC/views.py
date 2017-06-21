from django.shortcuts import render
from django.http import HttpResponse
from IRC.models import Assessment
#from django.contrib.auth.decorators import login_required

def index(request):
	if request.user.is_authenticated:
		assessmentList = Assessment.objects.filter(assessor=request.user.id)
		context = {'assessmentList': assessmentList}
	else:
		context = {}
	
	return render(request, 'IRC/index.html', context)