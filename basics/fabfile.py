from fabric.api import local

def whoami():
    local("who am i")
