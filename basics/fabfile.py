from fabric.api import task,local,run

@task
def localtime():
	local("date")

@task
def remotetime():
	run("date")

def private():
	print("private method")