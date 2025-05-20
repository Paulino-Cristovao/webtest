import os
import openai
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

openai.api_key = os.getenv('OPENAI_API_KEY')

@csrf_exempt
def chat_api(request):
    user_msg = request.POST.get('message')
    resp = openai.ChatCompletion.create(
        model='gpt-4o-mini',
        messages=[{'role':'user','content':user_msg}]
    )
    return JsonResponse({'reply': resp.choices[0].message.content})