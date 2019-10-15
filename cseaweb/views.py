from django.shortcuts import render
from cseaweb.forms import feedbackform
from django.core.mail import send_mail
from cseaweb.models import feedback
# Create your views here.
def home(request):
	return render(request,'home.html')
def events(request):
	return render(request,'events.html')
def gallery(request):
	return render(request,'gallery.html')
def team(request):
	return render(request,'team.html')
def alumni(request):
	return render(request,'alumni.html')
def feedback1(request):
	if request.method == 'POST':
		form = feedbackform(request.POST)
		if form.is_valid():
			sender = form.cleaned_data['cem']
			e_name = form.cleaned_data['event_name']
			fb = form.cleaned_data['fback']
			recipients = ['kapilrathod1234@gmail.com']
			subject = "Feedback on " + e_name
			message = fb
			send_mail(subject, message, sender, recipients) # sends to specified email
			f=feedback()
			f.cemail=sender
			f.eventname = e_name
			f.fback = fb
			f.save()

	return render(request,'feedback.html')

def straightoutta(request):
	return render(request,'straightoutta.html')

def alumniconnect(request):
	return render(request,'alumniconnect.html')
