# ws-deploy

Vagrant + Ansible to configure Debian

## Usage

### Create your vault

#### Create your hashed login password

python -c \
    "from passlib.hash import sha512_crypt;\
     from getpass import getpass;\
     print(sha512_crypt.encrypt(getpass()));\
    "

#### Set your vault variables

Add the following lines to `host_vars/default/vault` (set values in <>):

    vault_user: <your_login_username>
    vault_password: <your_hashed_password>
    vault_real_name: <your_fullname>
    vault_email: <your_email>
    vault_openstack_user: <your_openstack_review_username>
    vault_gpg_private_key: |
      -----BEGIN PGP PRIVATE KEY BLOCK-----
      <your_private_key>
      -----END PGP PRIVATE KEY BLOCK-----
    vault_gpg_public_key: |
      -----BEGIN PGP PUBLIC KEY BLOCK-----
      <your_private_key>
      -----END PGP PUBLIC KEY BLOCK-----
    vault_ssh_private_key: |
      -----BEGIN RSA PRIVATE KEY-----
      <your_private_key>
      -----END RSA PRIVATE KEY-----
    vault_ssh_public_key: <your_public_key>

#### (Optional): Rax specific configs

Follow steps in rax/roles/README.md

    git submodule init
    git submodule update
    less roles/rax/README.md

#### Encrypt your secrets

    ansible-vault encrypt host_vars/default/vault

### Build your VM

    cd vagrant
    vagrant up
