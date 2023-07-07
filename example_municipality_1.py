import requests

from inspire_gpkg_cache.spatial_data_cache import SpatialDataCache

area_of_interest_uri = "https://www.geoportal.rlp.de/spatial-objects/314/collections/vermkv:gemeinde_rlp/items?gemeinde=Mendig&f=json"
#area_of_interest_uri = "https://www.geoportal.rlp.de/spatial-objects/314/collections/vermkv:fluren_rlp/items/fluren_rlp.11660?f=json&gemeinde=Koblenz&flur=3"
r = requests.get(area_of_interest_uri)
area_of_interest = r.text

dataset_configuration = { "datasets": [ {"resourceidentifier": "https://registry.gdi-de.org/id/de.rp.vermkv/46f2d53e-6b79-284b-46a4-5f06c6248502", "type": "raster"},
                                        {"resourceidentifier": "https://registry.gdi-de.org/id/de.rp.vermkv/6c1a481c-72f2-45a0-32e8-0fcb89dc31eb", "type": "raster"},
                                        {"resourceidentifier": "https://registry.gdi-de.org/id/de.rp.vermkv/69ec8eb9-9b0f-57c4-30b4-d171cc974fda", "type": "raster"},
                                        {"resourceidentifier": "https://registry.gdi-de.org/id/de.rp.vermkv/e7f59a98-c64c-bf3e-301e-1be256de1272", "type": "raster"},
                                        {"resourceidentifier": "https://registry.gdi-de.org/id/de.rp.vermkv/2b009ae4-aa3e-ff21-870b-49846d9561b2", "type": "raster"},
                                        {"resourceidentifier": "https://registry.gdi-de.org/id/de.rp.vermkv/9c0cf294-087f-b646-b131-e3c53c9b1db0", "type": "raster"},
                                        {"resourceidentifier": "http://www.dlr-rnh.rlp.de/registry/spatial/dataset/7feed374-92ee-0441-cc8f-594651df2296", "type": "raster"},
                                        {"resourceidentifier": "https://komserv4gdi.service24.rlp.de/37341153-8116-5571-3ac9-92e503453c2b", "type": "raster"},
                                        {"resourceidentifier": "http://naturschutz.rlp.de/2b115f1ebeb7b0f8d7362b049d0e0f68", "type": "vector"},
                                        {"resourceidentifier": "http://www.lbm.rlp.de/registry/spatial/dataset/b7f3e7fd-48cb-a886-d4fa-35542de49288", "type": "vector"},
                                        {"resourceidentifier": "https://registry.gdi-de.org/id/de.rp.vermkv/79d8b001-972f-dc45-33ea-7d50113d4377", "type": "vector"},
                                        {"resourceidentifier": "http://www.lbm.rlp.de/registry/spatial/dataset/d4e949a9-d7a2-2050-e018-41ca97bdf11f", "type": "vector"},
                                        {"resourceidentifier": "https://lfu.rlp.de/8f35aa4febb687d285f2bbaacad26e19", "type": "vector"},
                                        {"resourceidentifier": "https://registry.gdi-de.org/id/de.rp.vermkv/a697f376-66fb-44a1-7881-2445b83efe3e", "type": "vector"},
                                        {"resourceidentifier": "http://www.lgb-rlp.de/registry/spatial/dataset/010fa400-b1ef-30ee-71df-c3c42e614292", "type": "vector"},
                                        {"resourceidentifier": "https://map1.sgdnord.rlp.de/a7ae05165abc0a6e88aaa59c5f19d299", "type": "vector"},
                                      ]
                        }

dataset_configuration = { "datasets": [ {"resourceidentifier": "https://registry.gdi-de.org/id/de.rp.vermkv/46f2d53e-6b79-284b-46a4-5f06c6248502", "type": "raster"},
                                        {"resourceidentifier": "https://registry.gdi-de.org/id/de.rp.vermkv/6c1a481c-72f2-45a0-32e8-0fcb89dc31eb", "type": "raster"},
                                        {"resourceidentifier": "http://naturschutz.rlp.de/2b115f1ebeb7b0f8d7362b049d0e0f68", "type": "vector"},
                                    ]
                        }

catalogue_uri = "https://vocabulary.geoportal.rlp.de/geonetwork/srv/ger/csw"
#catalogue_uri = "https://gdk.gdi-de.org/gdi-de/srv/ger/csw"
#catalogue_uri = "https://inspire-geoportal.ec.europa.eu/GeoportalProxyWebServices/resources/OGCCSW202"


cache = SpatialDataCache(dataset_configuration, area_of_interest, catalogue_uri, output_folder='/tmp/')
json_result = cache.check_options()
print(json_result)
#cache.generate_cache()