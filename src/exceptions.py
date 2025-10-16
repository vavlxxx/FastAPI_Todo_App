from fastapi import HTTPException, status


class BaseHTTPError(HTTPException):
    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    detail = "Internal Server Error"

    def __init__(self, *args, **kwargs):
        exc_detail = self.detail
        if "detail" in kwargs:
            exc_detail = kwargs["detail"]
        super().__init__(status_code=self.status_code, detail=exc_detail)


class NotFoundHTTPError(BaseHTTPError):
    status_code = 404
    detail = "Object not found"


class AlreadyExistsHTTPError(BaseHTTPError):
    status_code = 409
    detail = "Object already exists"


class TodoNotFoundHTTPError(NotFoundHTTPError):
    detail = "Todo with supplied ID not exists."


class TodoAlreadyExistsHTTPError(AlreadyExistsHTTPError):
    detail = "Todo with supplied ID already exists."
