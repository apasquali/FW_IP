import netmiko
import getpass

usrname = raw_input("Username: ")
pswd = getpass.getpass('Password:')

FileIn = open('ip_fw_all.txt', 'r')
FileOut = open('results.txt','w')
device = FileIn.readline().strip()

while (device != ""):
	
	cisco_asa = {
	'device_type': 'cisco_ios',
	'ip':   device,
	'username': usrname,          
	'password': pswd,
	'secret': pswd,
	}

	SSHClass = netmiko.ssh_dispatcher(cisco_asa['device_type'])
	try:
		net_connect = SSHClass(**cisco_asa)
		output1 = net_connect.send_command("show version | in Serial")
		#net_connect.send_command(" ")
		#output2 = net_connect.send_command("failover exec standby sh ver | in Serial")
		results = device + ',' + output1[15:] + '\n'
		print results
		FileOut.write(results)
		net_connect.disconnect()
	except:
		print "Issues with " + device
		results = device + ',Issues' + '\n'
		FileOut.write(results)
	
	device = FileIn.readline().strip()

FileIn.close()
FileOut.close()