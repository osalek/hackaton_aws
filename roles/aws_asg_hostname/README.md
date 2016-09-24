Aws_asg_hostname
================

This role helps to setup hostname for autoscaling host.

Requirements
------------

This role requires ansible 1.4 or higher.

Role Variables
--------------

The variables that can be passed to this role and a brief description about them are as follows:

    aws_asg_hostname_prefix: app
    aws_asg_hostname_domain: example.com

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
        - { role: aws_asg_hostname, tags: aws_asg_hostname }

License
-------

BSD

Author Information
------------------

Created by Viacheslav Kuzmenko (oxygen@zeoalliance.com)
