import netifaces
#interface indetifiers#

netifaces.interfaces()
['lo0', 'gif0', 'stf0', 'en0', 'en1', 'fw0']

#particular interface#
netifaces.ifaddresses('lo0')
#{18: [{'addr': ''}], 2: [{'peer': '127.0.0.1', 'netmask': '255.0.0.0', 'addr': '127.0.0.1'}], 30: [{'peer': '::1', 'netmask': 'ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff', 'addr': '::1'}, {'peer': '', 'netmask': 'ffff:ffff:ffff:ffff::', 'addr': 'fe80::1%lo0'}]}


netifaces.AF_LINK
#18

addrs = netifaces.ifaddresses('lo0')
addrs[netifaces.AF_INET]
	#[{'peer': '127.0.0.1', 'netmask': '255.0.0.0', 'addr': '127.0.0.1'}]


addrs = netifaces.ifaddresses('en0')
addrs[netifaces.AF_INET]
		#[{'broadcast': '10.15.255.255', 'netmask': '255.240.0.0', 'addr': '10.0.1.4'}, {'broadcast': '192.168.0.255', 'addr': '192.168.0.47'}]


addrs[netifaces.AF_LINK]
		#[{'addr': '00:12:34:56:78:9a'}]

#Mac Address#
addrs = netifaces.ifaddresses('en0')
addrs[netifaces.AF_LINK]
		#[{'addr': '00:12:34:56:78:9a:bc:de'}]


netifaces.gateways()
		#{2: [('10.0.1.1', 'en0', True), ('10.2.1.1', 'en1', False)], 30: [('fe80::1', 'en0', True)], 'default': { 2: ('10.0.1.1', 'en0'), 30: ('fe80::1', 'en0') }}

gws = netifaces.gateways()
gws['default'][netifaces.AF_INET]
		#('10.0.1.1', 'en0')

def get_interface(): 
	return netifaces.interfaces()

def get_mac(interface):
	Mac_Address = ""
	return Mac_Address

def get_ips(interface):
	Ip_dict = ()
	Ipv4 = ipv4(iface)
	Ip_dict[ipv4] = ipv4
	Ipv6 = ipv6(iface)
	Ip_dict[ipv6] = ipv6
	Return Ip_dict
   # Returns: (dict)
    {'v4': ipaddress.IPv4Address('192.168.65.48'),
     'v6': ipaddress.IPv6Address('fe80::14e1:8686:e720:57a')}
    
      

def get_netmask(interface):
	ip_dict = ()
	Ipv4 = ipv4(Address)
	ip_dict[ipv4] = ipv4
	Ipv6 = ipv6(Address)
	ip_dict[ipv6] = ipv6
	Return ip_dict
	
	{'v4': ipaddress.IPv4Address('255.255.255.0'),
     'v6': ipaddress.IPv6Address('ffff:ffff:ffff:ffff::')}
	Print()
def get_network(interface):
	Ip_dict = ()
	Ipv4 = ipv4()
	Ip_dict[ipv4] = ipv4
	Ipv6 = ipv6(iface)
	Ip_dict[ipv6] = ipv6
	Return Ip_di
	print()

	{'v4': ipaddress.IPv4Network('192.168.65.0/24'),
     'v6': ipaddress.IPv6Network('fe80::/64')}