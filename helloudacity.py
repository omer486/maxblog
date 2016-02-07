import webapp2
import cgi

rot13_form= """
<form method="post"> 

<textarea name="text" id="rot13" cols="45" rows="5">%(cipher)s</textarea>

  <p>
    <input type="submit" name="button" id="button" value="Submit" />
  </p>

  </form>

"""

def rot_13(text):
	rt=""
	for c in text:
	    temp=ord(c)
	    if (temp >= ord('A')) and (temp <= ord('Z')):
	    	temp = ((temp - ord('A') + 13) % 26 + ord('A'))

	    if (temp >= ord('a')) and (temp <= ord('z')):
	    	temp = ((temp - ord('a') + 13) % 26 + ord('a'))	  

	    rt=rt+ chr(temp) 
	return rt    	

def escape_html(s):
	return cgi.escape(s,quote=True)


sign_up_html = """
  <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Sign Up</title>
<style type="text/css">

.label {
  margin: 0px;
  width: 110px;
  padding: 0px;
  float: left;
}

</style>
</head>

<body>
<form id="form1" name="form1" method="post" >
  <p>
  <div class="label"> <label for="name">Name</label> </div>
    <input type="text" name="username" id="name"   value="%(username)s" /> %(user_error)s
  </p>
  <p>
    <div class="label"><label for="password">Password</label></div>
    <input type="password" name="password" id="password" />  %(pass_error)s
  </p>
  <p>
    <div class="label"><label for="Verify">verify password</label></div>
    <input type="password" name="verify" id="verify" />  %(verify_error)s
  </p>
  <p>
    <div class="label"><label for="Email">email (optional)</label></div>
    <input type="text" name="email" id="Email"  value="%(email)s" />  %(email_error)s
  </p>

   <p>
      
    <input type="submit" name="button" id="button" value="Submit" />
  </p>
</form>
</body>
</html>
"""






class MainPage(webapp2.RequestHandler):
  def get(self):
      self.response.headers['Content-Type'] = 'text/plain'
      self.response.out.write('Hello, Udacity!') 

class rot13(webapp2.RequestHandler):

  def write_form(self,form,cipher=""):
    self.response.out.write(form %{"cipher": cipher})
       
  
  def get(self):     
    #self.response.out.write(rot13_form, %{"cipher": """"})
    self.write_form(rot13_form)

  def post(self):
  	text = self.request.get('text')
  	text=escape_html(text)
  	text=rot_13(text)
  	#self.response.out.write(text)
  	self.write_form(rot13_form,text)


class sign_up(webapp2.RequestHandler):

  def write_html(self,sign_up_html,username="",email="",user_error="", pass_error="", email_error="", verify_error=""):
    self.response.out.write(sign_up_html %{"username": username, "email": email, "user_error":user_error, \
     "pass_error":pass_error, "email_error":email_error, "verify_error":verify_error })

  def get(self):     
    self.write_html(sign_up_html)  

  def post(self):

    flag=False;

    user_error=""; pass_error="";  email_error=""; verify_error=""

    import re
    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    def valid_username(username):
      return USER_RE.match(username)

    PASS_RE = re.compile(r"^.{3,20}$")
    def valid_password(password):
      return PASS_RE.match(password)  

    EMAIL_RE = re.compile(r"^[\S]+@[\S]+\.[\S]+$")
    def valid_email(email):
      return EMAIL_RE.match(email)    

    username = self.request.get('username')
    password = self.request.get('password')
    verify = self.request.get('verify')
    email = self.request.get('email')


    if (not valid_username(username)):
       user_error="That's not a valid username."
       flag=True

    if (not valid_password(password)):
       pass_error="That's not a valid password."
       flag=True   

    if not (valid_email(email) or email ==""):
       email_error="That's not a valid email."
       flag=True 

    if (verify != password):
      verify_error= "Your passwords did not match"
      flag =True
    


    username=escape_html(username); password=escape_html(password); verify=escape_html(verify)
    if flag:
      self.write_html(sign_up_html,username,email,user_error,pass_error, email_error, verify_error)  
    else:
      self.redirect("/welcome?username="+username) 


class welcome (webapp2.RequestHandler):
  def get(self):
      username = self.request.get('username')
      self.response.out.write('Welcome, %s!' %username) 

  






app = webapp2.WSGIApplication([('/', MainPage), ('/rot13', rot13), ('/sign_up', sign_up), ('/welcome', welcome)], debug=True)