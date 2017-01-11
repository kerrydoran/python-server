from simplerouter import Router
from webob import Response

html_file = open('home.html', 'r').read()


def respond(response):
	return Response (html_file)

router = Router()
router.add_route('/', respond)


















application = router.as_wsgi

if __name__=='__main__':
    from wsgiref.simple_server import make_server
    make_server('', 8000, application).serve_forever()

