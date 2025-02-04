# SimpleRandomMOTD
Use this Python script on a Minecraft server to update the server MOTD randomly from a file via an automated script.

# Description
This script is designed to automate the execution of MOTD updates using tools like Linux cron jobs. It allows you to either change the entire MOTD or modify only a specific part while keeping a predefined static section.

This script is intended to run natively on the server hosting Minecraft. To use it, you need full access to the operating system (Linux or other). In other words, this is meant for dedicated machines, whether owned or rented. If you're using a third-party Minecraft hosting service, I can't guarantee compatibility. However, if the service allows you to automate Python scripts and upload .txt or similar files, it should work fine.

# Requirements
Python 3.12 or newer must be installed on the server.

# How to Use

 -Open the .py file in your preferred text editor.
 
 -Add the full path to server.properties and the full path to the MOTD list file (e.g., "home/user/path/to/file").
 
 -A .txt file is preferred for storing MOTDs.
 
 -Each MOTD should be written on a separate line.
 
 -Minecraft supports most, if not all, Unicode characters.
 
 -You can format the MOTD directly in the .txt file or use the static part of the MOTD to do so.
 

If running on Linux:
Create a cron job to run the .py script and restart the server automatically.
