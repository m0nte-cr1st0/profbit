from django.db import connection


def connection_to_db(request):
    return {"connection": connection}
