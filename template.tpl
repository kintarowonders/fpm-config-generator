[%USER%]

listen = /var/run/php-fpm/%USER%
listen.owner = nginx
listen.group = nginx
listen.mode = 0666
user = %USER%
group = %USER%

pm = dynamic

pm.max_children = 50
pm.min_spare_servers = 10
pm.max_spare_servers = 35

php_admin_value[error_log] = /home/%USER%/php-fpm.log
php_flag[display_errors] = off
