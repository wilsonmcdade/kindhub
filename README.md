# kindhub
A customizable hub for daily needs.

# To run:
1) Clone the repo
2) Install required files with
~~~
pip install -r requirements.txt
~~~
3) Run app.py with
~~~
python app.py
~~~

# Customize:
The best thing about kindhub is that it's customizable! It's encouraged that you change your config.conf to match your needs. There are a few preinstalled packages that you can keep but you can also add (or create) your own packages. 

You probably want to modify your app.py to run the flask app on a different ip. You can do this by changing
~~~
app.py("0.0.0.0",port="8080")
~~~
to 
~~~
app.py()
~~~

Modifying your config.conf:
It's very easy to modify your kindhub by changing things in config.conf.
The first thing you should do is disable the config widget by changing the true value to false.

If you add your own package, it's very important that the name in the brackets match the name of the python file. This helps the dynamic importing function find the file.
