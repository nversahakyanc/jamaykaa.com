import os

# Set your root directory
root_dir = 'transcript/'  # change this if needed

for subdir, _, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.html'):
            file_path = os.path.join(subdir, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            new_content = content.replace(
                '@example',
                '@axtempl'
            )
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

print("✅ Replacement done.")
