"""This module runs the application."""
from models import api, app
from models.views import PersonResource


api.add_resource(PersonResource, '/api', '/api/<string:user_id>')

@app.errorhandler(404)
def handle_invalid_route(error):
    """
    Returns a http 404 error code and message when a wrong
    url is used by the client.
    """
    return {'error': str(error)}, 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
