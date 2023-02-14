# The WHOW Ontology Network

This repository includes the so-called **WHOW Ontology Network** of the [WHOW CEF Open Data project](https://whowproject.eu) The ontology network is organised in ontological modules that allow us to represent different topics faced in the project; namely, the monitoring of waters, both marine, internals, groundwaters and waters for human consumption, the monitoring of weather conditions, the monitoring of specific health indicators.

## Ontology modules of the WHOW ontology network
At the time being the following ontological modules are part of the network. We briefly introduce them below.

### [Hydrography ontology](https://w3id.org/whow/onto/hydrography)

![Graphical representation of the hydrography ontology](https://raw.githubusercontent.com/whow-project/semantic-assets/main/ontologies/graphical-representation-ontologies/hydrography-ontology.png)

The Hydrography ontological module represents a taxonomy of water bodies and the relationships between them. The ontology concepts are semantically aligned with INSPIRE defined concepts.

### [Water monitoring ontology](https://w3id.org/whow/onto/water-monitoring)

![Graphical representation of the water monitoring ontology](https://raw.githubusercontent.com/whow-project/semantic-assets/main/ontologies/graphical-representation-ontologies/water-monitoring.png)

The Water monitoring ontological module is an extension of the SOSA/SSN ontology and of the ISPRA ontology INSPIRE-MF for the water domain. It contributes to represent the monitoring of the various types of waters and to capture the different parameters that characterise the quality of the water, according to the different related European Directives. The ontology uses the Hydrography module above in order to model the Water Feature being observed.

### [Weather monitoring ontology](https://w3id.org/whow/onto/weather-monitoring)
![Graphical representation of the water monitoring ontology](https://raw.githubusercontent.com/whow-project/semantic-assets/main/ontologies/graphical-representation-ontologies/weather-monitoring.png)

The Weather monitoring ontological module is used in WHOW to support the extreme event use case. In particular, it is an ontology that is capable of representing meteorological observations. It can be used in general for this type of high value datasets.


### [Health monitoring ontology](https://w3id.org/whow/onto/health-monitoring)

![Graphical representation of the water monitoring ontology](https://raw.githubusercontent.com/whow-project/semantic-assets/main/ontologies/graphical-representation-ontologies/health-monitoring.png)

The Health monitoring ontological module aims to represent health indicators with a specific focus on infectious diseases.

We are currently working on an additional ontological module for water quality indicators.

## License
All the ontological modules are realeased under the open license Creative Commons Attribution 4.0
