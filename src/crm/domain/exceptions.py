class AppBaseException(Exception):
    status_code = 400


class UnauthorizedException(AppBaseException):
    status_code = 401


class BadRequestException(AppBaseException):
    pass


class AlreadyExistsException(AppBaseException):
    status_code = 409


class NotFoundException(AppBaseException):
    status_code = 404


class ForbiddenException(AppBaseException):
    status_code = 403
