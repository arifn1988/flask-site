# flask-site

I have made a simple website to where you can enter a xml link from the internet into it, and then it will read the link and grab the title , 
date and text from the xml and print it for you onto the screen. 
I have written some test for this website in the file test_main.py. And then the test will be executed with pytest.

When new push event happens then github actions performs all the test that are in test_main.py and if they all pass 
then the new code will be uploaded to the server.
To upload the code I have used the appleboy/ssh-action@master to connect with the digital ocean server and I delete all the contents of the original website 
and then use git clone to copy the repository to my server. To use appleboy/ssh-action@master to connect to the server it is neccessary to use ssh-keys, which I created and I have added the private key to github secrets.

The link to the website is : http://159.223.14.63/
