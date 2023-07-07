import json
import sys

from inspire_gpkg_cache.spatial_data_cache import SpatialDataCache

print(sys.argv[1])

configuration = json.loads(sys.argv[1])

cache = SpatialDataCache(configuration['dataset_configuration'], configuration['area_of_interest'], 'https://vocabulary.geoportal.rlp.de/geonetwork/srv/ger/csw')

json_result = cache.check_options()

print(json_result)



