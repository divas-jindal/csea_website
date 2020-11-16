from django.shortcuts import render
from cseaweb.forms import contactForms
from django.core.mail import send_mail
from cseaweb.models import feedback
from django.conf import settings
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
	print("cp0")
	if request.method == 'POST':
		form = feedbackform(request.POST)
		print("cp1")
		if form.is_valid():
			print("cp2")
			name = form.cleaned_data['name']
			comment = form.cleaned_data['comment']
			subject='Message from www.cseanitw.in'
			message = '%s %s' %(comment,name)
			emailFrom=form.cleaned_data['email']
			emailTo = ['divasjindal@gmail.com']
			send_mail(subject,message,emailFrom,emailTo,fail_silently=True,)
			title = 'Thanks'
			msg = 'We will get right back to you..'
			form = None
			f.email=sender
			f.name = name
			f.comment = comment
			f.save()
			print("hey")

	context = {'title':title,'form':form,'msg':msg,}
	template = 'home.html'
	return render(request,template,context)

def straightoutta(request):
	return render(request,'straightoutta.html')

def alumniconnect(request):
	return render(request,'alumniconnect.html')

def talksWithCsea(request):
	return render(request,'talksWithCsea.html')

def card(request):
	return render(request,'card.html')
