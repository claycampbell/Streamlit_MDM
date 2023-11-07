
from configparser import ConfigParser
from pathlib import Path

sfconnection={}
connection=''
statusmessage=''
statuscode=''
queryresult={}

def read_conf_file():
    configuration_path=Path(__file__).parent / "../connections/conf.ini"
    configparser = ConfigParser()
    configparser.read(configuration_path)
    return configparser
