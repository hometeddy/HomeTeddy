from django.shortcuts import render
from django.views import generic
from provider.models import Profile,ServiceList
from service.models import ItemType,Item
from .forms import SearchForm


##def search(request,itemtype_id=1):
##      list_of_provider=Profile.objects.filter(ItemType_id=itemtype_id)
##      return render(request,'search/search.html',{'list_of_provider':list_of_provider})

##def gosearch(request,itemtype_id):
##      HttpResponseRedirect(reverse('views.search', args=(itemtype_id,)))


#class Search(generic.ListView):
#    template_name= 'search/search.html'
#    context_object_name = 'list_of_provider'

#    def get_queryset(self):
#        return Profile.objects.all()


# Code implemented by ZR below

def search(request):
    # if this is a POST request we need to process the form data
    if request.method == 'GET':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.GET)
        # check whether it's valid:
        if form.is_valid():
            selected_choice = form.cleaned_data['service']
            profile_list = Profile.objects.filter(ItemType__id=selected_choice)
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'search/search.html', {'profile_list': profile_list,'form': form})
        else:
            profile_list = Profile.objects.all()
            return render(request, 'search/search.html', {'profile_list': profile_list,'form': form})