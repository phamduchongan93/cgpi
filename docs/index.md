## Background 
  This is page is dedicated to describe the architect and technical aspect of Community Garden IoT Project.
  There are three parts of documentation which are guide for installation, AWS device troubleshooting, Data Monitoring.

!!! Note 
    Pay attention to release of the document since each release has some changes in architecture.

### Installation Guide

  Install community garden script from the github for latest version.
  To verify the
    Install weewx and database software for weather station.
    Testing open hardware sensors for soil measurement.
## Roadmap
  Deploy sensors weather station.
  Feed data stream to AWS ecosystem.

## Architecture:
### Grid vs Off Grid Design:

  Grid like design, the community garden system would receive the energy provided from residential and commerical building directly. Losing certain piece of data data due to power outtage is possible since back up energy is not factored in the cost. While there is risk involve is low since data collected is farming sensors.

  Off Grid design, IoT computer and sensors are can be running via solar system, however number of sensors are limited.


### Project Component:

- **'communitygarden-cli'** program: software based solution to use for configuring and modifying the single board to fit in the need of deployment environment.
- **AWS IoT Core** stack: Used to establish connection with AWS.

