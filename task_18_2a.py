import yaml  # reads the devices.yaml file
from netmiko import ConnectHandler  # connects to network devices


# log=True means: if nobody passes log, it is True by default
def send_config_commands(device, config_commands, log=True):
    # device["host"] reads the IP address from the dictionary
    if log:  # only runs when log is True
        print(f"Connecting to {device['host']}...")  # f-string puts the IP into the text
    with ConnectHandler(**device) as ssh:  # open the SSH connection (closes automatically)
        ssh.enable()  # go into enable mode
        output = ssh.send_config_set(config_commands)  # send the whole list of config commands
    return output  # give the result back to the caller


if __name__ == "__main__":
    # the list of configuration commands to send
    commands = [
        "logging 10.255.255.1",
        "logging buffered 20010",
        "no logging console",
    ]
    with open("devices.yaml") as f:  # open the file with the device list
        devices = yaml.safe_load(f)  # turn the YAML text into a Python list of dictionaries
    for dev in devices:  # repeat for each device
        print(send_config_commands(dev, commands))  # log is True by default here