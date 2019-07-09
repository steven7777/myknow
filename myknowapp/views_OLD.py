from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
#from django.views.generic import TemplateView, ListView
from django.db.models import Q

from .models import Entity
#from .forms import EntityCompareForm



class AboutView(generic.TemplateView):
    #template_name = "about.html"
    template_name = "myknowapp/about.html"

class SearchSubmitView(generic.TemplateView):
    template_name = 'myknowapp/search.html'
class SearchResultsView(generic.ListView):
    model = Entity
    template_name = 'myknowapp/search_results.html'
    #queryset = Entity.objects.filter(name__icontains='ness') #
    def get_queryset(self):
        #return Entity.objects.filter(name__icontains='ness')
        query = self.request.GET.get('q')
        #name1 = self.request.GET.get('name1')
        #name2 = self.request.GET.get('name2')
        object_list = Entity.objects.filter(
            #Q(name__icontains='ness') | Q(name__icontains='l')
            #Q(name__icontains=name1) | Q(name__icontains=name2)
            Q(name__icontains=query) | Q(comment__icontains=query)
        )
        return object_list

class CompareSubmitView(generic.TemplateView):
    template_name = 'myknowapp/compare.html'
class CompareResultsView(generic.ListView):
    model = Entity
    template_name = 'myknowapp/compare_results.html'
    context_object_name = 'compared_entities_list'
    #queryset = Entity.objects.filter(name__icontains='ness') #
    def get_queryset(self):
        #return Entity.objects.filter(name__icontains='ness')
        name1 = self.request.GET.get('name1')
        name2 = self.request.GET.get('name2')
        object_list = Entity.objects.filter(
            #Q(name__icontains='ness') | Q(name__icontains='l')
            #Q(name__icontains=name1) | Q(name__icontains=name2)
            Q(name__icontains=name1) | Q(name__icontains=name2)
        )
        '''
        e1 = Entity.objects.get(name=name1)
        e2 = Entity.objects.get(name=name2)
        '''
        # compared_entities_list
        return object_list



"""
def search(request):
    C
    Using more advanced Python libraries like FuzzyWuzzy, 
    we can perform searches using queries with like text, 
    instead of returning only exact matches.  
    C
    query_string = ''
    found_entries = None
    if ('q' in request.GET) and request.GET['q'].strip():
        query_string = request.GET['q']
        entry_query = utils.get_query(query_string, ['title', 'body',])
        entities = Entity.objects.filter(entry_query).order_by('date_created')
        return render(request, 'search.html', { 'query_string': query_string, 'entities': entities })
    else:
        return render(request, 'search.html', { 'query_string': 'Null', 'found_entries': 'Enter a search term' })

def compare(request):
    C
    Form to compare 2 entitites
    C
    # POST
    if request.method == "POST":
        form = EntityCompareForm(request.POST)
        if form.is_valid():
            pass
            C
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
            #return render(request, 'myknowapp/compare.html', {'form': form})
            C

    # GET
    else:
        form = EntityCompareForm()
    return render(request, 'myknowapp/compare.html', {'form': form})
"""


class IndexView(generic.ListView):
    template_name = 'myknowapp/index.html'
    context_object_name = 'latest_entity_list'

    def get_queryset(self):
        """Return the last 100 entities."""
        # latest_entity_list
        return Entity.objects.order_by('-date_created')[:100]

    # Pass some extra variables to the template (implication, ...)
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        context['e_sun'] = Entity.objects.get(name='Sun')
        context['e_earth'] = Entity.objects.get(name='Earth')
        context['e_mars'] = Entity.objects.get(name='Mars')
        context['e_car'] = Entity.objects.get(name='car')
        context['e_hb'] = Entity.objects.get(name='human body')
        context['e_sts'] = Entity.objects.get(name='stellar system')
        context['e_sos'] = Entity.objects.get(name='solar system')
        context['e_love'] = Entity.objects.get(name='love')
        context['e_fear'] = Entity.objects.get(name='fear')
        context['e_fe'] = Entity.objects.get(name='fruit of the Spirit')
        return context



class DetailView(generic.DetailView):
    model = Entity
    template_name = 'myknowapp/detail.html'

    # Pass some extra variables to the template (implication, ...)
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        #obj = super().get_object()
        entity = context['entity']
        # ex: "love implies NO fear"
        # ex: "NO love implies fear"
        imp = ''
        if entity.implies:
            if entity.not_me: imp = 'NO '
            imp += entity.name + ' => '
            if entity.implies_not: imp += 'NO '
            imp += entity.implies.name
        context['implication'] = imp
        return context


'''
class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'
'''
