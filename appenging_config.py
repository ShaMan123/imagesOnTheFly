# appengine_config.py
# TO-DO: generate lib with:
# $ pip install -t lib / pythonLibrary
from google.appengine.ext import vendor

# Add any libraries install in the "lib" folder.
vendor.add('lib')
