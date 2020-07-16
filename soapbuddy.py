import urllib3

class SoapClient:
    def __init__(self, wsdl_url):
        http = urllib3.PoolManager()
        r = http.request(
            "GET",
            wsdl_url,
            preload_content=False
        )

        wsdl_bytes = b''
        # The WSDL document might be pretty large, so we take it in chunks,
        # rather than all at once.
        for chunk in r.stream(32):
            wsdl_bytes += chunk
        self._wsdl_raw_text = wsdl_bytes.decode("utf-8")




my_soap_client = SoapClient("http://www.soapclient.com/xml/soapresponder.wsdl")
print(my_soap_client._wsdl_raw_text)
