#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import re


page_header = """
<!DOCTYPE html>
<html>
<head>
    <title>User Signup</title>
    <style type="text/css">
        .error {
            color: red;
        }
    </style>
</head>
<body>

"""


# html boilerplate for the bottom of every page
page_footer = """
</body>
</html>
"""
signup_header = "<h2>User Signup</h2>"

def build_form(username, myemail, error_username, error_password, error_verify, error_email):
    info_form = """
    <form action="/" method="post">
        <label>
        Username:
        <input type="text" name="name" value="%(username)s">
        <div class="error">%(error_username)s</div>
        </label>
        <br> <br>
        <label>
        Password:
        <input type="password" name="password"/>
        <div class="error">%(error_password)s</div>
        </label>
        <br> <br>
        <label>
        Verify Password:
        <input type="password" name="verify"/>
        <div class="error">%(error_verify)s</div>
        </label>
        <br> <br>
        <label>
        Email(optional):
        <input type="text" name="email" value="%(myemail)s">
        <div class="error">%(error_email)s</div>
        </label>
        <br> <br>
        <input type="submit" value="Submit">
    </form>
    """
    form_data = {
    'username' : username,
    'myemail' : myemail,
    'error_email' : error_email,
    'error_verify' : error_verify,
    'error_username' : error_username,
    'error_password' : error_password
    }
    html = info_form % form_data
    return html

def valid_un(name):
    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    return not not USER_RE.match(name)

def valid_match(password, verify):
    Password_RE = re.compile("^.{3,20}$")
    return (password == verify)

def valid_password(password):
    Password_RE = re.compile("^.{3,20}$")
    return Password_RE.match(password)


def valid_email(email):
    email_RE = re.compile("^[\S]+@[\S]+.[\S]+$")
    return email_RE.match(email)

class Signup(webapp2.RequestHandler):
    def get(self):
        content = page_header + signup_header + build_form(username="", myemail="", error_username="", error_password="", error_verify="", error_email="") + page_footer
        self.response.write(content)

    def post(self):
        username1 = valid_un(self.request.get("name"))
        user_match = valid_match( self.request.get("password"), self.request.get("verify") )
        user_email = valid_email(self.request.get("email"))
        user_password = valid_password(self.request.get("password"))
        name = self.request.get("name")
        email = self.request.get("email")
        #username = self.request.get("name")

        error_username = ""
        if username1:
            error_username += ""
        else:
            error_username += "That is not a valid username"

        error_password = ""
        if user_password:
            error_password += ""
        else:
            error_password += "That is not a valid password"

        error_verify = ""
        if user_match:
            error_verify += ""
        else:
            error_verify += "Your passwords do not match"

        error_email = ""
        if user_email:
            error_email += ""
        elif email == "":
            error_email += ""
            user_email = True
        else:
            error_email += "That is not a valid email"

        if username1 and user_match and user_password and user_email:
            self.redirect('/welcome?name=' + name)

        else:
            error_reply = build_form(name, email, error_username, error_password, error_verify, error_email)
            self.response.write(page_header + signup_header + error_reply + page_footer)

class Welcome(webapp2.RequestHandler):
    def get(self):
        username = self.request.get('name')
        if valid_un(username):
            self.response.write("Welcome " + username + "!")
        else:
            self.redirect('/Signup')


app = webapp2.WSGIApplication([
    ('/', Signup),
    ('/welcome', Welcome)
], debug=True)
