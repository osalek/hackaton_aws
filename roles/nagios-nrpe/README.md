Nagios-nrpe
===========

This role helps to install and configure nagios-nrpe-server.

Requirements
------------

This role requires ansible 1.4 or higher.

Role Variables
--------------

The variables that can be passed to this role and a brief description about them are as follows:

Default values for variables:

    nagios_nrpe_allowed_hosts: 127.0.0.1,67.205.74.104,72.251.246.230
    nagios_nrpe_plugins:
      - name: check_all_disks
        command: check_disk
        options: -w '20%' -c '10%' -e

Typical variables for other services:

** Arbiter

    - name: check_arbiter
      command: check_tcp
      options: -H 127.0.0.1 -p 27017

** Disk space

    - name: check_all_disks
      command: check_disk
      options: -w '20%' -c '10%' -e

** Gearman nrpe

    - name: check_gearman
      command: check_gearman
      options: 127.0.0.1

** Haproxy nrpe

    - name: check_haproxy
      command: check_haproxy
      options: -u http://127.0.0.1:8181/\;csv

    - name: check_haproxy
      command: check_haproxy
      options: -u http://174.142.113.21:88/\;csv -U iweb -P f8C2c3RP

** Mongodb nrpe

    - name: check_mongodb_connect
      command: check_mongodb.py
      options: -H db1.account -A connect -P 27017 -W 2 -C 4
    - name: check_mongodb_connections
      command: check_mongodb.py
      options: -H db1.account -A connections -P 27017 -W 70 -C 80
    - name: check_mongodb_replication_lag
      command: check_mongodb.py
      options: -H db1.account -A replication_lag -P 27017 -W 15 -C 30
    - name: check_mongodb_lock
      command: check_mongodb.py
      options: -H db1.account -A lock -P 27017 -W 5 -C 10
    - name: check_mongodb_replset_state
      command: check_mongodb.py
      options: -H db1.account -A replset_state -P 27017 -W 0 -C 0
    - name: check_mongodb_flushing
      command: check_mongodb.py
      options: -H db1.account -A flushing -P 27017 -W 100 -C 200
    - name: check_mongodb_last_flush_time
      command: check_mongodb.py
      options: -H db1.account -A last_flush_time -P 27017 -W 200 -C 400

** Mongodb 3.0 nrpe

    - name: check_mongodb3_connect
      command: check_mongodb.py
      options: -M 3 -H db1.account -A connect -P 27017 -W 2 -C 4
    - name: check_mongodb3_connections
      command: check_mongodb.py
      options: -M 3 -H db1.account -A connections -P 27017 -W 70 -C 80
    - name: check_mongodb3_replication_lag
      command: check_mongodb.py
      options: -M 3 -H db1.account -A replication_lag -P 27017 -W 15 -C 30
    - name: check_mongodb3_replset_state
      command: check_mongodb.py
      options: -M 3 -H db1.account -A replset_state -P 27017 -W 0 -C 0

** Mongos

    - name: check_mongos
      command: check_tcp
      options: -H 127.0.0.1 -p 27017

** Mongos multi

    - name: check_mongos_27017
      command: check_tcp
      options: -H 127.0.0.1 -p 27017
    - name: check_mongos_27018
      command: check_tcp
      options: -H 127.0.0.1 -p 27018

** Mongos status

    - name: check_mongos_status
      command: check_mongos.py

** NFS

    - name: check_nfs_mount
      command: check_mountpoints.py

** Open files descriptor

    - name: check_ofd
      command: check_nofile_limit.sh

** Mdadm raid

    - name: check_raid
      command: check_raid

** Redis

    - name: check_redis
      command: check_redis.pl
      options: -H 127.0.0.1 -p 6379

** Rabbitmq

    - name: check_rabbitmq
      command: check_rabbitmq_server
      options: -H stage1-redis1 --port 15672 --user monit --password Ok6yoseiv5Oh

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
        - { role: nagios-nrpe, tags: nagios-nrpe }

License
-------

BSD

Author Information
------------------

Created by Viacheslav Kuzmenko (oxygen@zeoalliance.com)
