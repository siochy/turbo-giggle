
def app(environ, start_response):
    headers = [('Content-Type', 'text/plain')]
    path = environ['PATH_INFO'].lower()
    query = environ['QUERY_STRING'].lower()
    if '307' in path or '307' in query:
        status = '307 Temporary Redirect'
    elif '400' in path or '400' in query:
        status = '400 Bad Request'
    elif '403' in path or '403' in query:
        status = '403 Forbidden'
    elif '404' in path or '404' in query:
        status = '404 Not Found'
    elif '500' in path or '500' in query:
        status = '500 Internal Server Error'
    else:
        status = '200 OK'
    start_response(status, headers)
    return [status.encode('utf-8')]
