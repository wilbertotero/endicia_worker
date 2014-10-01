import xmlrpclib
from pydicia import *
import time
from xml.dom.minidom import parse, parseString
import xml.etree.ElementTree as ET


#def status():
proxy = xmlrpclib.ServerProxy("https://www.endicia.com/ELS/ELSServices.cfc?")
#count = 0
#b = Batch()
#b.etree
b = ET.fromstring('''
   <TransactionsListingRequest>
        <AccountID></AccountID>
        <PassPhrase></PassPhrase>
        <Test>Y</Test>
        <TransactionType></TransactionType>
        <StartDate></StartDate>
        <StartTime></StartTime>
        <EndDate></EndDate>
        <EndTime></EndTime>
        <Results></Results>
        <ToZipCode></ToZipCode>
        <FromAddress></FromAddress>
        <TrackingList>
            <PICNumber>9400109699937126318047</PICNumber>
            <PieceID></PieceID>
            <CustomsID></CustomsID>
        </TrackingList>
    </TransactionsListingRequest>''')
#while True:                        
    #b.add_package(ToName('Some Body'),DAZzle.Test)
    #print b.tostring()
#    ++count
value = proxy.GetTransactionsListing(9400109699937126318047)
#tree = ET.fromstring(value)
print 'Status:',value.find('Status').text

#    if count == 7:
#        break
    
#    time.sleep(5)

#status();

