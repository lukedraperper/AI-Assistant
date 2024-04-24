from O365 import Account, MSGraphProtocol

CLIENT_ID = '6db01545-2751-47cd-88ff-749540df44a7'
SECRET_ID = 'd523632a-00b7-4fa2-927a-bda6ad093b10'

credentials = (CLIENT_ID, SECRET_ID)

protocol = MSGraphProtocol() 
#protocol = MSGraphProtocol(defualt_resource='<sharedcalendar@domain.com>') 
scopes = ['Calendars.Read.Shared']
account = Account(credentials, protocol=protocol)

if account.authenticate(scopes=scopes):
   print('Authenticated!')