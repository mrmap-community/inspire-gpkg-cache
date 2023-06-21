#bfbce02a-a47d-03e2-b813-3a3223c8671d


from inspire_gpkg_cache.spatial_data_cache import SpatialDataCache
import requests

area_of_interest_uri = "https://www.geoportal.rlp.de/spatial-objects/314/collections/vermkv:gemeinde_rlp/items?gemeinde=Trierweiler&f=json"
r = requests.get(area_of_interest_uri)
area_of_interest = r.text
# some polygon in wiesbaden
area_of_interest = """
{
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "coordinates": [
          [
            [
              8.23801265870273,
              50.080535666460435
            ],
            [
              8.234518749956408,
              50.078553301362234
            ],
            [
              8.240505264333478,
              50.07577785251479
            ],
            [
              8.248664819516875,
              50.07695367804524
            ],
            [
              8.24934655780882,
              50.081369602454146
            ],
            [
              8.242124392776844,
              50.08358424729528
            ],
            [
              8.23801265870273,
              50.080535666460435
            ]
          ]
        ],
        "type": "Polygon"
      }
    }
  ]
}

"""

dataset_configuration = { "datasets": [ 
                                        {"file_identifier": "bfbce02a-a47d-03e2-b813-3a3223c8671d", "type": "vector"},
                                      ]
                        }

catalogue_uri = "https://gdk.gdi-de.org/gdi-de/srv/ger/csw"

cache = SpatialDataCache(dataset_configuration, area_of_interest, catalogue_uri)

cache.generate_cache()