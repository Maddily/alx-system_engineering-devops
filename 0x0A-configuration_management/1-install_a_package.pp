# Ensure Python 3.8.10 is installed

package { 'python3.8':
  ensure => '3.8.10',
}

# Install flask from pip3

package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

# Ensure Werkzeug 2.1.1 is installed

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
