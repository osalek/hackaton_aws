Mongos
======

This role helps to install and configure mongos. Supported versions 2.4.x-3.2.x.

Requirements
------------

This role requires ansible 1.4 or higher.

Role Variables
--------------

The variables that can be passed to this role and a brief description about them are as follows:

    mongos:
      - name: mongos_account
        configdb: cfg1.account:27019,cfg2.account:27019,cfg3.account:27019
        ip: 192.168.0.1
        port: 27017
        logpath: /var/log/mongodb/mongos-account.log
        auth: x509
        replset: rs_account_config

Variables 'mongos.ip' and 'mongos.port' are optional.  
Variables 'mongos.auth' and 'mongos.replset' are not obligatory.  
Default values for optional variables:

    ip: 127.0.0.1
    port: 27017

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
        - { role: mongos, tags: mongos }

License
-------

BSD

Author Information
------------------

Created by Viacheslav Kuzmenko (oxygen@zeoalliance.com)
