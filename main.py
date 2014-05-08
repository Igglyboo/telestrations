#!/usr/bin/env python
import webapp2
import os
from google.appengine.ext.webapp import template
from word_generator import words

class Telestrations(webapp2.RequestHandler):
    def get(self):
        template_values = {'word_list': words(6)}
        template_path = os.path.join(os.path.dirname(__file__), 'templates/index.html')
        self.response.out.write(template.render(template_path, template_values))


app = webapp2.WSGIApplication([('/', Telestrations)], debug=False)

