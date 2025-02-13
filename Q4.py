import os
import shutil
import sys
import datetime

def backup_files(source_dir, dest_dir):
    # Check if source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return
    
    # Check if destination directory exists, create if not
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    for file_name in os.listdir(source_dir):
        source_file = os.path.join(source_dir, file_name)
        dest_file = os.path.join(dest_dir, file_name)
        
        if os.path.isfile(source_file):
            # If the file exists in the destination, append a timestamp
            if os.path.exists(dest_file):
                timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                name, ext = os.path.splitext(file_name)
                dest_file = os.path.join(dest_dir, f"{name}_{timestamp}{ext}")
                
            shutil.copy2(source_file, dest_file)
            print(f"Copied: {source_file} -> {dest_file}")
    
    print("Backup completed successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python Q3.py <source_directory> <destination_directory>")
    else:
        source_directory = sys.argv[1]
        destination_directory = sys.argv[2]
        backup_files(source_directory, destination_directory)
