import os
import random
#To use ajust the paths and the static motd part if you have any 

# Paths to the MOTD list and server.properties file
MOTD_LIST_PATH = ""
SERVER_PROPERTIES_PATH = ""

# The static part of your MOTD (If there isnt a MOTD part that you like to keep, leave blank,)
STATIC_PART = (
    
)

def get_random_word():
    with open(MOTD_LIST_PATH, "r") as file:
        motds = file.readlines()

    if not motds:
        raise ValueError("The MOTD list is empty!")

    return random.choice(motds).strip()

def update_server_properties(new_dynamic_part):
   
    new_motd = f"{STATIC_PART}{new_dynamic_part}"

    # Make sure Minecraft recognizes the new line correctly (IMPORTANT if you dont have a "static" MOTD delete the line bellow this commentary)
    new_motd = new_motd.replace("\n", "\\n")  
    #^^^^^^^^^^^^^^^^^^ delete if the previous comment mach your dessired use

    with open(SERVER_PROPERTIES_PATH, "r") as file:
        lines = file.readlines()

    with open(SERVER_PROPERTIES_PATH, "w") as file:
        for line in lines:
            if line.startswith("motd="):
                file.write(f"motd={new_motd}\n")
            else:
                file.write(line)

if __name__ == "__main__":
    try:
        dynamic_part = get_random_word()
        update_server_properties(dynamic_part)
        print(f"Updated MOTD with dynamic part: {dynamic_part}")
    except Exception as e:
        print(f"Error: {e}")
