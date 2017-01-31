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

info_form = """
<form method="post">
    <label>
    Username:
    <input type="text" name="name"/>
    <div class="error">{error_username}</div>
    </label>
    <br> <br>
    <label>
    Password:
    <input type="password" name="password"/>
    <div class="error">{error_password}</div}
    </label>
    <br> <br>
    <label>
    Verify Password:
    <input type="password" name="verify"/>
    <div class="error">{error_verify}</div>
    </label>
    <br> <br>
    <label>
    Email(optional)
    <input type="text" name="email"/>
    <div class="error">{error_email}</div>
    </label>
    <br> <br>
    <input type="submit" value="Submit">
</form>
"""

def valid_un(name):
    USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    return USER_RE.match(name)


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

        content = page_header + signup_header + info_form + page_footer
        self.response.write(content)

    def post(self):
        user_name = valid_un(self.request.get("name"))
        user_match = valid_match( self.request.get("password"), self.request.get("verify") )
        user_email = valid_email(self.request.get("email"))
        user_password = valid_password(self.request.get("password"))

        if not (user_name and user_password and user_email and user_match):
            self.response.write(signup_header + info_form)
        else:
            self.response.write("<div style='color:red;'>Thanks!</div>")

app = webapp2.WSGIApplication([
    ('/', Signup)
], debug=True)
