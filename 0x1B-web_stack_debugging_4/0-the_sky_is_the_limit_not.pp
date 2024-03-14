# handle more traffic

exec { 'nginx-fix
  command => 'sed -i "s/15/5000/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
} ->

exec { 'restart':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
