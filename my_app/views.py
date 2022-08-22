from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Comment
import requests
# Create your views here.


# class IndexPageView(TemplateView):
# 	template_name = 'index.html'




def telegram_bot_sendtext(bot_message):
	bot_token = '5513853508:AAHWDQQWMK9ONElD02S_6DigxQFaxevDKU0'
	bot_chatID = '5036956072'
	send_text = 'https://api.telegram.org/bot'+bot_token+'/sendMessage?chat_id='+bot_chatID+'&parse_mode=Markdown&text='+bot_message
	response = requests.get(send_text)

	return response.json()

	
def IndexPageView(request):
	if request.method == 'POST':
		name = request.POST.get('name',None)
		email = request.POST.get('email',None)
		message = request.POST.get('message',None)
		user = Comment.objects.create(
			username = name,
			email = email,
			message = message
		)
		user.save()
		telegram_bot_sendtext(f"Ismi:{name}\nEmail:{email}\nXabar:{message}")
	return render(
	request=request,
	template_name = 'index.html'
	)