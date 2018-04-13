
import webapp2
#from google.cloud import storage
from google.appengine.api import images
from google.appengine.api.images import get_serving_url
from google.appengine.api import app_identity
from google.appengine.ext import blobstore
from google.appengine.ext import ndb

# for testing 
# url: {BASE-URL}/?file={google_cloud_storage_object_name}

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
	#first attempt from here: https://github.com/GoogleCloudPlatform/google-cloud-python/issues/1295
        url = get_serving_url(None, filename=blobstore_filename)
        res.write('\nurl:' url)
        if blob_info:
	        res.write(blob_info + '\n')
		#second attempt from offical documenation
	        get_serving_url(blobKey) #, size=150, crop=True, secure_url=True)
            
        res.headers['Content-Type'] = 'text/plain'
        res.write('end')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
