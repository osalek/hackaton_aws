Nagios3
=======

This role helps to install and configure the nagios3 server.

Requirements
------------

This role requires ansible 1.4 or higher.

Role Variables
--------------

The variables that can be passed to this role and a brief description about them are as follows:

** Master host

    nagios3:
      group:
        looxy:
          contacts: duty,looxy
        office:
          contacts: duty,office
        unix1:
          contacts: duty,unix1
        unix2:
          contacts: duty,unix2
      contact:
        - name: eney
          alias: Eney
          email: eney@zeoalliance.com
        - name: ewo
          alias: Ewo
          email: ewo@zeoalliance.com
        - name: firs
          alias: Firs
          email: firs@zeoalliance.com
        - name: ginlitvin
          alias: Ginlitvin
          email: ginlitvin@zeoalliance.com
        - name: ike
          alias: Ike
          email: ike@zeoalliance.com
        - name: jimi
          alias: Jimi
          email: jimi@zeoalliance.com
        - name: knyaz
          alias: Knyaz
          email: knyaz@zeoalliance.com
        - name: koffu
          alias: Koffu
          email: koffu@zeoalliance.com
        - name: lamer
          alias: Lamer
          email: lamer@zeoalliance.com
        - name: osalek
          alias: Osalek
          email: osalek@zeoalliance.com
        - name: oxygen
          alias: Oxygen
          email: oxygen@zeoalliance.com
        - name: vbakan
          alias: Vbakan
          email: vbakan@zeoalliance.com
        - name: zimin
          alias: Zimin
          email: zimin@zeoalliance.com
      contactgroup:
        - name: duty
          alias: Duty Administrators
          members: ewo,ginlitvin,ike,jimi,osalek,zimin
        - name: looxy
          alias: Looxy Administrators
          members: vbakan
        - name: office
          alias: Office Administrators
          members: eney,lamer
        - name: unix1
          alias: Unix Administrators
          members: knyaz,oxygen
        - name: unix2
          alias: Unix Administrators
          members: firs,koffu


** Slave host

    nagios3:
      group:
        looxy:
          contacts: duty,looxy
        office:
          contacts: duty,office
        unix1:
          contacts: duty,unix1
        unix2:
          contacts: duty,unix2
      contact:
        - name: eney
          alias: Eney
          email: eney@zeoalliance.com
        - name: ewo
          alias: Ewo
          email: ewo@zeoalliance.com
        - name: firs
          alias: Firs
          email: firs@zeoalliance.com
        - name: ginlitvin
          alias: Ginlitvin
          email: ginlitvin@zeoalliance.com
        - name: ike
          alias: Ike
          email: ike@zeoalliance.com
        - name: jimi
          alias: Jimi
          email: jimi@zeoalliance.com
        - name: knyaz
          alias: Knyaz
          email: knyaz@zeoalliance.com
        - name: koffu
          alias: Koffu
          email: koffu@zeoalliance.com
        - name: lamer
          alias: Lamer
          email: lamer@zeoalliance.com
        - name: osalek
          alias: Osalek
          email: osalek@zeoalliance.com
        - name: oxygen
          alias: Oxygen
          email: oxygen@zeoalliance.com
        - name: vbakan
          alias: Vbakan
          email: vbakan@zeoalliance.com
        - name: zimin
          alias: Zimin
          email: zimin@zeoalliance.com
      contactgroup:
        - name: duty
          alias: Duty Administrators
          members: ewo,ginlitvin,ike,jimi,osalek,zimin
        - name: looxy
          alias: Looxy Administrators
          members: vbakan
        - name: office
          alias: Office Administrators
          members: eney,lamer
        - name: unix1
          alias: Unix Administrators
          members: knyaz,oxygen
        - name: unix2
          alias: Unix Administrators
          members: firs,koffu
      master: nagios.ca.cloudmccloud.com

    nagios3_htpasswd:
      - user: nagiosadmin
        password: nagiosadmin

Dependencies
------------

Roles:
- nginx
- php5-fpm
- ulimit

Example Playbook
----------------

    - hosts: servers
      roles:
        - { role: nagios3, tags: nagios3 }

License
-------

BSD

Author Information
------------------

Created by Viacheslav Kuzmenko (oxygen@zeoalliance.com)
