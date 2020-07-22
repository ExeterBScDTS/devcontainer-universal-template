# Python dev container build example

## Open main.py

This should active a request to install the Python linter and will also ensure that the Python engine is installed.  You'll need to be online for this to happen.

## Select Python version

VS&nbsp;Code may already have a default Python selection if you've built Python projects before.  When using the Dev Container you must select one of the Python versions included in the container.  Click on the Python selection button on the bottom bar of VS&nbsp;Code and select one of the choices - 3.8.3  is recommended.

## Install the requirements

It should be possible to run the Python script in ```main.py``` now, but you will get errors because the required **flask** library module is not installed.

Open a bash terminal window and enter these commands

```bash
codespace:~/workspace$ cd app
codespace:~/workspace/app$ /opt/python/latest/bin/python -m pip install -r requirements.txt --user
```

Now run the script, and you shold see the following output in the Python terminal
```txt
 * Serving Flask app "main" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)
 ```
 Place your cusror over ```http://0.0.0.0:5000/``` and Ctrl+Click to open a browser window.