Nginx
=====

This role helps to install and configure the nginx.

Requirements
------------

This role requires ansible 1.4 or higher.

Role Variables
--------------

The variables that can be passed to this role and a brief description about them are as follows:

** global

    nginx_branch: stable
    nginx_user: www-data
    nginx_worker_processes: auto
    nginx_worker_priority: -5
    nginx_timer_resolution: 100ms
    nginx_worker_rlimit_nofile: 20512
    nginx_max_clients: 1024
    nginx_default_port: 80

** fastcgi_params

    nginx_fastcgi_params:
      template: default

    nginx_fastcgi_params:
      template: custom
      options:
        - fastcgi_param  HTTP_SCHEME        $http_x_forwarded_scheme
        - fastcgi_param  REMOTE_ADDR        $http_x_forwarded_for
        - fastcgi_param  X-Forwarded-For    $http_x_forwarded_for

** http_params

    nginx_http_params:
      - server_tokens off
      - sendfile on
      - tcp_nopush on
      - keepalive_timeout 65
      - tcp_nodelay on
      - client_max_body_size 50m
      - gzip off

    nginx_stub_status: 'on'
    nginx_stub_status_ip:
      - { perm: allow, ip: 127.0.0.1 }

** upstreams

    nginx_upstreams:
      - name: www-data
        template: fpm-port
        port: 9000
        state: present
      - name: user
        template: fpm-port
        port: 9001

** vhosts

    nginx_vhosts:
      - name: default
        template: default
      - name: account.example.com
        template: example_01
        state: present
      - name: example.com
        aliases: www.example.com
        template: example_02
        root: app
        upstream: www-data
        ssl: example.com
      - name: example.com
        template: redirect
        redirect: example.net

** htpasswd

    nginx_htpasswd:
      - user: username
        password: superpass

Variables 'root', 'upstream' and 'state' are optional.  
Default values for optional variables:

    root: {{ name }}
    upstream: fpm
    state: present

Dependencies
------------

None

Example Playbook
----------------

    - hosts: servers
      roles:
        - { role: nginx, tags: nginx }

License
-------

BSD

Author Information
------------------

Created by Viacheslav Kuzmenko (oxygen@zeoalliance.com)
