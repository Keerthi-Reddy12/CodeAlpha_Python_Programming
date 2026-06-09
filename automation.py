import os
import shutil
print("📂 Welcome to your File Automation Script!")
print("_" * 40)
source_folder = "My_Messy_Folder"
target_folder = "Moved_Text_Files"
if not os.path.exists(source_folder):
    os.makedirs(source_folder)
    print(f"Created a dummy folder named '{source_folder}' for testing.")
    for i in range(1, 4):
        with open(f"{source_folder}/sample_file_{i}.txt", "w") as f:
            f.write("This is a sample text file for automation.")
    print("Added 3 sample .txt files into it.")
    print("_" * 40)
if not os.path.exists(target_folder):
    os.makedirs(target_folder)
print(f"Scanning '{source_folder}' for text files...")
files_in_source = os.listdir(source_folder)
moved_count = 0
for file_name in files_in_source:
    if file_name.endswith(".txt"):
        source_path = os.path.join(source_folder, file_name)
        target_path = os.path.join(target_folder, file_name)
        shutil.move(source_path, target_path)
        print(f"📦 Successfully moved: {file_name} -> {target_folder}/")
        moved_count += 1
print("_" * 40)
print(f"🎉 Automation complete! Moved {moved_count} files successfully.")
print("_" * 40)