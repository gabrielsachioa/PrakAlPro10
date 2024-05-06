def parse_email_log(filename):
  """Membaca log email dan mengembalikan dictionary histogram dan dictionary jumlah pesan."""
  histogram = {}
  email_counts = {}
  
  with open(filename, 'r') as file:
    for line in file:
      # Cari baris yang berisi alamat email
      email_index = line.find("From:")
      if email_index != -1:
        email_end_index = line.find("\n", email_index)
        email = line[email_index + 6:email_end_index].strip()
        
        # Hitung jumlah pesan dari email ini
        if email not in email_counts:
          email_counts[email] = 0
        email_counts[email] += 1
        
        # Dapatkan kata-kata dalam baris
        words = line.split()
        words = [word for word in words if word != "From:"]  # Hapus "From:"
        words = [word for word in words if word != email]  # Hapus alamat email
        
        # Perbarui histogram kata
        for word in words:
          if word not in histogram:
            histogram[word] = 0
          histogram[word] += 1
  
  return histogram, email_counts

# Program utama
filename = "mbox-short.txt"
histogram, email_counts = parse_email_log(filename)

print("Jumlah Pesan per Email:")
print(email_counts)
