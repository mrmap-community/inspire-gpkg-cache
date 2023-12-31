inspire-gpkg-cache
------------------

A simple lib to cache spatial data which is published conform to the rules of the European SDI (INSPIRE).
Raster data, vector data and their corresponding metadata will be stored in a single OGC geopackage file. 
INSPIRE View and Download Services are used to access the remote data. The logic for building the cache
can also be used to cache data via standardized WMS, WFS and OAF interfaces. 

The typical themes where datacaches (offline usage) are relevant:

* Farming
* SAR 
* Field mapping
* Disaster management
* ...

In SDIs, like INSPIRE, all the data and it's metadata is served via web-based interfaces. If there is no connection to the Internet,
the Infrastructure fails.
It is extremly important to have the option to cache all relevant distributed data in an automatic way.

The European SDI uses some extensions of the OGC/ISO standards, that allow such an automatic caching method. 

**Crucial INSPIRE extensions:**

* Existence of persistent dataset identifiers
* Unified interpretation of ISO19119 and ISO19115 metadata (https://github.com/INSPIRE-MIF/technical-guidelines/tree/2022.2/metadata/metadata-iso19139)

**Following service types are supported:**

* Raster data:

  * INSPIRE View Service based on WMS 1.1.1 (https://github.com/INSPIRE-MIF/technical-guidelines/blob/2022.2/services/view-wms/ViewServices.pdf)
  * INSPIRE ATOM Feeds (https://inspire.ec.europa.eu/file/1554/download?token=Y_538IH4)

* Vector data:
  
  * OGC API Features (https://docs.ogc.org/is/17-069r4/17-069r4.html)
  * INSPIRE ATOM Feeds (https://inspire.ec.europa.eu/file/1554/download?token=Y_538IH4)



See the `documentation <https://inspire-gpkg-cache.readthedocs.io/en/latest/index.html>`_ for details.
