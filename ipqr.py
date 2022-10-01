import pyqrcode
import socket


def getIpAddress():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.connect(("8.8.8.8", 80))
	ipaddress = s.getsockname()[0]
	return ipaddress


def getQrCode():
	ip = f"http://{str(getIpAddress())}"
	url = pyqrcode.create(ip)
	url.png('ipqr.png', scale=6)
