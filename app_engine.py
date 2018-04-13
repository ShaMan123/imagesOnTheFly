
import webapp2
#from google.cloud import storage
from google.appengine.api import images
from google.appengine.api.images import get_serving_url
from google.appengine.api import app_identity
from google.appengine.ext import blobstore
from google.appengine.ext import ndb

#import importlib

#moduleName = input('Enter module name:')
#importlib.import_module(moduleName)

class MainPage(webapp2.RequestHandler):
    def get(self):
    	req = self.request
        res = self.response
        filePath = req.get('file')
    	blobstore_filename = '/gs/push-notification-111.appspot.com/{}'.format(filePath)
        blob_key = blobstore.create_gs_key(blobstore_filename)
    	res.write(filePath + '\n' + blobstore_filename + '\n' + blob_key + '\n' )
        blob_info = blobstore.get(blob_key)
        res.write('blob_info:' blob_info)
        url = get_serving_url(None, filename=blobstore_filename)
        res.write('\nurl:' url)
        if blob_info:
	        res.write(blob_info + '\n')
	        get_serving_url(blobKey) #, size=150, crop=True, secure_url=True)
            
        res.headers['Content-Type'] = 'text/plain'
        res.write('end')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)

""""
page_size = 1
  		##stats = gcs.listbucket(filePath, max_keys=page_size)
		##images.get_serving_url(filePath, size=150, crop=True, secure_url=True)
##from google.appengine.api import images
        client = storage.Client()
        bucket = client.get_bucket('<your-bucket-name>')
        blob = bucket.blob('my-test-file.txt')
        blob.upload_from_string('this is test content!')
"""
