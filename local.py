from invoke import run as local
from datetime import datetime

# A python script to run commands locally using local
# Example local("ls")


date = datetime.utcnow()
file = "versions/web_static_{}{}{}{}{}{}".format(date.year,
													date.month,
													date.day,
													date.hour,
													date.minute,
													date.second)

local("mkdir -p versions")
try:
	local("tar -czf {}.tgz web_static".format(file))
	print(file)
except Exception:
	print("Error")
