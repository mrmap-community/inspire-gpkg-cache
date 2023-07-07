import requests

from inspire_gpkg_cache.spatial_data_cache import SpatialDataCache

area_of_interest_uri = "https://www.geoportal.rlp.de/spatial-objects/314/collections/vermkv:gemeinde_rlp/items?gemeinde=Ochtendung&f=json"
r = requests.get(area_of_interest_uri)
area_of_interest = r.text

dataset_configuration = { "datasets": [ 
                                        {"resourceidentifier": "http://naturschutz.rlp.de/2b115f1ebeb7b0f8d7362b049d0e0f68", "type": "vector"},
                                      ]
                        }

catalogue_uri = "https://gdk.gdi-de.org/gdi-de/srv/ger/csw"

cache = SpatialDataCache(dataset_configuration, area_of_interest, catalogue_uri)

json_result = cache.check_options()
print(json_result)

cache.generate_cache()