from django.http import JsonResponse
from .models import *


def new_room(request):
    room = Room()
    room.save()
    data = {
        'code': room.id
    }
    return JsonResponse(data)


def main(request, code):
    room = Room.objects.all().filter(id=str(code))[0]
    if room:
        users = {}
        for user in User.objects.all().filter(room=room):
            users[user.id] = user.email
        data = {
            'users': users
        }
    else:
        data = {
            'error': 'Wrong room number'
        }
    return JsonResponse(data)


def new_user(request):
    print('request', request.GET)
    room = Room(id=request.GET['code'])
    user = User(email=request.GET['email'], room=room)
    user.save()
    calendar = Calendar(room=room, url=request.GET['url'])
    calendar.save()
    users = {}
    for user in User.objects.all().filter(room=room):
        users[user.id] = user.email
    data = {
        'users': users
    }
    return JsonResponse(data)


def get_times(request):
    room = Room.objects.all().filter(id=request.GET['code'])[0]
    users = User.objects.all().filter(room=room)
    if len(users) == 1:
        data = {
            'error': 'Only one user!'
        }
    else:
        calendars = Calendar.objects.all().filter(room=room)
        times = process_calendars(calendars[0], calendars[1])
        data = {
            'times': times
        }
    return JsonResponse(data)


def process_calendars(calendar1, calendar2):
    pass
