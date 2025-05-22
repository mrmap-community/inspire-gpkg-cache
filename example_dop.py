import requests

from inspire_gpkg_cache.spatial_data_cache import SpatialDataCache

area_of_interest_uri = "https://www.geoportal.rlp.de/spatial-objects/314/collections/vermkv:gemeinde_rlp/items?gemeinde=Mendig&f=json"
r = requests.get(area_of_interest_uri)
area_of_interest = r.text
datasets_to_exclude = [ "https://registry.gdi-de.org/id/de.rp.vermkv/9ab1d827-ec73-93ff-9863-e4b2f47caeaf", "https://registry.gdi-de.org/id/de.rp.vermkv/2b009ae4-aa3e-ff21-870b-49846d9561b2",]
dataset_configuration = { "datasets": [ 
                                        {"resourceidentifier": "https://registry.gdi-de.org/id/de.rp.vermkv/2b009ae4-aa3e-ff21-870b-49846d9561b2", "type": "raster"},
                                        {"resourceidentifier": "https://registry.gdi-de.org/id/de.rp.vermkv/5e410c1e-8f71-c62c-2cd4-4344e790e623", "type": "vector"},
                                        #{"resourceidentifier": "https://registry.gdi-de.org/id/de.rp.vermkv/9ab1d827-ec73-93ff-9863-e4b2f47caeaf", "type": "vector"},
                                      ]
                        }

catalogue_uris = ["https://vocabulary.geoportal.rlp.de/geonetwork/srv/ger/csw", "https://gdk.gdi-de.org/gdi-de/srv/ger/csw", "https://inspire-geoportal.ec.europa.eu/srv/ger/csw"]

cache = SpatialDataCache(dataset_configuration, area_of_interest, catalogue_uris, output_filename=False, output_folder="/tmp/", datasets_to_exclude=datasets_to_exclude)

json_result = cache.check_options()
print(json_result)

cache.generate_cache()