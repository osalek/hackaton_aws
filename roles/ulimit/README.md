Ulimit
======

This role helps to configure ulimit.

Requirements
------------

This role requires ansible 1.4 or higher.

Role Variables
--------------

The variables that can be passed to this role and a brief description about them are as follows:

    ulimit_hard: 65536
    ulimit_soft: 65536

Variables 'ulimit_hard' and 'ulimit_soft' are default.

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
         - { role: ulimit, tags: ulimit }

License
-------

BSD

Author Information
------------------

Created by Viacheslav Kuzmenko (oxygen@zeoalliance.com)
