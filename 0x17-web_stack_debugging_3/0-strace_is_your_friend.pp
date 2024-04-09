# Manage the content of wp-settings.php file,
# replacing .phpp with .php
file { '/var/www/html/wp-settings.php':
    ensure  => present,
    content => file('/var/www/html/wp-settings.php').content.gsub('.phpp', '.php'),
}
