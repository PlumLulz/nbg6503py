import hashlib
import argparse

def nbg6503(serial):
	serial = serial[1:]
	digest = hashlib.md5()
	digest.update(serial.encode())
	digest_hex = digest.hexdigest()
	key = digest_hex[0:13].upper()
	print(key)


parser = argparse.ArgumentParser(description='Zyxel NBG6503 Keygen')
parser.add_argument('serial', help='Serial Number')
args = parser.parse_args()

nbg6503(args.serial)