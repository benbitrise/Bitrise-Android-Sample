import telnetlib
import sys
import re

host = "localhost"
port = "5554"

telnet = telnetlib.Telnet(host, port)

auth_token = sys.argv[1]
print(auth_token)

#result = telnet.read_until(str.encode("Authentication Required"), 3)
#print(result.decode("utf-8"))
telnet.expect([re.compile(b"Android Console: you can find your <auth_token> in ")], 3)
telnet.write(bytes("auth " + auth_token + "\n", 'utf-8'))

telnet.write(bytes("geo fix {0} {1}\n".format(10, 20), 'utf-8'))
result = telnet.read_until(b"OK", 3)
print("1")
print(telnet.read_lazy().decode("utf-8"))
accel_point=[4,3,1]
telnet.write(bytes("sensor set acceleration {0}:{1}:{2}\n".format(accel_point[0],accel_point[1],accel_point[2]), 'utf-8'))
result = telnet.read_until(b"OK", 3)
print("2")
print(telnet.read_lazy().decode("utf-8"))
telnet.write(bytes("sensor status\n", 'utf-8'))
result = telnet.read_until(b": enabled", 3)
print("3")
print(telnet.read_lazy().decode("utf-8"))

telnet.write(bytes("sensor get acceleration\n", 'utf-8'))
result3 = telnet.read_until(b"acceleration = 4:3:1", 3)
print("4")
print(result3.decode("utf-8"))
bla = result3.decode("utf-8")
if "4:3:1" not in bla:
    raise Exception("expected acceleration not present")
