# Import Modules
import subprocess
import time

# Creating function
def do():
    # Getting the meta-data
    meta_data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])

    # Decoding the meta-data
    data = meta_data.decode('utf-8', errors="backslashreplace")

    # Split the  meta-data into separate lines
    data = data.split('\n')

    # Create a list/directory of the wireless networks
    profiles = []

    for i in data:
        # find "All User Profile"
        if "All User Profile" in i :

            # if found, split the item
            i = i.split(":")

            i = i[1]

            i = i[1:-1]
            # Appending the wifi name in the list
            profiles.append(i)

    print("{:<30}| {:<}".format("Wi-Fi Name", "Password"))
    print("----------------------------------------------")

    for i in profiles:
        results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile' ,i,'key=clear'])

        results = results.decode('utf-8', errors="backslashreplace")
        results = results.split('\n')

        results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]

        try:
            print("{:<30}| {:<}".format(i, results[0]))

        # else it will print blank in front of pass word
        except IndexError:
            print("{:<30}| {:<}".format(i, ""))

        # called when this process get failed
        except subprocess.CalledProcessError:
            print("Encoding Error Occured")

# Calling the function
do()

# after the code finishes being executed it will wait for 300secs till the program closes
print("-"*20,"Search has ended!!!","-"*20)

# Total time taken by the program before it closes after completing
time.sleep(300)


