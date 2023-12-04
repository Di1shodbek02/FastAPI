from fastapi_users.authentication import CookieTransport, AuthenticationBackend, JWTStrategy

cookie_transport = CookieTransport(cookie_name='bonds', cookie_max_age=3600)

SECRET = 'd5850570ccfd2d686beb4c87226b19a516ba8b6501f70f753820ef8ce33b6fd2'


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name='jwt',
    transport=cookie_transport,
    get_strategy=get_jwt_strategy,
)
