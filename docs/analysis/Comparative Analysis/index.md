# System Build Comparison
## Build with AWS 
This is the current build that the community garden has been implementing for the summer build. The AWS IoT Core was introduced by the database team. Although there are features and add-ons for this service, this AWS IoT Core software is an MQTT message broker. since AWS IoT Core is open source, there is no fee involve while using this software.

## Build with Self Hosted Soluation:
- Due to the recent upgrade of raspberry pi 4. The potential running a message broker on the raspberry pi is possible as well as running a web-based dashboard. This new hardware upgrade helps to reduce the reliance on the AWS cloud.
- Visit the following link for information:

<iframe width="1756" height="669" src="https://www.youtube.com/embed/_DO2wHI6JWQ" title="Raspberry Pi IoT Server Tutorial: InfluxDB, MQTT, Grafana, Node-RED &amp; Docker" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

- This build is stable and well-supported by electronics enthusiasts. Additionally, the supply of open hardware is more available and budget-friendly to consumers. The only limitation is the lack of automation and scalability for this model. Compare AWS cloud-based solution, this require the user manually install the required services and need an end program or an end user to verify the usability.

