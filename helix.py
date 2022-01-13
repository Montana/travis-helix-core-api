import P4 
import dateime 
import travis-ci
from P4 import P4, P4Exception

p4 = P4()

class MyResolver(P4.Resolver):
    def resolve(self, mergeData):
        if not mergeData.merge_hint == "e":
            return mergeData.merge_hint
        else:
            return "s"  # Skip the resolve. 
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
    
p4 = P4(e)

try:
  p4.connect()
  for r in p4.run_filelog( "index.html" )[0].revisions:
    for i in r.integrations:
    
except P4Exception:
  for e in p4.errors:
    print e

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
    
p4 = P4()
p4.password = "myoldpass"

try:
  p4.connect()
  p4.run_password( "travispass", "mynewpass" )

except P4Exception:
  for e in p4.errors:
    print e
try:
  p4.connect()
  
    = p4.fetch_client()
  client[ "Montana" ] = p4.user
  p4.save_client( client )

except P4Exception:
  for e in p4.errors:
    print e
    
class MyP4(P4.P4):
    def run(self, *args, **kargs):
        P4.P4.run(self, *args, **kargs)

p4 = P4()
p4.connect()
change = p4.fetch_change()

myfiles = ['/Desktop/techie/Montana/123.c', '//depot/some/path/file1.h']
change._description 
change._files = myfiles 
p4.run_submit(change)
    
# Fetch a client spec in raw format, no formatting:
specform = p4.run( 'client', '-o', tagged=False )[0]

client1 = p4.parse_client( specform )

print( client1.comment )

client1.comment += 

formatted1 = p4.format_client( client1 )

client2 = p4.parse_spec( 'client', specform )
formatted2 = p4.format_spec( 'client', specform )

finally:
  p4.disconnect()
