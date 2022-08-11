VERSION_ID=$(cat /etc/os-release | grep VERSION_ID | cut -c 12-)
echo "#============================================#"
echo "Welcome to Fedora Version: ${VERSION_ID}!"
echo "#============================================#"
