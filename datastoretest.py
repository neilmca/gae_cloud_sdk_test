import webapp2
import logging
import string




class BaseHandler(webapp2.RequestHandler):
    def handle_exception(self, exception, debug):
        # Log the error.
        
        logging.exception(exception)

        # Set a custom message.
        self.response.write('An error occurred.')

        # If the exception is a HTTPException, use its error code.
        # Otherwise use a generic 500 error code.
        if isinstance(exception, webapp2.HTTPException):
            self.response.set_status(exception.code)
        else:
            self.response.set_status(500)




class DataStoreTest(BaseHandler):

   
    def get(self):             

        self.response.write('hello world')


  

 


logging.getLogger().setLevel(logging.DEBUG)

app = webapp2.WSGIApplication([

    ('/.*', DataStoreTest)    
    
], debug=True)

