# SimpleRandomMOTD
Use this .py file on a minecraft server to update via a programed script the server MOTD randomly from a file

The intended use of this code is for automating it execution via for example linux cronjobs to selectet and change either the full MOTD of a minecraft server or a small part of it leaving a predetermined "static" part to the MOTD

This code is intended to run natively from the server running minecraft, so in order to work, you need to have full access  to linux or other OS in the server, (in other simpler words you need to be running the server from a dedicated machine, yours or rented) if you are using a minecraft server hosting service, I don`t know if its goin to work or how it works, i sopouse that if the hosting service lets you automate python files and upload .txt or similar texts files, it should work just fine.


 # Requieremts
 You need to have installed python 3.12 or newer to run the file

 # How to use 
 Open the .py file with your prefered text editor, add the full path to the server.properties and the full path to the list of MOTDs (Example "home/user/path/to/file") is prerred a .txt to store the MOTDs
 Furthermore youll need to store one MOTD for each line of the file (keep in mind that minecraft supports most if not all the unicode characters) moreover if you want to format the message you can format the MOTD on the .txt file or use the static part of the MOTD tho do so.

 If running on linux Create a new cronjob to run the .py file and reset the server.
