from django.conf.urls import url,include
from . import views
urlpatterns = [
    url(r'^home/', views.home),
    url(r'^events/', views.events),
    url(r'^gallery/', views.gallery),
    url(r'^team/', views.team),
    url(r'^alumni/', views.alumni),
    url(r'^feedback/', views.feedback1), 
    url(r'^straightoutta/', views.straightoutta),
    url(r'^alumniconnect/',views.alumniconnect),

]
