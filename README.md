# ws-deploy

Vagrant + Ansible to configure Debian

## Usage

### Create your vault

Create a `host_vars/default/vault` with your config / secrets from
`host_vars/default/vault.template` by replacing the bits in `<>`.

#### (Optional): Rax specific configs

Follow steps in rax/roles/README.md

    git submodule init
    git submodule update
    less roles/rax/README.md

#### Encrypt your secrets

    ansible-vault encrypt host_vars/default/vault

### Build your VM

    vagrant up
