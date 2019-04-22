#!/usr/bin/env python

def main():
	f = open("MAC_out.txt", "r")
	WIFICredentials = ""
	for x in f:
		WIFICredentials += x
	f.close()
	segmented = WIFICredentials.splitlines()
	segmentedLines = len(segmented)
	IPLine = 0
	#Go through segmented as many lines as there are
	for x in range(segmentedLines):
		#foundIndex will be -1 if B8:27:EB is not found and the character index if it was found
		foundIndex = segmented[x].find("B8:27:EB")		
		if foundIndex >= 0:
			#the line of the IP is 2 lines before the MAC address
			IPLine = x - 2
			#rpiMAC will hold the MAC address of the found rpi
			rpiMAC = segmented[x][foundIndex : foundIndex + 17]
	print rpiMAC
	rpiIP = ""

	#The commented section is another way to parse for the IP address
	########################################################################################
	#segmented[IPLine] += "\n"
	#endOfLine = segmented[IPLine].find("\n")
	#rpiIP = segmented[IPLine][21 : endOfLine]
	########################################################################################

	#The following is a way to parse the listed string to find the IP address
	for x in segmented[IPLine][21 : ]:
		rpiIP += x
	print rpiIP

	f = open("PIIP.txt", "w")
	f.write(rpiIP)
	f.close()
	return rpiMAC

if __name__=="__main__":
	main()


