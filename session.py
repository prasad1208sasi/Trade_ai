sessions = {}

def track_session(user):
    sessions[user] = sessions.get(user, 0) + 1