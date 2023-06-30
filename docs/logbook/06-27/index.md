# Set Up Battery and Analysis IoT architecture

- In order to test if battery can carry the charge, the battery need to generate 12V on the Multimeter measurement. As is right now, the battery did show the 12 V output.

- However, as recommened for any DIY off-grid instalation, the MPPT charge controller has to provide green indicator to notify the healthy state.

- The AWS IoT as mqtt message broker only able to receive message from weewx service, however this is a simple query that fetch info and send it to AWS IoT Core. In short, the communication is not statefull. Because of this limitation, storage mechanism has to be inititated. I set up a bucket to store the data from weewx on AWS cloud. Refer to video to have a better understand the architect of AWS IoT.

- To achieve continunity and cost effective when running IoT services, creating a single channel stream is the best option to operate the IoT projects. In other word, the real time data design is what the project aim for.

 

# Reference:
- For more information, please visit phamduchongan93.github.io/cgpi to get the latest info of AWS IoT core.
