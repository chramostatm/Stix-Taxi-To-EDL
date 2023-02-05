# STIX/TAXII Feed to EDL
## Project Inspiration
This project was spawned from a business need to pull a STIX/TAXII feeds for IOCs (Indicatiors of Compromise) from specific entities to an EDL (External Dynamic List) to block IPs and Domains

## Learning steps


## Explaining Each File
 HardCoded.py 
 - Meant for partial understanding how the json/ stix api is set up and work on how to get the URLs/IPs
GeneralFromJSON.py
 - Core functionality from Hard coded but generalized to any stix 2.1 JSON Bundle
 - The STIX JSON that I choose cointained ~75k IPs. With output redirection the time is ~78 seconds to complete. Without output redirection the time to complete was ~158 seconds.
 GeneralFromServer.py
 - adding in the taxii2client package and connecting to a hosted server (TODO)

### GeneralFromServer 
The Ultimate want/desire is to get the GeneralFromServer working with a specific ISAC server so the process can be fully automated. However, I won't get access to it till I can show the ISAC that the business is ready for Ingestion, but I wanted a specific test file and server to make sure it works first. I was unable to find an open server for testing (within time) that supported the new specifications of STIX/TAXII.
