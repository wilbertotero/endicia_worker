from SOAPpy import WSDL          
import xmlrpclib
import time

#
#Method: transaction
#Description: Test the if a package has been refunded

def transaction(pic_number):
    wsdlFile = 'https://www.endicia.com/ELS/ELSServices.cfc?wsdl'
    server = WSDL.Proxy(wsdlFile)    
    count = 0;
    
    # print server.methods.keys() 
    # callInfo = server.methods['GetTransactionsListing']
    # print callInfo.inparams
    # print callInfo.inparams[0].name
    # print callInfo.inparams[0].type
    # 
    # print callInfo.outparams
    # print callInfo.outparams[0].name 
    # print callInfo.outparams[0].type
    
    #The value 9400109699937126318047 was inserted by default but can be sent through the method
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
 
    print b
    
    try:
        while True:
            count += 1
            
            xml = server.GetTransactionsListing(b)
            print xml
            refund_code = xml['TransactionsListingResponse']['TransactionResults']['Transaction']['RefundCode']
            
            if refund_code in ['A','C', 'S', 'U', 'M']:
                print 'Package has been refunded' + refund_code
                break;
            
            elif refund_code == 'R':
                print 'Package has been rejected' + refund_code
            else:
                print 'Package is pending for refund' + refund_code
            
            if count == 7: # testint the 7 times       
                break
            
            time.sleep(1) #it can be changed to more second - just to see results of the exercise
      
    except xmlrpclib.ProtocolError as err:
        print "A protocol error occurred"
        print "URL: %s" % err.url
        print "HTTP/HTTPS headers: %s" % err.headers
        print "Error code: %d" % err.errcode
        print "Error message: %s" % err.errmsg

transaction('9400109699937126318047')
    
