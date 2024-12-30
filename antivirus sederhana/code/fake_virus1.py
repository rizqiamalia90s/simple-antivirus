import time
import sys

def main():
    counter = 1
    try:
        print("Program perhitungan maju dimulai...")
        print("Tekan Ctrl+C untuk menghentikan program")
        while True:
            print(f"Hitungan ke-{counter}")
            counter += 1
            time.sleep(1)  # Jeda 1 detik antara setiap hitungan
            
    except KeyboardInterrupt:
        print("\nProgram dihentikan oleh pengguna")
        sys.exit(0)

if __name__ == "__main__":
    main()
