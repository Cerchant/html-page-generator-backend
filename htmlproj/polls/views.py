from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse, JsonResponse


def index(request):
    user = request.user
    list_of_templates = Templates.objects.filter(user=user)

    return redirect('', {'user': user, 'list_of_templates': list_of_templates})


def delete_template(request):
    template_id = request.GET.get('template_id')
    status = 200
    print('input', str(template_id))
    try:
        Templates.objects.filter(id=template_id).delete()
        print('deleted')
    except:
        print('fail')
        status = 400
    return JsonResponse({'status': status, })

def get_card(request):
    template_id = request.GET.get('template_id')
    exist = Templates.objects.filter(id=template_id)[0]
    if exist:
        HTML_text = exist.HTML_page
    else:
        HTML_text = ''
    return JsonResponse({'text': HTML_text, })

