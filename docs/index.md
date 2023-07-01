## Background 
-  This is page is dedicated to describe the architect and technical aspect of Community Garden IoT Project.
-  There are three kind of content in this documentation which are guide for installation, AWS device troubleshooting, Data Monitoring.

!!! Note 
    Please get the latest release of the document since each release has some changes in architecture.

### Installation Guide

- Install community garden script from the [github page](https://github.com/phamduchongan93/cgpi) 
- Connect RJ11 cable from ISS Transmitter to Davis Envoy. The communication between Envoy and raspberry pi will create two type of database which are sqlite and mysql. 
  
## Roadmap

1. Deploy sensors weather station.
2. Feed data stream to AWS ecosystem.
3. Test open hardware sensors for soil measurement.

## Architecture:
### Grid vs Off Grid Design:

  Grid like design, the community garden system would receive the energy provided from residential and commerical building directly. Losing certain piece of data data due to power outtage is possible since back up energy is not factored in the cost. While there is risk involve is low since data collected is farming sensors.

  Off Grid design, IoT computer and sensors are can be running via solar system, however number of sensors are limited.

### Transition of Technology:
- Davis station is based in CA, most of their hardware is propriety hardware. This requires a lot of time to develope configuration to work around the technology. Second of all, the scarity of the parts would drive up the price. 

### Project Component:

- **communitygarden-cli** program: software based solution written by Community Garden Team to use for configuring and modifying the single board while deploying different environment. 
- **AWS IoT Core** stack: Used to establish connection with AWS.

