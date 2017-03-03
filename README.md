# ws-deploy

Vagrant + Ansible to configure Debian

## Usage

### Requirements and setup

1. Virtualbox: https://www.virtualbox.org/wiki/Downloads
   * Debian: `sudo apt-get install virtualbox`
   * OS X: `brew cask install virtualbox`
1. Vagrant: https://www.vagrantup.com/downloads.html
   * Debian: `sudo apt-get install vagrant`
   * OS X: `brew cask install vagrant`
1. Vagrant vbquest plugin: `vagrant plugin install vagrant-vbguest`
1. Ansible: http://docs.ansible.com/ansible/intro\_installation.html
   * Debian: `sudo apt-get install ansible`
   * OS X: `brew install ansible`
1. Python requirements: `pip install -r requirements.txt`
1. Create VM share directory: `mkdir -p ~/Documents/dev-vm-share`

### Create your vault

Create a `host_vars/default/vault` from `host_vars/default/template.vault`
by replacing the bits in `<>` with your config values / secrets.

#### (Optional): Rax specific configs

Follow steps in rax/roles/README.md

    git submodule init
    git submodule update
    view roles/rax/README.md

#### Encrypt your secrets

    ansible-vault encrypt host_vars/default/vault

### Build your VM

    vagrant up

### GUI

* Shutdown the VM.
* Retinal displays: enable HiDPI support in VirtualBox display options.
* Boot the VM to launch the login manager.
* Maximize; then login for fullscreen hi-res UI.

