from P4 import P4, P4Exception

p4 = P4()

try:
    p4.connect()
    p4.exception_level = 2  # File(s) up-to-date is a warning
    files = p4.run_sync()

except P4Exception, ex:
    for w in p4.warnings:
        print w

finally:
    p4.disconnect()
