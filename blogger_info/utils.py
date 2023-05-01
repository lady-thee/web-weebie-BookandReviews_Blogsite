# THIS py FILE IS USED TO CREATE TOKENS THAT WE CAN USE ONE TIME 
# _make_hash_value gives a way to create token and verifies if the token has changed
# depending on the return of the hash_value
#To create a hash we need some utilities to ensure that the hash is compatible using six


import six 
from django.contrib.auth.tokens import PasswordResetTokenGenerator


class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return six.text_type(user.pk)+six.text_type(timestamp)+six.text_type(user.is_email_verified)
    



generator_token = TokenGenerator()