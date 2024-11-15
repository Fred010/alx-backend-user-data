#!/usr/bin/env python3
"""
SessionExpAuth class for managing session expiration.
"""
from datetime import datetime, timedelta
from os import getenv
from api.v1.auth.session_auth import SessionAuth


class SessionExpAuth(SessionAuth):
    """SessionExpAuth class inheriting from SessionAuth."""

    def __init__(self):
        """Initialize the instance with session duration."""
        try:
            self.session_duration = int(getenv('SESSION_DURATION', 0))
        except ValueError:
            self.session_duration = 0

    def create_session(self, user_id=None):
        """
        Create a session with an expiration time.
        """
        session_id = super().create_session(user_id)
        if not session_id:
            return None

        # Add a session dictionary with user_id and created_at
        self.user_id_by_session_id[session_id] = {
            "user_id": user_id,
            "created_at": datetime.now()
        }
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """
        Retrieve the user_id from the session dictionary.
        """
        if session_id is None:
            return None

        session_data = self.user_id_by_session_id.get(session_id)
        if not session_data:
            return None

        user_id = session_data.get("user_id")
        created_at = session_data.get("created_at")
        if not created_at or not isinstance(created_at, datetime):
            return None

        if self.session_duration <= 0:
            return user_id

        # Check if the session has expired
        if created_at + timedelta(
                seconds=self.session_duration) < datetime.now():
            return None

        return user_id
