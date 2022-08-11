echo "#============================================#"
echo "Welcome to Debian Version: $(tail -n +1 /etc/os-release | tr -d \" | grep VERSION_ID | cut -c 12-) !"
echo "#============================================#"
