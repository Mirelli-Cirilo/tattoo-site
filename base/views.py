from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	if request.method == "POST":
		message_name = request.POST['message-name']
		message_email = request.POST['message-email']
		message = request.POST['message']

		# send an email
		send_mail(
			message_name, # subject
			message, # message
			message_email, # from email
			['TanaHora1661@gmail.com'], # To Email
			)
		
		send_mail(
			'Hiago Tatto', # subject
			'Olá', # message
			'TanaHora1661@gmail.com', # from email
			[message_email,], # To Email
			)
		

		return render(request, 'home.html', {'message_name': message_name})

	else:
		return render(request, 'home.html')

