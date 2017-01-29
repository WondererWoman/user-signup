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

class Signup(webapp2.RequestHandler):
    def get(self):

        signup_header = "<h2>User Signup</h2>"

        info_form = """
        <form method="post">
            <label>
            Username:
            <input type="text" name="name"/>
            </label>
            <br> <br>
            <label>
            Password:
            <input type="password" name="password"/>
            </label>
            <br> <br>
            <label>
            Verify Password:
            <input type="password" name="verify"/>
            </label>
            <br> <br>
            <label>
            Email(optional)
            <input type="text" name="email"/>
            </label>
            <br> <br>
            <input type="submit" value="Submit">
        </form>
        """
        content = page_header + signup_header + info_form + page_footer
        self.response.write(content)

    def post(self):
        user_name = valid_un(self.request.get("name"))
        user_password = valid_password(self.request.get("password"))
        user_validation = valid_password(self.request.get("verify"))
        user_email = valid_email(self.request.get("email"))

        

app = webapp2.WSGIApplication([
    ('/', Signup)
], debug=True)
