from django.shortcuts import render, render_to_response, RequestContext,get_object_or_404,get_list_or_404


# Create your views here.



def dashboard(request):

       return render(request, 'dashboard/dashboard.html')
