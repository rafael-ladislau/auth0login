# auth0login/auth0backend.py

from six.moves.urllib import request
from jose import jwt
from social_core.backends.oauth import BaseOAuth2
import logging

log = logging.getLogger(__name__)

class Auth0(BaseOAuth2):
    """Auth0 OAuth authentication backend"""
    name = 'auth0'
    SCOPE_SEPARATOR = ' '
    ACCESS_TOKEN_METHOD = 'POST'
    EXTRA_DATA = [
        ('picture', 'picture')
    ]

    def authorization_url(self):
        return 'https://' + self.setting('DOMAIN') + '/authorize'

    def access_token_url(self):
        return 'https://' + self.setting('DOMAIN') + '/oauth/token'

    def get_user_id(self, details, response):
        """Return current user id."""

        log.warn("details " + str(details))
        return details['email']

    def get_user_details(self, response):
        # Obtain JWT and the keys to validate the signature
        id_token = response.get('id_token')
        jwks = request.urlopen('https://' + self.setting('DOMAIN') + '/.well-known/jwks.json')
        issuer = 'https://' + self.setting('DOMAIN') + '/'
        audience = self.setting('KEY')  # CLIENT_ID
        payload = jwt.decode(id_token, jwks.read(), algorithms=['RS256'], audience=audience, issuer=issuer)
        log.warn("payload " + str(payload))
        log.warn("response " + str(response))
        return {'username': payload['nickname'],
                'email': payload['name'],
                'fullname': payload['https://openid.org/user_metadata']["first_name"] + " " + payload['https://openid.org/user_metadata']["last_name"],
                'first_name': payload['https://openid.org/user_metadata']["first_name"],
                'last_name': payload['https://openid.org/user_metadata']["last_name"]
                }
