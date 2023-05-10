import json


# Any GCal methods need to be passed the request and oauth from views.py


# Returns a user's google account events as a dictionary
def getGCal(request, oauth):
    user = request.session.get("user")
    token = request.session.get("token")
    email = user["email"]
    url = "https://www.googleapis.com/calendar/v3/calendars/%s/events" % email
    resp_bytes = oauth.google.get(
        url=url,
        token=token,
        request=request,
    ).content
    resp_str = resp_bytes.decode("utf-8")
    resp = json.loads(resp_str)
    print(type(resp))
    return resp


# Pass through an event string such as "Appointment at Location from 10:30-12:00"
def addGCalEvent(request, oauth, event):
    user = request.session.get("user")
    token = request.session.get("token")
    email = user["email"]
    url = "https://www.googleapis.com/calendar/v3/calendars/%s/events/quickAdd" % email
    return oauth.google.post(
        url=url,
        token=token,
        request=request,
        json={
            "text": event,
        },
    ).content
