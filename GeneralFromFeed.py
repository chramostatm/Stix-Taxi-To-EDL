from stix2.v21 import (Indicator, KillChainPhase, Malware, Relationship, Bundle)
from stix2 import parse



bundle =Bundle(objects=[indicator, malware, relationship])
for obj in bundle.objects:
    if obj.get("type") == "indicator":
        if(str(obj.get("pattern")).__contains__("url")):
            print(str(obj.get("pattern")).split("'",1)[1].replace("']", ""))
            #append to file in Python or lasy way us the '>>' when running
        elif str(obj.get("pattern")).__contains__("ip"):
            print(str(obj.get("pattern")).split('\'',1)[1].replace("']", ""))
            #append to file in Python or lasy way us the '>>' when running