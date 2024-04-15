# This Puppet manifest modifies the OS configuration to enable the
# holberton user to log in without encountering "Too many open files" errors.

exec { 'increase-file-limits-for-holberton-user':
  command => 'sed -i "/holberton/s/5/50000/;/holberton/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
