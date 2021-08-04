# import Patients.src.back_end.db_connection
#import Patients.src.back_end.db_connection as m
from Patients.src.back_end.db_connection import Connection
from Patients.src.controller.middleware import middleware_controller
from Patients.src.front_end.template import front_end_templates
#import numpy,pytest_bdd
import logging, argparse
from logging.handlers import TimedRotatingFileHandler
#logname = r'C:\Users\admin\PycharmProjects\Hospitalapplications\Patients\log\app.log'
#handler = TimedRotatingFileHandler(logname, when="midnight", interval=1)
#handler.suffix = "%Y%m%d"
#logger.addHandler(handler)
if __name__ == '__main__':

    #Patients.src.back_end.db_connection.connection()
    #m.connection()

    #argparse configuration
    parser = argparse.ArgumentParser()
    requiredNamed = parser.add_argument_group("required named argument")
    requiredNamed.add_argument('-e', '--email_id', dest='email_id',
                               help="please enter the email address",
                               required=True, nargs='+')
    args = parser.parse_args()
    email_address = args.email_id


    #logging configuration
    logger = logging.getLogger()
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(lineno)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    FileHandler = logging.FileHandler(filename= r'C:\Users\HP\PycharmProject\hospitalapplication_1\Patients\log\app.log')
    FileHandler.setFormatter(formatter)
    #logname = r'C:\Users\HP\PycharmProject\hospitalapplication_1\Patients\log\app.log'
    #handler = TimedRotatingFileHandler(logname, when="midnight", interval=1)
    #handler.suffix = "%Y%m%d"
    #logger.addHandler(handler)

    logger.setLevel(level=logging.INFO)
    logger.addHandler(FileHandler)

    streamhandler = logging.StreamHandler()
    streamhandler.setLevel(logging.CRITICAL)
    streamhandler.setFormatter(formatter)
    logger.addHandler(streamhandler)

    logger.debug("Starting...")
    logger.debug("Call to connection method...")
    logger.error("general error")

    Connection()
    front_end_templates()
    middleware_controller()
    logger.info("email address - {}".format(email_address))