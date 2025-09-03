import os
from PIL import Image
from glob import glob

# === CONFIGURATION ===
group_dir = "/content/DeepPCB/PCBData"
output_dir = "/content/pix2pix_data/train"
output_size = (256, 256)

# Create output folder
os.makedirs(output_dir, exist_ok=True)

total_processed = 0
skipped = 0

def resize_image(img, size):
    return img.resize(size, Image.BICUBIC)

for group_path in glob(os.path.join(group_dir, "group*")):
    for subfolder in os.listdir(group_path):
        folder_path = os.path.join(group_path, subfolder)

        test_images = glob(os.path.join(folder_path, "*_test.jpg"))

        for test_path in test_images:
            temp_path = test_path.replace("_test.jpg", "_temp.jpg")

            if not os.path.exists(temp_path):
                print(f"❌ Missing: {temp_path}")
                skipped += 1
                continue

            try:
                input_img = Image.open(test_path).convert('RGB')
                target_img = Image.open(temp_path).convert('RGB')

                # Ensure same size before resizing
                if input_img.size != target_img.size:
                    print(f"⚠️ Size mismatch: {test_path}")
                    skipped += 1
                    continue

                # Resize both together
                input_resized = resize_image(input_img, output_size)
                target_resized = resize_image(target_img, output_size)

                # Combine side by side
                concat_img = Image.new('RGB', (output_size[0] * 2, output_size[1]))
                concat_img.paste(input_resized, (0, 0))                 # Left: input
                concat_img.paste(target_resized, (output_size[0], 0))   # Right: target

                # Save
                filename = os.path.basename(test_path).replace("_test.jpg", ".jpg")
                output_path = os.path.join(output_dir, filename)
                concat_img.save(output_path)
                total_processed += 1

            except Exception as e:
                print(f"⚠️ Error: {test_path} - {e}")
                skipped += 1

print(f"\n✅ Done: {total_processed} images processed.")
if skipped > 0:
    print(f"⚠️ Skipped: {skipped} due to mismatch or errors.")
