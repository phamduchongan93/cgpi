# Previous Meeting Note:
- Verifying Davis Station Status.
- Building off-grid system. 
- Defining and building bucket for logging. 
- Getting message system ready for s3 bucket.

# Report
- Hope you are doing well.
- To have a insight look for technical documentation of the project, please visit https://cppfarm.anpham.me for information regarding software maintnance and installation of solar and sensor station.
- Knowing that we try to apply "agile" for the projectp previously. Tasks and operations are divided into parts which are installing weather station, install solar system, and install network. These tasks can be perfomed individually without affecting each other. So far, none defect has been found on the equipment.
- Knowning this project is funded by AWS grant. Beside AWS IoT Core solution provided by AWS, there are other BYO (Build Your Own) solution. This approach is due to the opportunity of having new technolgoy stack that has been developed by single board community. This tech stack is maturely tested, supported, and popular to educational community.  As for Davis Weather Station, with previous approach of Melvin and Peter and new cable installed, I can put together a webpage dashboard for viewing the data. However, due to proprietary cable that Davis company has been implementing, the damage cable I tried to fix can't be connected to the sensors. 
- I also added one of Professor to our supporter list, we had some discussion before regarding Community Garden project during Spring semester. The scope of discussion is narrawed to network deployment concern. He also mentioned IT department should be one of our stakeholders since we are going to consume soome of their network bandwith. However, right now this is not really our concern since most of our dataset are sensors data. Unless you guys want to have the outdoor camera installed for remote monitoring which require some wiring work for the camera inside the box, we are going to need more bandwith for the camera. 
- I try to install the solar indoor while letting the pannel faces the window to charge the battery. The solar only charge around 0-7V which is not enough to charge the battery and power the weather station.
- The limitation we have is that weewx can't seem to provide a single json payload. There is an extension of the program, yet it doesn't seem seem to be supported anymore, latest release is weewx-json_1.1. I hope that using python to query the database file to message AWS IoT would has the better chance. Because of this limitation, a S3 bucket has to be created prior to data filtering. Long story short, our station can communicate to AWS Cloud. I will try to test out the python script next week.
- There is other thing is seems like the solar pannel has never been used since no wiring work has been done to solar pannel. I've been contacting our solar vendor which is solarland. If they are not responsive, I just document my wiring work and contact one of the professor from supporter list since she seems to be expert in off-grid solar.
- After July, we should able to record a webinair to demonstrate our tech stack for software side.
- If you have any further concern regarding the deliverable matter of this project, feel free to reach out to me. 
