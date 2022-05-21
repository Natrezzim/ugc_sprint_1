import jwt
from fastapi import HTTPException

from core.config import Settings

settings = Settings()


class Auth:
    secret = settings.jwt_secret

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=['HS256'])
            if (payload['type'] == 'access'):
                return payload['sub']
            raise HTTPException(status_code=401, detail='Scope for the token is invalid')
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Token expired')
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail='Invalid token')
