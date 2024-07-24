import webbrowser
from data_scraping import sinaweibopy3


def main():
    '''
    if you want to use this api,you should follow steps follows to operate.
    '''
    try:
        # step 1 : sign a app in weibo and then define const app key,app secret,redirect_url
        APP_KEY = '3729405214'
        APP_SECRET = '0054d25ae5c2fc0ffc382bc1c059d749'
        REDIRECT_URL = 'http://api.weibo.com/oauth2/default.html'
        # step 2 : get authorize url and code
        client = sinaweibopy3.APIClient(app_key=APP_KEY, app_secret=APP_SECRET, redirect_uri=REDIRECT_URL)
        url = client.get_authorize_url()
        # print(url)
        webbrowser.open_new(url)
        # step 3 : get Access Token
        # Copy the above address to the browser to run, 
        #enter the account and password to authorize, the new URL contains code
        result = client.request_access_token(
            input("please input code : "))  # Enter the CODE obtained in the authorized address
        print(result)
        # At this point, the access_token and expires_in should be saved,
        # because there is a validity period.A
        # If you need to send the microblog multiple times in a short time,
        # you can use it repeatedly without having to acquire it every time.
        client.set_access_token(result.access_token, result.expires_in)


    except ValueError:
        print('pyOauth2Error')

if __name__ == '__main__':
    main()

