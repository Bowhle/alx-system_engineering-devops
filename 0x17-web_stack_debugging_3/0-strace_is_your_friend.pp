# Ensures that wp-settings.php exists before modifying it
file { '/var/www/html/wp-settings.php':
  ensure => 'file',
  before => Exec['fix-wordpress'], # Ensures file is created before exec runs
}

# Runs sed to fix incorrect 'phpp' extensions
exec { 'fix-wordpress':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/bin/:/bin/',
}
