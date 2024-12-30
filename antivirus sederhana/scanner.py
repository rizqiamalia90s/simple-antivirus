import os
import pyodbc
import psutil

def scan_file(filename):
    # Koneksi ke database
    conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Hp\My Docs\New Folder\db.dat')
    cursor = conn.cursor()
    
    # Query untuk mencari nama file di database
    cursor.execute("SELECT * FROM tbl_virrus WHERE nama_file_virus=?", filename)
    result = cursor.fetchone()
    
    if result:
        print(f"PERINGATAN: File {filename} adalah VIRUS!.")
    else:
        print(f"File {filename} aman.")
    
    conn.close()

def tampilkan_proses():
    # Koneksi ke database
    conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\Hp\My Docs\New Folder\db.dat')
    cursor = conn.cursor()
    
    print("\nDaftar Proses yang Berjalan:")
    print("-" * 120)
    print("{:<10} {:<30} {:<60} {:<15}".format("PID", "Nama Proses", "Path File", "Status"))
    print("-" * 120)
    
    try:
        for proc in psutil.process_iter(['pid', 'name', 'exe', 'cmdline']):
            try:
                # Dapatkan informasi proses
                pid = proc.info['pid']
                nama = proc.info['name']
                path = proc.info['exe'] if proc.info['exe'] else "Path tidak tersedia"
                cmdline = proc.info['cmdline']
                
                # Jika proses adalah python.exe, cek argumen command line
                if nama.lower() == 'python.exe' and cmdline and len(cmdline) > 1:
                    # Ambil nama file yang dijalankan oleh Python
                    script_path = cmdline[1]
                    nama = os.path.basename(script_path)
                    path = script_path
                
                # Cek status di database
                cursor.execute("SELECT * FROM tbl_virrus WHERE nama_file_virus=?", (nama,))
                result = cursor.fetchone()
                
                status = "Mencurigakan!" if result else "Normal"
                
                if len(path) > 57:
                    path = path[:54] + "..."
                
                print("{:<10} {:<30} {:<60} {:<15}".format(
                    pid, nama[:27] + "..." if len(nama) > 27 else nama,
                    path, status
                ))
                
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
                
    except Exception as e:
        print(f"Error saat membaca proses: {str(e)}")
    
    finally:
        conn.close()

def tampilkan_direktori_sekarang():
    print(f"\nDirektori saat ini: {os.getcwd()}")

def ganti_direktori():
    tampilkan_direktori_sekarang()
    try:
        new_dir = input("\nMasukkan path direktori baru (atau tekan Enter untuk batal): ").strip()
        if new_dir:
            os.chdir(new_dir)
            print(f"Direktori berhasil diubah ke: {os.getcwd()}")
        else:
            print("Perubahan direktori dibatalkan")
    except Exception as e:
        print(f"Error: Tidak dapat mengubah direktori. {str(e)}")

def baca_file():
    tampilkan_direktori_sekarang()
    nama_file = input("\nMasukkan nama file yang ingin dibaca: ")
    
    try:
        if os.path.exists(nama_file):
            with open(nama_file, 'r', encoding='utf-8') as file:
                print(f"\nIsi file {nama_file}:")
                print("-" * 50)
                print(file.read())
                print("-" * 50)
        else:
            print(f"File {nama_file} tidak ditemukan.")
    except Exception as e:
        print(f"Error saat membaca file: {str(e)}")

def tampilkan_isi_folder():
    tampilkan_direktori_sekarang()
    print("\nDaftar file dan folder:")
    print("-" * 80)
    print("{:<50} {:<10} {:<20}".format("Nama", "Tipe", "Ukuran (bytes)"))
    print("-" * 80)
    
    try:
        for item in os.listdir():
            path = os.path.join(os.getcwd(), item)
            size = os.path.getsize(path) if os.path.isfile(path) else "-"
            tipe = "File" if os.path.isfile(path) else "Folder"
            
            # Potong nama yang terlalu panjang
            if len(item) > 47:
                item = item[:44] + "..."
                
            print("{:<50} {:<10} {:<20}".format(item, tipe, size))
    except Exception as e:
        print(f"Error saat membaca folder: {str(e)}")

def kill_proses():
    try:
        pid = input("\nMasukkan PID proses yang ingin dihentikan: ")
        if not pid.isdigit():
            print("Error: PID harus berupa angka")
            return
            
        pid = int(pid)
        proses = psutil.Process(pid)
        
        # Tampilkan informasi proses sebelum kill
        print(f"\nProses yang akan dihentikan:")
        print(f"PID: {pid}")
        print(f"Nama: {proses.name()}")
        
        konfirmasi = input("\nAnda yakin ingin menghentikan proses ini? (y/n): ")
        if konfirmasi.lower() == 'y':
            proses.kill()
            print(f"Proses dengan PID {pid} berhasil dihentikan")
        else:
            print("Pembatalan penghentian proses")
            
    except psutil.NoSuchProcess:
        print(f"Error: Proses dengan PID {pid} tidak ditemukan")
    except psutil.AccessDenied:
        print(f"Error: Tidak memiliki izin untuk menghentikan proses dengan PID {pid}")
    except Exception as e:
        print(f"Error: {str(e)}")

def hapus_file():
    tampilkan_direktori_sekarang()
    try:
        nama_file = input("\nMasukkan nama file yang ingin dihapus: ")
        if os.path.exists(nama_file):
            # Tampilkan informasi file sebelum menghapus
            print(f"\nInformasi file yang akan dihapus:")
            print(f"Nama file: {nama_file}")
            print(f"Ukuran: {os.path.getsize(nama_file)} bytes")
            print(f"Path lengkap: {os.path.abspath(nama_file)}")
            
            konfirmasi = input("\nAnda yakin ingin menghapus file ini? (y/n): ")
            if konfirmasi.lower() == 'y':
                os.remove(nama_file)
                print(f"\nFile {nama_file} berhasil dihapus!")
            else:
                print("\nPenghapusan file dibatalkan.")
        else:
            print(f"\nFile {nama_file} tidak ditemukan.")
    except Exception as e:
        print(f"Error saat menghapus file: {str(e)}")

def scan_multiple_files():
    while True:
        print("\nMenu Scanner Virus:")
        print("1. Pindai file")
        print("2. Tampilkan Proses Berjalan")
        print("3. Ganti Direktori")
        print("4. Tampilkan Isi Folder")
        print("5. Baca File")
        print("6. Kill Proses")
        print("7. Hapus File")
        print("8. Keluar")
        
        pilihan = input("Pilih menu (1-8): ")
        
        if pilihan == "1":
            tampilkan_direktori_sekarang()
            file_to_scan = input("Masukkan nama file yang akan dipindai: ")
            
            if os.path.exists(file_to_scan):
                print(f"\nMemulai pemindaian file: {file_to_scan}")
                scan_file(file_to_scan)
            else:
                print(f"\nFile {file_to_scan} tidak ditemukan.")
        
        elif pilihan == "2":
            tampilkan_proses()
        
        elif pilihan == "3":
            ganti_direktori()
        
        elif pilihan == "4":
            tampilkan_isi_folder()
        
        elif pilihan == "5":
            baca_file()
        
        elif pilihan == "6":
            kill_proses()
        
        elif pilihan == "7":
            hapus_file()
        
        elif pilihan == "8":
            print("Terima kasih telah menggunakan scanner virus!")
            break
        
        else:
            print("Pilihan tidak valid. Silakan pilih 1-8.")
if __name__ == "__main__":
    scan_multiple_files()
