import ipinfo
access_token = '123456789abc'
handler = ipinfo.getHandler(access_token)
ip_address = '216.239.36.21'
details = handler.getDetails(ip_address)
details.city
'Mountain View'
details.loc
'37.3861,-122.0840'
