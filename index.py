import os
import webapp2
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
        loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
        extensions=['jinja2.ext.autoescape'],
        autoescape=True)


class MainPage(webapp2.RequestHandler):
    def get(self):
        template_values = {
            'msg': "e-gaav application under development",
            'title': 'e-gaav under development'
        }
        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))


app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
