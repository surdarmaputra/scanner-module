import os
from w3af_api_client import Connection, Scan
import helper

printLog = helper.printLog
parent_dir = '/home/jiwa/tugasakhir/'

def initConnection(scannerUrl):
	printLog("Initialize connection with scanner at ", scannerUrl)
	conn = Connection(scannerUrl)
	printLog("Version: ", conn.get_version())
	return conn

def startScanner(conn, targetUrl):
	scan = Scan(conn)
	scanProfilePath = os.path.join(parent_dir, "w3af/profiles/OWASP_TOP10.pw3af")
	scanProfile = file(scanProfilePath).read()
	targetUrls = [targetUrl]

	printLog("")
	printLog("Starting scanner for target ", targetUrl)
	scan.start(scanProfile, targetUrls)

	scan.get_urls()
	scan.get_log()
	scan.get_findings()
	return;

def initTask(scannerUrl, targetUrl):
	conn = initConnection(scannerUrl)
	startScanner(conn, targetUrl)
	return

def main():
	print "Please use this program as plug-in. Thanks!"

if __name__ == "__main__":
	main()
