#!/usr/bin/env python3
""" SessionDBAuth module """
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """ SessionDBAuth class for session management using database """

    def create_session(self, user_id=None):
        """ Create and store a new session in the database """
        session_id = super().create_session(user_id)
        if not session_id:
            return None

        # Create and save the UserSession instance
        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """ Retrieve a user ID from the session database """
        if not session_id:
            return None

        # Retrieve the UserSession object from the database
        user_session = UserSession.search({'session_id': session_id})
        if not user_session:
            return None
        return user_session[0].user_id  # Assuming search returns a list

    def destroy_session(self, request=None):
        """ Destroy a session by removing it from the database """
        if not request:
            return False

        session_id = self.session_cookie(request)
        if not session_id:
            return False

        # Find and delete the UserSession object
        user_sessions = UserSession.search({'session_id': session_id})
        if not user_sessions:
            return False
        for session in user_sessions:
            session.remove()
        return True
