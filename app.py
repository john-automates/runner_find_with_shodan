print("[+] START: MarkItDown Converter")
print("[~] Importing required modules...")

import os
print("[+] os module imported successfully")

import sys
print("[+] sys module imported successfully")

import shutil
print("[+] shutil module imported successfully")

# Print all environment variables
print("[~] All Environment Variables:")
for key, value in os.environ.items():
    print(f"{key}={value}")

print("[~] Setting up HOME cache directory...")
root_dir = '/tmp/root'
os.makedirs(root_dir, exist_ok=True)
os.chmod(root_dir, 0o777)
os.environ["HOME"] = root_dir
print(f"[+] HOME set to: {os.environ['HOME']}")
print("[+] HOME directory configured successfully")

# Print all environment variables
print("[~] All Environment Variables:")
for key, value in os.environ.items():
    print(f"{key}={value}")

try:
    print("[~] Checking command line arguments...")
    print(f"[DEBUG] Number of arguments: {len(sys.argv)}")
    print(f"[DEBUG] Arguments list: {sys.argv}")

    print("[~] Getting input filename...")
    file_name = sys.argv[1]
    print(f"[DEBUG] Input file: {file_name}")
    print("[~] ---")
    print("[~] Building file paths...")
    input_path = os.path.join(os.getcwd(), "inputs", file_name)
    print(f"[DEBUG] Current working directory: {os.getcwd()}")
    print(f"[DEBUG] Full input path: {input_path}")

    print("[~] Generating output filename...")
    output_filename = os.path.splitext(file_name)[0] + '.md'
    print(f"[DEBUG] Base filename without extension: {os.path.splitext(file_name)[0]}")
    print(f"[DEBUG] Output filename: {output_filename}")
    output_path = os.path.join(os.getcwd(), "outputs", output_filename)
    print(f"[DEBUG] Full output path: {output_path}")

    print("[~] Verifying input file exists...")
    if not os.path.exists(input_path):
        print(f"[ERROR] Input file not found at {input_path}")
        sys.exit(1)
    print("[+] Input file verified")

    print("[~] Creating output directory if needed...")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    print(f"[+] Output directory ready: {os.path.dirname(output_path)}")

    print(f"[~] Converting {file_name} to Markdown...")
    from markitdown import MarkItDown

    md = MarkItDown()
    print(f"[DEBUG] input_path: {input_path}")
    result = md.convert(input_path)
    print(f"[DEBUG] result: {result}")
    print("[+] File conversion completed")
    str_result_text_content = str(result.text_content)
    
    print("[~] Writing markdown content to output file...")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(str_result_text_content)
    print(f"[+] Markdown file created successfully at: {output_path}")

except Exception as e:
    print(f"[ERROR] An unexpected error occurred: {str(e)}")
    sys.exit(1)

print("[+] END: MarkItDown Converter")