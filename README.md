# kindhub
A customizable hub for daily needs.

___

## To run:
1) Clone the repo
2) Install required files with
~~~
pip install -r requirements.txt
~~~
3) Run app.py with
~~~
python app.py
~~~

___

## Customize:
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

___

## Developing kindhub packages:

Kindhub has a few default packages including gCal, weather, xkcd, and a news feed. To see an example of an add-on widget package, check out [RPi Light Controller](https://github.com/wilsonmcdade/lights-widget). 

The structure of a package needs to be like so:

~~~
config.conf
|__ templates/
|__ __ widget.html
|__ widgets/
|__ __ widget.py
~~~

To install a package, the user simply needs to add the relevant part of the package's config.conf to their config.conf and drags and drops templates/ and widgets/ into their directories.

The config for your package must have the following:
⋅⋅* the name of your widget (matching the name of the python file) in brackets
⋅⋅* an enabled value
⋅⋅* a strname value -- this is what shows up in the navbar on the website
⋅⋅* a route for your widget -- this is what the navbar links send you to.

~~~
[widget]
# default widget structure
enabled: true
strname: Default Widget
route: /widget
~~~
