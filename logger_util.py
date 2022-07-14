import logging
from flask import request

class ContextFilter(logging.Filter):
    """ Adds request argument -customer_id from Flask to log records. Here more request attributes can be added, if needed in
    future. """
    def filter(self, record):
        try:
            customer_id = request.args.get('customer_id', type=int)
            record.customerId = f'custId - {customer_id}'
        except RuntimeError as ex:
            if "Working outside of request context" in str(ex):
                record.customerId = ''
            else:
                raise ex

        return True


contextFilter = ContextFilter()

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
formatter = logging.Formatter(
    '%(asctime)s %(module)s %(threadName)s %(customerId)s ::%(funcName)s:%(lineno)d %(levelname)-8s %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S'
)

handler.setFormatter(formatter)
handler.addFilter(contextFilter)
logger.addHandler(handler)
