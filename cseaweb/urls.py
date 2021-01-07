from django.conf.urls import url,include
from django.views.generic.base import RedirectView
from . import views
urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/home/')),
    url(r'^home/', views.home),
    url(r'^events/', views.events),
    url(r'^gallery/', views.gallery),
    url(r'^team/', views.team),
    url(r'^alumni/', views.alumni),
    url(r'^feedback/', views.feedback1), 
    url(r'^intoTheCSED/', views.intoTheCSED),
    url(r'^straightoutta',views.intoTheCSED),
    url(r'^talksWithCsea/',views.talksWithCsea),
    url(r'^card/',views.card)

]
