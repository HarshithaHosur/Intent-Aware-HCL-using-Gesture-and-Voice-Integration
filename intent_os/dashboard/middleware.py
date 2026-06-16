from django.shortcuts import redirect
import sys
import os

# Add parent directory to path to import db.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from db import settings_collection

class FaceAuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # Only check authenticated users
        if not request.user.is_authenticated:
            return None

        # Exclude admin panel and static assets
        if request.path.startswith('/admin/') or request.path.startswith('/static/'):
            return None

        # Exclude specific views to avoid redirect loops
        resolver_match = request.resolver_match
        if resolver_match:
            url_name = resolver_match.url_name
            if url_name in ['login', 'signup', 'custom_logout', 'face_register', 'face_verify', 'api_face_status']:
                return None

        username = request.user.username
        
        # Check if user has registered a face
        face_doc = settings_collection.find_one({"key": "user_face", "username": username})
        if not face_doc:
            # Face not registered -> redirect to register
            return redirect('face_register')

        # Check if face verification is successful for this session
        if not request.session.get('face_verified', False):
            # Face registered but not verified -> redirect to verify
            return redirect('face_verify')

        return None
