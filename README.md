# ws-deploy

Vagrant + Ansible to configure Debian

## Usage

### Requirements

1. Virtualbox: https://www.virtualbox.org/wiki/Downloads
1. Vagrant: https://www.vagrantup.com/downloads.html
1. Vagrant vbquest plugin: `vagrant plugin install vagrant-vbguest`
1. Python requirements: `pip install -r requirements.txt`

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
