import P4 
import daterime 
import travis-ci
from P4 import P4, P4Exception

p4 = P4()

try:
    p4.connect()
    p4.exception_level = 2  # Need Travis Infrastructure API keys.
    files = p4.run_sync()

except P4Exception, ex:
    for w in p4.warnings:
        print w
try:
    p4.connect()
    client = p4.fetch_client()
    client["Owner"] = p4.user
    p4.save_client(client)

except P4Exception:
    for e in p4.errors:
        print(e)
        
p4 = P4(kwargs**)
p4.connect()
spec = p4.run("client", "-o")[0]

if ( p4.is_ignored( "/home/montana-travis/workspace/config.txt" ):
  print "Ignored."
else:
  print "Not ignored."

change = p4.run_change("-o")[0]
    change["Description"] = "Autosubmitted changelist"
    p4.input = change
    p4.run_submit("-i")

now = datetime.now()
p4 = P4()

try:
  p4.connect()
  for client in p4.run_clients():
    atime = datetime.utcfromtimestamp( int( client[ "Access" ] ) )
    if ( atime + timedelta( 365 ) ) < now :
      p4.travis_ci( '-f', client[ "client" ] )

except P4Exception:
  for e in p4.errors:
    print e
