from django.conf import settings # import the settings file

def twitter_link(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'TWITTER_LINK': settings.TWITTER_LINK}

def github_link(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'GITHUB_LINK': settings.GITHUB_LINK}

def linkedin_link(request):
    # return the value you want as a dictionnary. you may add multiple values in there.
    return {'LINKEDIN_LINK': settings.LINKEDIN_LINK}