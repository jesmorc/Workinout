# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "azure"
  config.vm.network "public_network"
  config.vm.network "private_network",ip: "192.168.56.10", virtualbox__intnet: "vboxnet0"
  config.vm.network "forwarded_port", guest: 80, host: 80
  config.vm.define "localhost" do |l|
          l.vm.hostname = "localhost"
  end

  config.vm.provider :azure do |azure, override| 
    azure.mgmt_certificate = File.expand_path('~/.ssh/azurevagrant.pem') 
    azure.mgmt_endpoint = 'https://management.core.windows.net'
    azure.subscription_id = 'c0428c40-ac09-44a8-9362-32f8256ae427'
    azure.vm_image = 'b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_04_2-LTS-amd64-server-20150506-en-us-30GB'
    azure.vm_name = 'iv-jesmorc-ubuntuserver' 
    azure.vm_password = 'CACAjes1990!'
    azure.vm_location = 'Central US' 
    azure.ssh_port = '22'
    azure.tcp_endpoints = '80:80'
  end

  config.vm.provision "ansible" do |ansible|
        ansible.sudo = true
        ansible.playbook = "playbookansible.yml"
        ansible.verbose = "v"
        ansible.host_key_checking = false
  end
end
