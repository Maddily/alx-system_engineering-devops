# Manage the content of wp-settings.php file, replacing .phpp with .php

exec { 'Correct php':
  command  => 'sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
