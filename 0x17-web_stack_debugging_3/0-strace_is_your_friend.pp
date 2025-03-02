# Fixes bad `phpp` extensions to `php` in the WordPress file `wp-settings.php`
# Ensures that the file exists before running the sed command.

file { '/var/www/html/wp-settings.php':
  ensure => 'file',
}

exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/',
  onlyif  => 'test -f /var/www/html/wp-settings.php', # Ensure the file exists before running sed
}
