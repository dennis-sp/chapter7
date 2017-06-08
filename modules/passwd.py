def run():
	with open('/etc/passwd', 'r') as f:
		data = f.read()
		return str(data)
