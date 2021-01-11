from django.conf.urls import url,include
from django.views.generic.base import RedirectView
from . import views
urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/home/')),
    url(r'^home/', views.home,name='home'),
    url(r'^events/', views.events,name='events'),
    url(r'^gallery/', views.gallery,name='gallery'),
    url(r'^team/', views.team,name='team'),
    url(r'^alumni/', views.alumni,name='alumni'),
    url(r'^feedback/', views.feedback1,name='feedback'), 
    url(r'^intoTheCSED/', views.intoTheCSED,name='intoTheCSED'),
    url(r'^straightoutta',views.intoTheCSED,name='straightoutta'),
    url(r'^talksWithCsea/',views.talksWithCsea,name='talksWithCsea'),
    url(r'^card/',views.card,name='card'),
    url(r'cpl/$',views.cpl,name='cpl'),
    url(r'^cpl/(?P<code>[0-9]{1,})/$',views.teams,name='teams')
]
