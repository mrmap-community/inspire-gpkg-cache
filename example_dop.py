import requests

from inspire_gpkg_cache.spatial_data_cache import SpatialDataCache

area_of_interest_uri = "https://www.geoportal.rlp.de/spatial-objects/314/collections/vermkv:gemeinde_rlp/items?gemeinde=Trierweiler&f=json"
r = requests.get(area_of_interest_uri)
area_of_interest = r.text

dataset_configuration = { "datasets": [ 
                                        {"file_identifier": "2b009ae4-aa3e-ff21-870b-49846d9561b2", "type": "raster"},
                                      ]
                        }

catalogue_uri = "https://gdk.gdi-de.org/gdi-de/srv/ger/csw"

cache = SpatialDataCache(dataset_configuration, area_of_interest, catalogue_uri)

cache.generate_cache()