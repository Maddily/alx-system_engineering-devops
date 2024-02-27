# Install and configure Nginx server

exec { 'update':
        command => '/usr/bin/apt-get update',
}

package { 'nginx':
    ensure  => 'installed',
}

file {'/var/www/html/index.html':
    content => 'Hello World!'
}

exec {'redirect_me':
    command  => 'sed -i "46i\	rewrite ^/redirect_me https://www.example.com/ permanent;" /etc/nginx/sites-available/default',
    provider => 'shell'
}

service {'nginx':
    ensure  => running,
}
