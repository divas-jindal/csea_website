from django.shortcuts import render, redirect
from cseaweb.forms import contactForms
from django.http.response import Http404
from django.core.mail import send_mail
from cseaweb.models import feedback
from django.conf import settings
from django.http import HttpResponseRedirect
from .cpl_teams import teams_data as td

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
	# context = {}
	next = '/'
	if request.method == 'POST':
		form = contactForms(request.POST)

		print("cp1")
		if form.is_valid():
			print("cp2")
			f = form.save(commit=False)
			f.save()
			next = request.POST.get('next', '/')
			print("path: " + next)
			name = form.cleaned_data['name']
			comment = form.cleaned_data['comment']
			to_email = form.cleaned_data['email']
			#Acknowledgement mail to sender
			subject='Message from CSEA NIT Warangal'
			message = 'Hey ' + name + ',\n\n' + 'Hope you are safe and doing well.\n\n' + \
			'Thank you for contacting us. We will get back to you soon.\n\n\n' + \
			'Best Regards,\n\n' + \
			'Divas Jindal\n'+ \
			'General Secretary\n'+ \
			'CSEA NIT Warangal'
			recipient_list = [to_email]
			email_from = settings.EMAIL_HOST_USER
			send_mail(subject, message, email_from, recipient_list)
			print(email_from)
			#Mail to Admin
			subject = 'CSEA feeback Received'
			message = '%s \nName : %s \nEmail ID : %s' %(comment,name, to_email)
			recipient_list = [email_from]
			send_mail(subject, message, email_from, recipient_list)
			print("hey")
			# title = 'Thanks'
			# context = {'title':title,'form':form,'msg':msg,}

	return HttpResponseRedirect(next)


def intoTheCSED(request):
	return render(request,'intoTheCSED.html')

# def alumniconnect(request):
# 	return render(request,'alumniconnect.html')

def talksWithCsea(request):
	return render(request,'talksWithCsea.html')

def card(request):
	return render(request,'card.html')

def cpl(request):
	return render(request,'CPL/main.html',{'teams':td.TEAMS})

def teams(request,code):
    itr = int(code)
    itr_temp = 0
    for team in td.TEAMS:
        itr_temp += 1
        if(itr_temp == itr):
            return render(request,'CPL/teams.html',{'team':td.TEAMS[team],'name':team,'letter':int(team,2)})
    raise Http404('Invalid Team ID')