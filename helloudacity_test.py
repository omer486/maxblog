import webapp2

#rot13_form= """
#<form method=”post”> 

#<textarea name="text" id="rot13" cols="45" rows="5"></textarea>

"""

class MainPage(webapp2.RequestHandler):
  def get(self):
      self.response.headers['Content-Type'] = 'text/plain'
      self.response.out.write('Hello, Udacity!') 

class rot13(webapp2.RequestHandler):
  def get(self):     
    self.response.out.write(rot13_form)

  def post(self):
  	self.response.out.write(rot13_form)
  

     

app = webapp2.WSGIApplication([('/', MainPage), ('/rot13', rot13)],
                              debug=True)