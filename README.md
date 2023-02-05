# STIX/TAXII Feed to EDL
## Project Inspiration
This project was spawned from a business need to pull a STIX/TAXII feeds for IOCs (Indicatiors of Compromise) from specific entities to an EDL (External Dynamic List) to block IPs and Domains

## Learning steps


## Explaining Each File
 HardCoded.py 
 - Meant for partial understanding how the json/ stix api is set up and work on how to get the URLs/IPs
GeneralFromJSON.py
 - Core functionality from Hard coded but generalized to any stix 2.1 JSON Bundle
 GeneralFromServer.py
 - adding in the taxii2client package and connecting to a hosted server (TODO)

### GeneralFromServer 
The Ultimate want desire is to update 
