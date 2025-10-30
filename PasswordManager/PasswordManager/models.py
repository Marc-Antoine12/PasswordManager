from django.db import models
from django.contrib.auth.models import User
from cryptography.fernet import Fernet
from django.conf import settings
import base64


class Password(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='stored_passwords')
    title = models.CharField(max_length=200, help_text="Service or website name")
    username = models.CharField(max_length=200, blank=True, null=True)
    password = models.TextField()  # Will store encrypted password
    url = models.URLField(max_length=500, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} - {self.user.username}"

    def set_password(self, raw_password):
        """Encrypt and store the password"""
        key = self._get_encryption_key()
        fernet = Fernet(key)
        encrypted_password = fernet.encrypt(raw_password.encode())
        self.password = base64.urlsafe_b64encode(encrypted_password).decode()

    def get_password(self):
        """Decrypt and return the password"""
        try:
            key = self._get_encryption_key()
            fernet = Fernet(key)
            encrypted_password = base64.urlsafe_b64decode(self.password.encode())
            return fernet.decrypt(encrypted_password).decode()
        except:
            return "Unable to decrypt password"

    def _get_encryption_key(self):
        """Generate encryption key from Django secret key"""
        # Use Django's SECRET_KEY to generate a consistent encryption key
        secret_key = settings.SECRET_KEY.encode()
        # Take first 32 bytes and base64 encode for Fernet
        key_bytes = secret_key[:32].ljust(32, b'0')  # Pad to 32 bytes if needed
        return base64.urlsafe_b64encode(key_bytes)

