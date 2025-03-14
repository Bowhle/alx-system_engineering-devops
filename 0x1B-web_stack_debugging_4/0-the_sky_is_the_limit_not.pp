# This script increases the ULIMIT of nginx default from 15 to 4096

# Increase the ULIMIT of nginx default
exec { 'increase-ulimit':
    command => '/bin/sed -i \'s/ULIMIT="-n 15"/ULIMIT="-n 4096"/\' /etc/default/nginx'
}

#restart nginx
exec { 'restart-nginx':
    command => '/usr/sbin/service nginx restart'
}

