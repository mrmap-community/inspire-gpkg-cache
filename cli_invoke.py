import json
import sys

from inspire_gpkg_cache.spatial_data_cache import SpatialDataCache

print(sys.argv[1])

configuration = json.loads(sys.argv[1])

if sys.argv[2] == 'checkOptions':
    cache = SpatialDataCache(configuration['dataset_configuration'], json.dumps(configuration['area_of_interest']), ['https://vocabulary.geoportal.rlp.de/geonetwork/srv/ger/csw'])
    json_result = cache.check_options()
    # give back json with download options
    print(json_result)
    sys.exit()
if sys.argv[2] == 'generateCache':
    cache = SpatialDataCache(configuration['dataset_configuration'], json.dumps(configuration['area_of_interest']), ['https://vocabulary.geoportal.rlp.de/geonetwork/srv/ger/csw'], output_filename='test', output_folder='/home/armin/GDI-RP/devel/Geoportal/Mapbender2.8/http/tmp/')
    print('start generate cache')
    cache.generate_cache()
    sys.exit()



