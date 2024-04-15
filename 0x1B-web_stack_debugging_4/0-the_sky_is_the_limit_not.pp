# This Puppet manifest enhances the capacity of an Nginx server
# to handle traffic by adjusting the ULIMIT settings in the default
# configuration file and subsequently restarting the Nginx service.

exec { 'fix_and_restart_nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx && nginx restart',
  path    => ['/usr/local/bin', '/bin', '/etc/init.d'],
}
