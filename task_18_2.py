import yaml
from netmiko import ConnectHandler


def send_config_commands(device, config_commands):
    # 1. open the connection with a "with" block
    # 2. enter enable mode
    # 3. send the commands with send_config_set
    # 4. return the output
    pass


if __name__ == "__main__":
    commands = [
        "logging 10.255.255.1",
        "logging buffered 20010",
        "no logging console",
    ]
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    for dev in devices:
        print(send_config_commands(dev, commands))