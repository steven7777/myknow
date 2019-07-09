from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
#from django.template import loader
from django.http import Http404

from .models import Entity

def index(request):
    #return HttpResponse("Hello, world. You're at the myknow (app) index.")
    #latest_entity_list = Entity.objects.order_by('-created')[:5]
    latest_entity_list = Entity.objects.order_by('-date_created')[:100]
    # SANS template
    #output = ', '.join([q.entity_text for q in latest_entity_list])
    #return HttpResponse(output)
    # AVEC template
    #template = loader.get_template('myknowapp/index.html')
    context = {
        'latest_entity_list': latest_entity_list,
    }
    #return HttpResponse(template.render(context, request))
    '''
    The render() function takes the request object as its first argument, a template name as its second argument and a dictionary as its optional third argument. 
    It returns an HttpResponse object of the given template rendered with the given context
    '''
    return render(request, 'myknowapp/index.html', context)




# VIEW
def detail(request, entity_id):
    #return HttpResponse("You're looking at entity %s." % entity_id)
    '''
    try:
        entity = Entity.objects.get(pk=entity_id)
    except Entity.DoesNotExist:
        raise Http404("Entity does not exist")
    '''
    '''
    There’s also a get_list_or_404() function, which works just as get_object_or_404() – except using filter() instead of get(). 
    It raises Http404 if the list is empty.
    '''
    entity = get_object_or_404(Entity, pk=entity_id)
    return render(request, 'myknowapp/detail.html', {'entity': entity})

