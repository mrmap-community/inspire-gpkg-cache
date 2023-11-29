Usage
=====

Prepare 
-------

* Get some geojson Polygon with a smal area ;-) - maybe some square kilometer (e.g. digitize it on https://geojson.io)
* Get some metadata resourceidentifier for datasets, that are available via supported INSPIRE Services
* Get the catalogues base url from which you want to resolve the metadata

How it works
------------
Normally there are 2 stages:

1. Get a list of needed datasets. These should be identified by their SpatialDatasetIdentifier.
  The initial dataset_configuration includes an array with this identifiers. With help of the
  method check_options, the user get a json object with all relevant information to decide, which
  dataset is available in which dataset_type (raster or vector).

2. The generate_cache method should be invoked with an additional information about the wished type of 
   dataset - raster or vector. See the examples below.


Examples
--------

1. One single dataset available in the catalogue of Germany

  .. code-block:: python

    from inspire_gpkg_cache.spatial_data_cache import SpatialDataCache
    import requests

    area_of_interest_uri = "https://www.geoportal.rlp.de/spatial-objects/314/collections/vermkv:fluren_rlp/items/fluren_rlp.11660?f=json&gemeinde=Mendig&flur=3"
    r = requests.get(area_of_interest_uri)
    area_of_interest = r.text
    dataset_configuration = { "datasets": [ 
                                        {"resourceidentifier": "http://naturschutz.rlp.de/2b115f1ebeb7b0f8d7362b049d0e0f68", "type": "vector"},
                                      ]
                        }
    catalogue_uris = ["https://gdk.gdi-de.org/gdi-de/srv/ger/csw"]
    cache = SpatialDataCache(dataset_configuration, area_of_interest, catalogue_uris)

    json_result = cache.check_options()
    print(json_result)

    cache.generate_cache()

2. Some datasets (mixed raster and vector) - use the catalogue of Rhineland-Palatinate

  .. code-block:: python

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

    #dataset_configuration = { "datasets": [ {"resourceidentifier": "https://registry.gdi-de.org/id/de.rp.vermkv/46f2d53e-6b79-284b-46a4-5f06c6248502", "type": "raster"},
    #                                        {"resourceidentifier": "https://registry.gdi-de.org/id/de.rp.vermkv/6c1a481c-72f2-45a0-32e8-0fcb89dc31eb", "type": "raster"},
    #                                        {"resourceidentifier": "http://naturschutz.rlp.de/2b115f1ebeb7b0f8d7362b049d0e0f68", "type": "vector"},
    #                                    ]
    #                        }

    catalogue_uris = ["https://vocabulary.geoportal.rlp.de/geonetwork/srv/ger/csw"]
    #catalogue_uri = "https://gdk.gdi-de.org/gdi-de/srv/ger/csw"
    #catalogue_uri = "https://inspire-geoportal.ec.europa.eu/GeoportalProxyWebServices/resources/OGCCSW202"


    cache = SpatialDataCache(dataset_configuration, area_of_interest, catalogue_uris, output_folder='/tmp/')
    json_result = cache.check_options()
    print(json_result)
    cache.generate_cache()

3. Example for an json object as returned by the check_options method:

   .. code-block:: json
    
    [{
      "spatial_dataset_identifier": "https://registry.gdi-de.org/id/de.rp.vermkv/46f2d53e-6b79-284b-46a4-5f06c6248502",
      "time_to_resolve_dataset": "0.37201809883117676",
      "error_messages": [],
      "title": "ATKIS DTK50",
      "fileidentifier": "46f2d53e-6b79-284b-46a4-5f06c6248502",
      "format": "GeoTIFF",
      "epsg_id": 25832,
      "services": [{
        "service_type": "view",
        "service_version": "OGC:WMS 1.1.1",
        "possible_dataset_type": "raster",
        "access_uri": "https://www.geoportal.rlp.de/mapbender/php/wms.php?inspire=1&layer_id=61669&withChilds=1&REQUEST=GetCapabilities&SERVICE=WMS",
        "service_resource_name": "rp_dtk50",
        "error_messages": []
      }, {
        "service_type": "download",
        "service_version": "predefined ATOM",
        "possible_dataset_type": null,
        "access_uri": null,
        "service_resource_name": null,
        "error_messages": ["ATOM Feed: No link to dataset feed for Spatial Dataset Identifier found in service feed", "Service is not usable for downloading dataset"]
      }],
      "time_to_resolve_services": "0.33198046684265137"
    }, {
      "spatial_dataset_identifier": "https://registry.gdi-de.org/id/de.rp.vermkv/6c1a481c-72f2-45a0-32e8-0fcb89dc31eb",
      "time_to_resolve_dataset": "0.34154748916625977",
      "error_messages": [],
      "title": "ATKIS DTK25",
      "fileidentifier": "6c1a481c-72f2-45a0-32e8-0fcb89dc31eb",
      "format": "GeoTIFF",
      "epsg_id": 25832,
      "services": [{
        "service_type": "download",
        "service_version": "predefined ATOM",
        "possible_dataset_type": null,
        "access_uri": null,
        "service_resource_name": null,
        "error_messages": ["ATOM Feed: No link to dataset feed for Spatial Dataset Identifier found in service feed", "Service is not usable for downloading dataset"]
      }, {
        "service_type": "view",
        "service_version": "OGC:WMS 1.1.1",
        "possible_dataset_type": "raster",
        "access_uri": "https://www.geoportal.rlp.de/mapbender/php/wms.php?inspire=1&layer_id=61673&withChilds=1&REQUEST=GetCapabilities&SERVICE=WMS",
        "service_resource_name": "rp_dtk25",
        "error_messages": []
      }],
      "time_to_resolve_services": "0.7597250938415527"
    }, {
      "spatial_dataset_identifier": "http://naturschutz.rlp.de/2b115f1ebeb7b0f8d7362b049d0e0f68",
      "time_to_resolve_dataset": "0.4537999629974365",
      "error_messages": [],
      "title": "Biotopkataster (Fl\u00e4chen)",
      "fileidentifier": "2b115f1e-beb7-b0f8-d736-2b049d0e0f68",
      "format": "Database",
      "epsg_id": 4258,
      "services": [{
        "service_type": "oaf",
        "service_version": null,
        "possible_dataset_type": "vector",
        "access_uri": "https://www.geoportal.rlp.de/spatial-objects/537/collections/ms:bk_f",
        "service_resource_name": null,
        "error_messages": []
      }, {
        "service_type": "view",
        "service_version": "OGC:WMS 1.1.1",
        "possible_dataset_type": "raster",
        "access_uri": "https://www.geoportal.rlp.de/mapbender/php/wms.php?inspire=1&layer_id=54206&withChilds=1&REQUEST=GetCapabilities&SERVICE=WMS",
        "service_resource_name": "bk_f_text",
        "error_messages": []
      }, {
        "service_type": "view",
        "service_version": "OGC:WMS 1.1.1",
        "possible_dataset_type": "raster",
        "access_uri": "https://www.geoportal.rlp.de/mapbender/php/wms.php?inspire=1&layer_id=54195&withChilds=1&REQUEST=GetCapabilities&SERVICE=WMS",
        "service_resource_name": "bk_f",
        "error_messages": []
      }, {
        "service_type": "download",
        "service_version": "OGC:WFS 2.0.0",
        "possible_dataset_type": "vector",
        "access_uri": "https://www.geoportal.rlp.de/mapbender/php/wfs.php?INSPIRE=1&FEATURETYPE_ID=3015&REQUEST=GetCapabilities&SERVICE=WFS&VERSION=2.0.0",
        "service_resource_name": "ms:bk_f",
        "error_messages": []
      }, {
        "service_type": "download",
        "service_version": "predefined ATOM",
        "possible_dataset_type": null,
        "access_uri": "https://www.geoportal.rlp.de/mapbender/php/mod_inspireDownloadFeed.php?id=2b115f1e-beb7-b0f8-d736-2b049d0e0f68&type=DATASET&generateFrom=wfs&wfsid=537&featuretypeid=3015",
        "service_resource_name": null,
        "error_messages": ["Service is not usable for downloading dataset"]
      }, {
        "service_type": "download",
        "service_version": "predefined ATOM",
        "possible_dataset_type": "raster",
        "access_uri": "https://www.geoportal.rlp.de/mapbender/php/mod_inspireDownloadFeed.php?id=2b115f1e-beb7-b0f8-d736-2b049d0e0f68&type=DATASET&generateFrom=wmslayer&layerid=54195",
        "service_resource_name": null,
        "error_messages": []
      }],
      "time_to_resolve_services": "0.4542813301086426"
    }]

4. Geopackage which was generated by the second example: https://documents.geoportal.rlp.de/index.php/s/X3Lp8pxH8f9NoNM/download/spatialcache_mendig.gpkg