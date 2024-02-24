# Set up SSH configuration file
file_line { 'Use a private key':
    ensure =>  'present',
    path   =>  '/etc/ssh/ssh_config',
    line   =>  '   IdentityFile            ~/.ssh/school',
}

file_line { "Don't authenticate using a password":
    ensure =>  'present',
    path   =>  '/etc/ssh/ssh_config',
    line   =>  '   PasswordAuthentication     no',
}
