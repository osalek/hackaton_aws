Mongodb
=======

This role helps to install and configure mongodb server. Supported versions 2.4.x-3.2.x.

Requirements
------------

This role requires ansible 1.4 or higher.

Role Variables
--------------

The variables that can be passed to this role and a brief description about them are as follows:

** EXAMPLE 1

    mongodb:
      version: 2.6.5
      bind:
        ip: 127.0.0.1
        port: 27017
      path:
        db: /var/lib/mongodb
        log: /var/log/mongodb/mongod.log
      replication: false
      rsyslog: false
      replset:
        name: rs0
        primary: "localhost"
        secondary: []

** EXAMPLE 2

    mongodb:
      version: 2.6.5
      path:
        db: /data/mongodb
        log: /var/log/mongodb/mongod.log
      replication: true
      rsyslog: true
      replset:
        name: sh1_mb
        primary: db1.sh1.mb
        secondary: [db2.sh1.mb, db3.sh1.mb]

** EXAMPLE 3

    mongodb:
      version: 3.0.6
      engine:
        storage: wiredTiger
        cachesize: 18
      path:
        db: /data/mongodb
        log: /var/log/mongodb/mongod.log
      replication: true
      replset:
        name: sh1_mb
        primary: db1.sh1.mb
        secondary: [db2.sh1.mb, db3.sh1.mb]
      auth:
        type: x509

Variables 'mongodb.bind', 'mongodb.rsyslog', 'mongodb.auth' and 'mongodb.engine' are not obligatory.  
Default values for optional variables:

    bind:
      ip: 0.0.0.0
      port: 27017
    rsyslog: false

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
        - { role: mongodb, tags: mongodb }

License
-------

BSD

Author Information
------------------

Created by Viacheslav Kuzmenko (oxygen@zeoalliance.com)
