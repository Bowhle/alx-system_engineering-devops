# Ensure Python3 and pip3 are installed
package { 'python3':
  ensure => 'installed',
}

package { 'python3-pip':
  ensure => 'installed',
}

# Install Flask version 2.1.0 using pip3
package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip',
}

# Install Werkzeug version 2.1.1 as a requirement for Flask
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip',
  require  => Package['Flask'],
}

