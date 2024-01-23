from typing import Optional

from fastapi import  Request
from fastapi_users import BaseUserManager, IntegerIDMixin, models, schemas, exceptions

from .database import User

SECRET = 'd5850570ccfd2d686beb4c87226b19a516ba8b6501f70f753820ef8ce33b6fd2'


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET
    verification_token_secret = SECRET

    async def on_after_register(
            self, user: models.UP, request: Optional[Request] = None
    ) -> None:
        print(f'{user.id} has registered')

    async def create(
            self,
            user_create: schemas.UC,
            safe: bool = False,
            request: Optional[Request] = None,
    ) -> models.UP:
        await self.validate_password(user_create.password, user_create)

        existing_user = await self.user_db.get_by_email(user_create.email)

        if existing_user is not None:
            raise exceptions.UserAlreadyExists()

        user_dict = (
            user_create.create_update_dict()
            if safe
            else user_create.create_update_dict_superuser()
        )
