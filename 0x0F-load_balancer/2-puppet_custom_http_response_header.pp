# Install and configure Nginx server

exec { 'update packages':
  command => '/usr/bin/apt-get update',
  before  => package['nginx'],
}

package { 'nginx':
  ensure => 'present',
  before => file_line['add_header'],
}

file_line { 'add_header':
  path   => '/etc/nginx/nginx.conf',
  match  => 'http {',
  line   => "http {\n\tadd_header X-Served-By \"${hostname}\";",
  before => exec['restart server'],
}

exec { 'restart server':
  command => '/usr/sbin/service nginx restart',
}
