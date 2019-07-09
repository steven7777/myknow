from django.urls import path

from . import views

# Application namespace
app_name = 'myknowapp'
urlpatterns = [

    # ex: /myknowapp/
    # (classic) function view:
    #path('', views.index, name='index'),
    # Generic view:
    path('', views.IndexView.as_view(), name='index'),
    #path('', HomePageView.as_view(), name='home'),

    #path('search/', views.search, name='search')
    path('search/', views.SearchSubmitView.as_view(), name='search'),
    path('search_results/', views.SearchResultsView.as_view(), name='search_results'),

    #path('compare/', views.compare, name='compare')
    path('compare/', views.CompareSubmitView.as_view(), name='compare'),
    path('compare_results/', views.CompareResultsView.as_view(), name='compare_results'),

    # ex: /myknowapp/5/
    # (classic) function view:
    #path('<int:entity_id>/', views.detail, name='detail'),
    # Generic view:
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    path('about/', views.AboutView.as_view()),


    # ex: /myknowapp/5/results/
    #path('<int:entity_id>/results/', views.results, name='results'),
    ##path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),

    # ex: /myknowapp/5/vote/
    #path('<int:entity_id>/vote/', views.vote, name='vote'),
    ##path('<int:question_id>/vote/', views.vote, name='vote'),

]
