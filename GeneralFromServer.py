#from stix2.v21 import (Indicator, KillChainPhase, Malware, Relationship, Bundle)
from stix2 import parse
from taxii2client import Collection#https://github.com/oasis-open/cti-taxii-client
from stix2 import CompositeDataSource, FileSystemSource, TAXIICollectionSource
from taxii2client.v21 import Server
"""
import time
def current_milli_time():
    return round(time.time() * 1000)
"""

# create TAXIICollectionSource
colxn = Collection("https://www.circl.lu/doc/misp/feed-osint/")
ts = TAXIICollectionSource(colxn, allow_custom=True)
print(type(ts))
#startTime =current_milli_time()
#bundle = parse(colxn, allow_custom=True)
#print(type(bundle))#here for troubleshooting errors
"""
for obj in bundle.objects:
    if obj.get("type") == "indicator":
        if(str(obj.get("pattern")).__contains__("url")):
            #str(obj.get("pattern")).split('\'',1)[1].replace("']", "")
            print(str(obj.get("pattern")).split("'",1)[1].replace("']", ""))
            #append to file in Python or lasy way us the '>>' when running
        elif str(obj.get("pattern")).__contains__("ip"):
            #str(obj.get("pattern")).split('\'',1)[1].replace("']", "")
            print(str(obj.get("pattern")).split('\'',1)[1].replace("']", ""))
            #append to  a file in Python or lasy way us the '>>' when running
            #or do > if you don't compare abot file contents
#endTime = current_milli_time()
"""
#print(endTime-startTime)
