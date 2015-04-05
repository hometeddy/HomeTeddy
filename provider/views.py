 
from django.shortcuts import render, render_to_response, RequestContext,get_object_or_404,get_list_or_404
from provider.models import Profile, ServiceList

# Create your views here.
def home(request):
    return render_to_response("index.html",
                              locals(),
                              context_instance =RequestContext(request))


def profile(request, profile_id):

        #servicelist = ServiceList.objects.select_related('profile')
	profile = get_object_or_404(Profile, pk=profile_id)
        #context  =  {'servicelist': servicelist, 'profile' : profile }
        context  =  {'profile' : profile }
        return render(request, 'provider/profile.html', context)
