from flask import Flask, request
import logger_util


LOGGER = logger_util.logger

app = Flask(__name__)

@app.route('/customer')
def vod() -> Tuple[Response, int]:   
    customer_id = request.args.get('customer_id', type=id) 
    LOGGER.info('Processing request for customer')
    
if __name__ == '__main__':
  
    # run() method of Flask class runs the application
    # on the local development server.
    LOGGER.info('Starting main')
    app.run()
