Php5-fpm
========

This role helps to install and configure php5-fpm and php modules.

Requirements
------------

This role requires ansible 1.4 or higher.

Role Variables
--------------

The variables that can be passed to this role and a brief description about them are as follows:

    php_ver: 5.6
    php5_modules: [common,curl,dev,gd,geoip,intl,mongo,mysql]
    php5_modules_deb: [mongodb,phalcon]
    php_modules: [pear]
    php_modules_pear:
      - name: twig
        pear: pear.twig-project.org
    php_modules_pecl:
      - name: igbinary
        repo: https://github.com/nicolasff/phpredis.git
        dest: phpredis
        configure: --enable-redis-igbinary
    php_modules_source:
      - name: phalcon
        version: 2.0.7
        repo: https://github.com/phalcon/cphalcon.git
        dest: phalcon
    php_fpm_conf:
      - name: global
        vars:
          - pid = /var/run/php5-fpm.pid
          - error_log = /var/log/php5-fpm/php5-fpm.log
          - log_level = warning
          - daemonize = yes
          - include=/etc/php5/fpm/pool.d/*.conf
    php_fpm_pools:
      - name: www
        vars:
          - user = www-data
          - group = www-data
          - listen = 127.0.0.1:9000
          - listen.backlog = 65536
          - pm = ondemand
          - pm.max_children = 250
          - pm.max_requests = 300
          - request_terminate_timeout = 300s
          - rlimit_files = 65536
          - rlimit_core = unlimited
          - chdir = /
          - php_flag[display_errors] = off
          - php_admin_value[error_log] = /var/log/php5-fpm/error.$pool.log
          - php_admin_flag[log_errors] = on
    php_config:
      - name: default
        vars:
          - expose_php = Off
          - cgi.fix_pathinfo = 0
          - max_execution_time = 300
          - memory_limit = 256M
          - post_max_size = 16M
          - upload_max_filesize = 2M
          - max_input_time = 300
          - short_open_tag = On

Dependencies
------------

Roles:
- dotdeb-list (optional)
- cloudmccloud-list (optional)

Example Playbook
----------------

    - hosts: servers
      roles:
        - { role: php5-fpm, tags: php5-fpm }

License
-------

BSD

Author Information
------------------

Created by Viacheslav Kuzmenko (oxygen@zeoalliance.com)
