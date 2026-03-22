# copy-auth-header
This Burp plugin allow copy all authentication headers by one click . While you are testing for IDOR vulnerabilites you always need to copy the auth headers from one account to another and this burp basically serach for 4 auth headers (from my expierence on pentesting ) :
- cookie
- x-api-key
- x-auth-key
- authorization

and you can edit it and add whatever header you want

# Install 

- download the python file of this repo either by git clone or copy and paste to local file
- Go to Extensions tab and on extension settings ensure you load the Jython jar file with the latest stand alone version
- go back to extension tab and click add and on extension type select python
- select the file you downloaded before and you are ready to go

# Usage 
- on any request from account 1 without mark any strings just right click on the request and select extension => copy-auth-header
- now on the repeater request from account 2 just mark the auth headers and click paste 
