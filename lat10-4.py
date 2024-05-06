def parse_email_log(filename):
  """Membaca log email dan mengembalikan dictionary nama domain dan jumlah pesan."""
  domain_counts = {}
  
  with open(filename, 'r') as file:
    for line in file:
      # Cari baris yang berisi alamat email
      email_index = line.find("From:")
      if email_index != -1:
        email_end_index = line.find("\n", email_index)
        email = line[email_index + 6:email_end_index].strip()
        
        # Dapatkan nama domain pengirim
        domain_start_index = email.find("@")
        if domain_start_index != -1:
          domain_end_index = email.find(" ", domain_start_index)
          if domain_end_index == -1:
            domain_end_index = len(email)
          domain = email[domain_start_index + 1:domain_end_index]
          
          # Hitung jumlah pesan dari domain ini
          if domain not in domain_counts:
            domain_counts[domain] = 0
          domain_counts[domain] += 1
  
  return domain_counts

# Program utama
filename = "mbox-short.txt"
domain_counts = parse_email_log(filename)

print(domain_counts)
