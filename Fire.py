from json import dumps
from kivy.network.urlrequest import UrlRequest
from add_user import add_user_to_db,get_user_info

# Firebase Project meta info - MUST BE CONFIGURED BY DEVELOPER
web_api_key ="AIzaSyC61oXg5fBWi_cFGz7lHGqZfyqHHdnH0v8"  # From Settings tab in Firebase project

# Firebase Authentication Credentials - what developers want to retrieve
refresh_token = ""
localId = ""
idToken = ""
debug = False
email=""
ename=""
ecity=""
def sign_up(mail,password,name,city):
    """If you don't want to use Firebase, just overwrite this method and
    do whatever you need to do to sign the user up with their email and
    password.
    """
    global email,ename,ecity
    email,ename,ecity=mail,name,city


    print("Attempting to create a new account: ", email, password)
    signup_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key=" + web_api_key
    signup_payload = dumps(
        {"email": email, "password": password, "returnSecureToken": "true"})

    UrlRequest(signup_url, req_body=signup_payload,
                on_success=successful_login,
                on_failure=sign_up_failure,
                on_error=sign_up_error)

def successful_login(self,urlrequest):
    idToken = urlrequest['idToken']
    localId = urlrequest['localId']
    add_user_to_db(localId,idToken,email,ename,ecity)

    
    
    
# def add_db(mail,name,City):
#     print()
    

def successful_signin(self,urlrequest):
    global debug 

    #print(urlrequest)
    localId = urlrequest['localId']
    get_user_info(localId)
    print("succes sign in")

    debug=True
    print("inside",debug)


def change(self):
    print(debug)
    if debug==False:
        self.toHome()
    else:
        print("error")
        
def sign_up_failure(self, urlrequest):
    """Displays an error message to the user if their attempt to log in was
    invalid.
    """
    print("faillure")
def sign_up_error(self, *args):
    print("error")

def sign_in(self,email, password):
        """Called when the "Log in" button is pressed.

        Sends the user's email and password in an HTTP request to the Firebase
        Authentication service.
        """
        sign_in_url = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=" + web_api_key
        sign_in_payload = dumps(
            {"email": email, "password": password, "returnSecureToken": True})


        UrlRequest(sign_in_url, req_body=sign_in_payload,
                   on_success=successful_signin,
                   on_failure=sign_in_failure,
                   on_error=sign_in_error)



def sign_in_failure(self, urlrequest):
    print("faillure")

def sign_in_error(self, *args):
    print("error")
