from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from artist.models import User,Profile

from twilio.rest import Client
from twilio.jwt.access_token import AccessToken
from twilio.jwt.access_token.grants import (
    SyncGrant,
    ChatGrant
)


# Create your views here.
def app(request):
    return render(request, 'twilio/index.html')

def token(request):
    return generateToken(request.user.username or 'anonymous')

def userJoin(request):
    if request.user.is_authenticated:
        if request.user.profile.is_client:
            Profile.objects.filter(pk=request.user.profile.pk).update(is_in_Chat=True)

    if len(Profile.objects.filter(is_in_Chat=True))>0:
        return JsonResponse({'isInChat':'true'})
    else:
        return JsonResponse({'isInChat':'false'})


def userLeaves(request):
    if request.user.is_authenticated:
        if request.user.profile.is_client:
            Profile.objects.filter(pk=request.user.profile.pk).update(is_in_Chat=False)
            return JsonResponse({'left':f"Admin {request.user.username}"})

        return JsonResponse({'left':request.user.username})
    return JsonResponse({'left':'anonymous'})

def generateToken(identity):
    # Get credentials from environment variables
    account_sid      = settings.TWILIO_ACCT_SID
    chat_service_sid = settings.TWILIO_CHAT_SID
    sync_service_sid = settings.TWILIO_SYNC_SID
    api_sid          = settings.TWILIO_API_SID
    api_secret       = settings.TWILIO_API_SECRET
    print(account_sid)
    print(chat_service_sid)
    print(sync_service_sid)
    print(api_sid)
    print(api_secret)
    # Create access token with credentials
    token = AccessToken(account_sid, api_sid, api_secret, identity=identity)
    print(token)

    # Create a Sync grant and add to token
    if sync_service_sid:
        sync_grant = SyncGrant(service_sid=sync_service_sid)
        token.add_grant(sync_grant)

    # Create a Chat grant and add to token
    if chat_service_sid:
        chat_grant = ChatGrant(service_sid=chat_service_sid)
        token.add_grant(chat_grant)

    # Return token info as JSON
    return JsonResponse({'identity':identity,'token':token.to_jwt()})