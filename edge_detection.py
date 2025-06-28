import numpy as np
from pynq import Overlay
from pynq import allocate
from PIL import Image
import time
import matplotlib.pyplot as plt

def main():
    # Load overlay (replace with your overlay name)
    overlay = Overlay("design_2.bit")
    overlay.download()

    # Get reference to sobel IP (update 'hls_sobel_axi_stream_0' with your IP name)
    sobel_ip = overlay.hls_sobel_axi_stream_0

    # Load image and convert to grayscale
    img = Image.open("test_image.jpg").convert('L')
    img_np = np.array(img)

    # Ensure image size matches your hardware buffer size or is padded accordingly
    height, width = img_np.shape
    print(f"Image dimensions: {width}x{height}")

    # Allocate contiguous memory for input and output
    in_buffer = allocate(shape=(height, width), dtype=np.uint8)
    out_buffer = allocate(shape=(height, width), dtype=np.uint8)

    # Copy image data to input buffer
    np.copyto(in_buffer, img_np)
    in_buffer.flush()

    # Print some debug info
    print("Input buffer sample (top-left 5x5):")
    print(in_buffer[0:5, 0:5])

    # Set up hardware registers and start processing
    sobel_ip.write(0x10, in_buffer.physical_address)  # Input buffer address register
    sobel_ip.write(0x18, out_buffer.physical_address)  # Output buffer address register
    sobel_ip.write(0x20, width)  # Image width
    sobel_ip.write(0x28, height)  # Image height
    sobel_ip.write(0x00, 0x01)  # Start the IP (assuming bit 0 is start)

    # Wait for IP to finish with timeout
    start_time = time.time()
    while (sobel_ip.read(0x00) & 0x1):
        if time.time() - start_time > 5:  # 5 seconds timeout
            print("Timeout waiting for IP")
            break
        time.sleep(0.01)

    print("Processing complete")
    out_buffer.invalidate()

    # Print some debug info
    print("Output buffer sample (top-left 5x5):")
    print(out_buffer[0:5, 0:5])

    # Normalize output if needed (Sobel can produce values outside 0-255)
    output_np = np.array(out_buffer, dtype=np.uint8)
   
    # Check if output is all zeros
    if np.all(output_np == 0):
        print("Warning: Output is all zeros!")
    else:
        print(f"Output range: {output_np.min()} to {output_np.max()}")

    # Convert output buffer to image
    output_img = Image.fromarray(output_np)

    # Display input and output images side by side
    plt.figure(figsize=(10, 5))
    plt.subplot(1, 2, 1)
    plt.imshow(img, cmap='gray')
    plt.title('Input Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(output_img, cmap='gray')
    plt.title('Sobel Edge Detection')
    plt.axis('off')

    plt.tight_layout()
    plt.show()

    # Save output image to file
    output_img.save("output_sobel.jpg")
    print("Output saved as output_sobel.jpg")

    # Clean up
    in_buffer.close()
    out_buffer.close()
    
if _name_ == "_main_":
    main()