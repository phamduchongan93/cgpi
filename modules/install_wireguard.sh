# Name: install wiregoard on server


generate_private_key () {

}

generate_public_key () {
  sudo_check 
  cat /etc/wireguard/private.key | wg pubkey | sudo tee /etc/wireguard/public.key
}
