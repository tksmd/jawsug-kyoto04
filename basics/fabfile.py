from fabric.api import task,local,run,hosts,env

env.use_ssh_config = True
env.ssh_config_path = 'ssh.config'

@task
def localtime():
	local("date")

@task
def remotetime():
	run("date")

def private():
	print("private method")