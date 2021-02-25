import NetpingRelay
import time

relay = NetpingRelay.NetpingRelay("10.0.0.56")

# cheking socket status
err = relay.check_connection()
if isinstance(err, str):
    print(err)
    relay = None

if relay:
    print(f'relay1 status: {relay.get_state(1)}')
    time.sleep(1)
    relay.reset_socket(1, 2)

while True:
    print(f'relay1 status: {relay.get_state(1)}')
    time.sleep(1)
