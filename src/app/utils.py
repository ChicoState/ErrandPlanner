# Returns a user's google account events as a dictionary
def getGCal(request, oauth):
    user = request.session.get("user")
    token = request.session.get("token")
    email = user["email"]
    url = "https://www.googleapis.com/calendar/v3/calendars/%s/events" % email
    return oauth.google.get(url=url, token=token, request=request).content
