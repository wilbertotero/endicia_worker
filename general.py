from SOAPpy import WSDL          
import xmlrpclib
import time

#
#Method: transaction
#Description: Test the if a package has been refunded

def transaction(server, pic_number):

    b = '''
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
                <PICNumber>'''+pic_number+'''</PICNumber>
                <PieceID></PieceID>
                <CustomsID></CustomsID>
            </TrackingList>
        </TransactionsListingRequest>'''
      
    try:
        
        xml = server.GetTransactionsListing(b)
        #print xml
        refund_code = xml['TransactionsListingResponse']['TransactionResults']['Transaction']['RefundCode']
        
        return refund_code
      
    except xmlrpclib.ProtocolError as err:
        print "A protocol error occurred"
        print "URL: %s" % err.url
        print "HTTP/HTTPS headers: %s" % err.headers
        print "Error code: %d" % err.errcode
        print "Error message: %s" % err.errmsg


wsdlFile = 'https://www.endicia.com/ELS/ELSServices.cfc?wsdl'
#username = 'username'
#password = 'password'

server = WSDL.Proxy(wsdlFile)    
#session = server.login(username, password)

refund_code = transaction(server, '9400109699937126318047')


if refund_code in ['A','C', 'S', 'U', 'M']:
    print 'Package has been refunded' + refund_code
elif refund_code == 'R':
    print 'Package has been rejected' + refund_code
else:
    print 'Package is pending for refund' + refund_code
    
