from spatial_data_cache import SpatialDataCache
import requests

area_of_interest_uri = "https://www.geoportal.rlp.de/spatial-objects/314/collections/vermkv:gemeinde_rlp/items?gemeinde=Mendig&f=json"
area_of_interest_uri = "https://www.geoportal.rlp.de/spatial-objects/314/collections/vermkv:fluren_rlp/items/fluren_rlp.11660?f=json&gemeinde=Mendig&flur=3"
r = requests.get(area_of_interest_uri)
area_of_interest = r.text

dataset_configuration = { "datasets": [ {"file_identifier": "46f2d53e-6b79-284b-46a4-5f06c6248502", "type": "raster"},
                                        {"file_identifier": "6c1a481c-72f2-45a0-32e8-0fcb89dc31eb", "type": "raster"},
                                        {"file_identifier": "69ec8eb9-9b0f-57c4-30b4-d171cc974fda", "type": "raster"},
                                        {"file_identifier": "e7f59a98-c64c-bf3e-301e-1be256de1272", "type": "raster"},
                                        {"file_identifier": "2b009ae4-aa3e-ff21-870b-49846d9561b2", "type": "raster"},
                                        {"file_identifier": "2b115f1e-beb7-b0f8-d736-2b049d0e0f68", "type": "vector"},
                                        {"file_identifier": "b7f3e7fd-48cb-a886-d4fa-35542de49288", "type": "vector"},
                                        {"file_identifier": "79d8b001-972f-dc45-33ea-7d50113d4377", "type": "vector"},
                                        {"file_identifier": "d4e949a9-d7a2-2050-e018-41ca97bdf11f", "type": "vector"},
                                        {"file_identifier": "8f35aa4f-ebb6-87d2-85f2-bbaacad26e19", "type": "vector"},
                                        {"file_identifier": "a697f376-66fb-44a1-7881-2445b83efe3e", "type": "vector"},
                                        {"file_identifier": "010fa400-b1ef-30ee-71df-c3c42e614292", "type": "vector"},
                                        {"file_identifier": "a7ae0516-5abc-0a6e-88aa-a59c5f19d299", "type": "vector"},
                                      ]
                        }

catalogue_uri = "https://vocabulary.geoportal.rlp.de/geonetwork/srv/ger/csw"

cache = SpatialDataCache(dataset_configuration, area_of_interest, catalogue_uri)

cache.generate_cache()